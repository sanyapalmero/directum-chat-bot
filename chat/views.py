from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse
from .models import Support

class IndexView(View):
    """Главная страница"""
    def get(self, request):
        template_name = 'chat/index.html'
        return render(request, template_name)


class ChatView(View):
    """Страница чата"""
    template_name = 'chat/chat.html'
    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        user_message = request.POST['user-message']
        if user_message == "Привет!":
            return JsonResponse({'UserMessage':user_message, 'BotMessage':'Привет :)'})
        elif user_message == "Как дела?":
            return JsonResponse({'UserMessage':user_message, 'BotMessage':'Замечательно!'})
        else:
            return JsonResponse({'UserMessage':user_message, 'BotMessage':'Непонятный для меня запрос :('})


class FaqView(View):
    """FAQ страница"""
    def get(self, request):
        template_name = 'chat/faq.html'
        return render(request, template_name)


class SupportView(View):
    """Страница просмотра саппортов"""
    def get(self, request):
        template_name = 'chat/supports.html'
        supports = Support.objects.all()
        return render(request, template_name, {'supports':supports})


class CreateSupportView(View):
    """Страница создания саппортов"""
    def get(self, request):
        template_name = 'chat/supcreate.html'
        return render(request, template_name)

    def post(self, request):
        name = request.POST['name']
        description = request.POST['description']
        key_words = request.POST['key_words']

        Support.objects.create(
            name=name,
            description=description,
            key_words=key_words
        )
        return redirect('chat:supports')


class EditSupportView(View):
    """Страница изменения саппортов"""
    def get(self, request, sup_id):
        template_name = 'chat/supedit.html'
        support = Support.objects.get(pk=sup_id)
        return render(request, template_name, {'support':support})

    def post(self, request, sup_id):
        support = Support.objects.get(pk=sup_id)

        support.name = request.POST['name']
        support.description = request.POST['description']
        support.key_words = request.POST['key_words']
        support.save()

        return redirect('chat:supports')


class DeleteSupportView(View):
    """Страница удаления саппортов"""
    def get(self, request, sup_id):
        template_name = 'chat/supdelete.html'
        support = Support.objects.get(pk=sup_id)
        return render(request, template_name, {'support':support})

    def post(self, request, sup_id):
        support = Support.objects.get(pk=sup_id)
        support.delete()
        return redirect('chat:supports')

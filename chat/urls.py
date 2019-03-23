from django.urls import include, path
from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('chat/', views.ChatView.as_view(), name='chat'),
    path('supports/', views.SupportView.as_view(), name='supports'),
    path('supports/create/', views.CreateSupportView.as_view(), name='supcreate'),
    path('supports/edit/<int:sup_id>', views.EditSupportView.as_view(), name='supedit'),
    path('supports/delete/<int:sup_id>', views.DeleteSupportView.as_view(), name='supdelete'),
    path('faq/', views.FaqView.as_view(), name='faq')
]

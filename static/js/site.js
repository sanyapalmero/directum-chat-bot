$(document).ready(function(){
    $('#send-message').click(function(){
        var userMessage = showUserMessage();
        sendUserMessageAjax(userMessage);
    });
});

var countUserMessages = 0;
function showUserMessage(){
    var messageText = $('#user-message').val();
    var messageId = "messageId-" + countUserMessages;
    var messageBlock = $('<div>', {'class':'message', 'id':messageId}).prependTo('.chat-window');
    var userMessageBlock = $('<div>', {'class':'user-message'}).prependTo(messageBlock);
    $('<p>', {'text':"Вы: " + messageText}).prependTo(userMessageBlock);
    $('#user-message').val("");
    countUserMessages++;
    return messageText;
}

var countBotMessages = 0;
function showBotMessage(message){
    var messageText = message;
    var messageId = "messageId-" + countBotMessages;
    var messageBlock = $('<div>', {'class':'message', 'id':messageId}).prependTo('.chat-window');
    var userMessageBlock = $('<div>', {'class':'bot-message'}).prependTo(messageBlock);
    $('<p>', {'text':"Бот: " + messageText}).prependTo(userMessageBlock);
    $('#user-message').val("");
    countBotMessages++;
    return messageText;
}

function sendUserMessageAjax(userMessage){
    var data = {};
    data['user-message'] = userMessage;
    $.ajax({
        headers: {
            "X-CSRFToken": getCookie('csrftoken'),
        },
        method: 'POST',
        url:'/chat/',
        data: data,
        dataType: 'json',
        success: function(response) {
            var botMessage = response.BotMessage;
            showBotMessage(botMessage);
            console.log(response);
        },
    });
}

function getCookie(name) {
    var cookieValue = null;
    var i = 0;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (i; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

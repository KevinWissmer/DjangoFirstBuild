from django.shortcuts import render
from .models import Message, Chat
from django.http import HttpResponseRedirect

def index(request):
    
    if request.method == 'POST':
        print("recieved data: " + request.POST['textmessage'])
        myChat = Chat.objects.get(id=1)
        Message.objects.create(text=request.POST['textmessage'], chat=myChat ,author=request.user ,receiver=request.user)
        return HttpResponseRedirect('/chat/')
    chatMessages = Message.objects.filter(chat__id=1)
    return render(request, 'chat/index.html', {'name': request.user, 'messages': chatMessages})



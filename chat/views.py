from django.shortcuts import render
from .models import Message, Chat
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login

@login_required(login_url='/login/')
def index(request):
    if request.method == 'POST':
        print("recieved data: " + request.POST['textmessage'])
        myChat = Chat.objects.get(id=1)
        Message.objects.create(text=request.POST['textmessage'], chat=myChat ,author=request.user ,receiver=request.user)
        return HttpResponseRedirect('/chat/')
    chatMessages = Message.objects.filter(chat__id=1)
    return render(request, 'chat/index.html', {'name': request.user, 'messages': chatMessages})

def loginView(request):
    if request.method == 'POST':
        #print("recieved data: " + request.POST['textmessage'])
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        print(user)
        if user is not None:
            
            login(request, user)
            return HttpResponseRedirect('/chat/')
        else:
            print(user)
            return render(request, 'auth/login.html', {'wrong_password': True})
        #return HttpResponseRedirect('/chat/')
    return render(request, 'auth/login.html')

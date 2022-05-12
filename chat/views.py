from django.shortcuts import render

def index(request):
    if request.method == 'POST':
        print("recieved data: " + request.POST['textmessage'])
    return render(request, 'chat/index.html', {'name': request})

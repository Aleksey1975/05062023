from django.shortcuts import render

def signupuser(request):
    return render(request, 'signupuser/todo/signupuser.html')

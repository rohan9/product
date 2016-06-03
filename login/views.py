from django.shortcuts import render
from .forms import LoginForm
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from .models import User
from django.http import HttpResponseRedirect, HttpResponse



def post_list(request):
    return render(request,'login/login.html',{})


def check_pass(request):
    if request.method == 'POST':
       # print(username, password)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return render_to_response('login/product.html')
        else:
            return HttpResponseRedirect('/')

    else:
        return render_to_response('login/login.html')

from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from .forms import UserRegisterForm,ProfileUpdateForm,UserUpdateForm,CommentForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .serializers import CurrentUserSerializer
from rest_framework.parsers import JSONParser
from django.contrib.auth import authenticate
from .models import FormSubmit,UserMetaData
from django.http import HttpResponse


def register(request):
    if request.method =="POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('blog-login')
    else:
        form = UserRegisterForm()
    return render(request,'Users/register.html',context={'form':form})

@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST,instance=request.user)
        s_form = CommentForm(request.POST,instance=request.user)
        
    else:
        u_form = UserUpdateForm(instance=request.user)
        s_form = CommentForm(instance=request.user)

    if u_form.is_valid():
        u_form.save()

    if s_form.is_valid():
        # print(CheckerAdmin.objects.filter(user_using=request.user).first(),"\n\n\n\n\n\n\n\n\n")
        u = request.user
        print(u)
        comment = FormSubmit(task_choosen=s_form.cleaned_data["task_choosen"],
                            user_using= request.user,others=s_form.cleaned_data['others']
                            ,hours_spent=s_form.cleaned_data["hours_spent"])
        comment.save()

        return redirect('blog-profile')

    context = {
        'u_form': u_form,
        's_form':s_form
    }
    return render(request,'Users/profile.html',context = context)

@login_required
def seeing_dashboard(request):
    data = None
    pass

@csrf_exempt
def users_list(request):
    if request.method == "GET":
        # query 
        users = User.objects.all()
        serializer = CurrentUserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        # here data comes to drf and we need to deserialize it...
        data = JSONParser().parse(request)
        serializer = CurrentUserSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse(serializer.data,status=201) # send the status code too and the serialized data..
        return JsonResponse(serializer.errors, status=400)
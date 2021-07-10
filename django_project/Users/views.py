from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .forms import UserRegisterForm, ProfileUpdateForm, UserUpdateForm, CommentForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .serializers import CurrentUserSerializer
from rest_framework.parsers import JSONParser
from django.contrib.auth import authenticate
from .models import FormSubmit, UserMetaData
from django.http import HttpResponse
from .models import UserMetaData, UserTotalHour

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            return redirect("blog-login")
    else:
        form = UserRegisterForm()
    return render(request, "Users/register.html", context={"form": form})

@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile
        )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect("blog-profile")
    else:
        s_form = CommentForm(user=request.user)
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        print(request.META.get("REMOTE_ADDR"),"==========================")

    context = {"u_form": u_form, "p_form": p_form, "s_form": s_form}

    return render(request, "Users/profile.html", context)

@login_required
def comment(request):
    if request.method == "POST":
        s_form = CommentForm(request.POST, user=request.user)
        if s_form.is_valid():
            comment = FormSubmit(
                task_chosen=s_form.cleaned_data["task_chosen"],
                user_using=request.user,
                others=s_form.cleaned_data["others"],
                hours_spent=s_form.cleaned_data["hours_spent"],
            )
            comment.save()
            return redirect("blog-profile")
        return HttpResponse("<h1>Vapas Bharkar Aao</h1>")
    else:
        return HttpResponse("<h1>Vapas Bharke Aao</h1>")

@login_required
def seeing_dashboard(request):
    # Users all hours spent.

    def get_client_ip(request):
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            ip = x_forwarded_for.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR")
        return ip

    data = UserMetaData.objects.filter()
    print((data))
    for present_user in list(data):
        print(present_user.user, present_user.total_hours)
    context = {"data": data}
    return render(request, "Users/dashboard.html", context=context)


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

            return JsonResponse(
                serializer.data, status=201
            )  # send the status code too and the serialized data..
        return JsonResponse(serializer.errors, status=400)

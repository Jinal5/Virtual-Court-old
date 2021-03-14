from django.shortcuts import render
from django.views.generic import *
from django.views.generic.edit import *
from .models import *
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib import messages


class UserFormView(View):
    form_class = UserForm
    template_name = "court/registration_form.html"

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            password1 = form.cleaned_data["password1"]
            user_type = form.cleaned_data["user_type"]
            court = form.cleaned_data["court"]
            address = form.cleaned_data["address"]
            license_no = form.cleaned_data["license_no"]

            if password == password1:
                user.set_password(password)
                user.save()
                user = User.objects.get(username=username)
                user_profile = UserProfile.objects.get(user=user)
                user_profile.user_type = user_type
                user_profile.save()
                advocate_details=Advocate()
                advocate_details.user=request.user
                advocate_details.license_no=license_no
                advocate_details.name=first_name+last_name
                advocate_details.court_type=court_type
                advocate_details.address=address
                messages.success(request, "Account register successfully")
                return redirect("court:login")
            else:
                messages.success(request, "Password does not match")
        else:
            return render(request, self.template_name, {"form": form})


class LoginView(View):
    form_class = LoginForm
    template_name = "court/login.html"

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                user_profile=UserProfile.objects.filter(user=request.user)
                user_type=user_profile.user_type
                if user_type=="Lawyer":
                    return redirect("court:advocate")
                elif user_type=="Judge":
                    return redirect("court:judge")
                else:
                    return redirect("court:login",{"Wrong User Type"})

                # messages.info(request, 'Your have successfully loged in!')git              
            else:
                return render(
                    request,
                    "court/login.html",
                    {"error_message": "Your account has been disabled"},
                )
        else:
            return render(
                request,
                "music/login.html",
                {"form": form, "error_message": "Invalid login"},
            )


class LogoutView(View):
    form_class = LoginForm
    template_name = "court/login.html"

    def get(self, request):
        form = self.form_class(None)
        logout(request)
        return redirect(reverse("court:login"))


def home(request):
    return render(request, "court/home.html", {"title": "Home"})


def about(request):
    return render(request, "court/about.html", {"title": "About"})


# Create your views here.

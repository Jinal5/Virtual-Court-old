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
import random, string
from court.utils import get_judge

def generateKey():
    x = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
    return x

def generateNo():
    x = ''.join(random.choice(string.digits) for _ in range(8))
    return x    

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
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            user_type = form.cleaned_data["user_type"]
            court = form.cleaned_data["court"]
            address = form.cleaned_data["address"]
            license_no = form.cleaned_data["license_no"]

            if password == password1:
                if user_type=="Lawyer":
                    user.set_password(password)
                    user.save()
                    user = User.objects.get(username=username)
                    user_profile = UserProfile.objects.get(user=user)
                    user_profile.user_type = user_type
                    user_profile.save()
                    advocate_details=Advocate()
                    advocate_details.user=user
                    advocate_details.license_no=license_no
                    advocate_details.name=first_name+last_name
                    advocate_details.court_type=court
                    advocate_details.address=address
                    advocate_details.save()
                    messages.success(request, "Account register successfully")
                    return redirect("court:login")
                elif user_type=="Judge":
                    user.set_password(password)
                    user.save()
                    user = User.objects.get(username=username)
                    user_profile = UserProfile.objects.get(user=user)
                    user_profile.user_type = user_type
                    user_profile.save()
                    judge_details=Judge()
                    judge_details.user=user
                    judge_details.license_no=license_no
                    judge_details.name=first_name+last_name
                    judge_details.court_type=court
                    judge_details.address=address
                    judge_details.save()
                    messages.success(request, "Account register successfully")
                    return redirect("court:login")
                else: 
                    messages.success(request, "Wrong user type")
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
                user_profile=UserProfile.objects.get(user=request.user)
                # print(user_profile)
                user_type=user_profile.user_type
                # print(user_type)
                if user_type=="Lawyer":
                    return render(request, "court/advocate.html")
                elif user_type=="Judge":
                    return render(request, "court/judge.html")
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
                "court/login.html",
                {"form": form, "error_message": "Invalid login"},
            )

# class JudgeView(View):
#     form_class = LoginForm
#     template_name = "court/judge.html"

#     def get(self, request):
#         form = self.form_class(None)
#         return render(request, self.template_name, {"form": form})

# class AdvocateView(View):
#     form_class = LoginForm
#     template_name = "court/advocate.html"

#     def get(self, request):
#         form = self.form_class(None)
#         return render(request, self.template_name, {"form": form})

class FileCase(LoginRequiredMixin,View):
    form_class=CaseForm
    template_name='court/fileCase.html'
        
    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            provider=form.save(commit=False)
            phone_number=form.cleaned_data["phone_number"]
            if phone_number>=6000000000 and phone_number<=9999999999:
                form.instance.advocate = self.request.user
                form.instance.cnr=generateKey()
                form.instance.fileNo=generateNo()
                print(form.instance.court_type)
                print(form.instance.district)
                form.instance.judge=get_judge(form.instance.court_type,form.instance.district)
                provider.save()
                return render(request, 'court/advocate.html')
            
        else:
            return render(request,self.template_name,{'form':form})

class LogoutView(View):
    form_class = LoginForm
    template_name = "court/login.html"

    def get(self, request):
        form = self.form_class(None)
        logout(request)
        return redirect(reverse("court:login"))

# class SearchView(ListView):
#     template_name = 'court/status.html'
#     context_object_name = "case_details"
#     model = Case

#     def get_queryset(self):
#         cnr = self.kwargs.get('cnr', '')
#         object_list = self.model.objects.all()
#         if cnr:
#             object_list = object_list.filter(cnr__icontains=cnr)
#         print(object_list)
#         return object_list

class SearchView(ListView):
    template_name = 'court/status.html'
    context_object_name = "case_details"
    model = Case

    def get_queryset(self):
       result = super(SearchView, self).get_queryset()
       query = self.request.GET.get('search')
       if query:
          postresult = Case.objects.filter(cnr__icontains=query)
          result = postresult
       else:
           result = None
       return result

# class SearchForm(View):
#     form_class=SearchForm
#     template_name='court/search.html'
    
#     def get(self,request):
#         form=self.form_class(None)
#         return render(request,self.template_name,{'form':form})

#     def post(self,request):
#         form=self.form_class(request.POST)
#         if form.is_valid():
#             cnr=form.cleaned_data["cnr"]
#             return redirect(reverse("court:status",cnr))

def home(request):
    return render(request, "court/home.html", {"title": "Home"})


def about(request):
    return render(request, "court/about.html", {"title": "About"})

def search(request):
    return render(request, "court/search.html", {"title": "search"})

def feecalc(request):
    return render(request, "court/feecalc.html", {"title": "Fee Calculator"})

class FeesFormView(View):
    form_class = FeesForm
    template_name = "court/feecalc.html"

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            court = request.POST['court']
            case = request.POST['case']
            subtype = request.POST['subtype']
            CourtType = {
                'Supreme court' : 500,
                'High court' : 300,
                'District court' : 200,
                'Sessions court' : 100
            }
            CaseType = {
                'Civil' : 200,
                'Criminal' : 400
            }
            CaseSubtype = {
                'Arbitration Cases' : 150,
                'Rent Petitions' : 50,
                'Recovery Suits' : 100,
                'Civil Appeals' : 200,
                'Transfer Applications' : 75,
                'Bail Applications' : 100,
                'Criminal Appeals' : 250,
                'Criminal Revision Cases' : 80,
                'Maintenance Cases' : 90,
                'Miscellaneous Applications' : 100
            }
            fees = CourtType[court] + CaseType[case] + CaseSubtype[subtype]
            results = {
                'fees' : fees,
                'court' : court,
                'case' : case,
                'subtype' : subtype
            }
            return render(request, "court/fees.html", results)

        else:
            return render(request, self.template_name, {"form": form})


# Create your views here.

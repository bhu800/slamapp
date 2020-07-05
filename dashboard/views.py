from django.shortcuts import render, get_object_or_404, reverse, redirect
from . import forms
from dashboard.models import tableThree, senior_users
from django.views.generic import View,TemplateView,ListView,DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.conf import settings

# Create your views here.
def index(request):
    return render(request, 'dashboard/template.html')

def HomePageView(request, *args, **kwargs):
    if request.user.is_authenticated:
        return redirect(settings.LOGIN_REDIRECT_URL) 
    return render(request, 'home.html', context={})

def dashboardPageView(request):
    return render(request, 'dashboard/examples/dashboard.html', context={})

def basePageView(request):
    return render(request, 'dashboard/layouts/base.html', context = {})

@login_required
def userPageView(request):
    if (senior_users.objects.filter(email=request.user.email).exists()):
        return render(request, 'dashboard/user.html', context={"is_senior":True}) 
    return render(request, 'dashboard/user.html', context={"is_senior":False}) 

def letterPageView(request):
    seniors = senior_users.objects.all()
    # if request.user.email is in seniors.email:
    print(seniors.filter(email=request.user.email).exists())
    if (seniors.filter(email=request.user.email).exists()):
        return render (request, 'dashboard/letter.html', context={"seniors":seniors, "is_senior":True})
    return render (request, 'dashboard/letter.html', context={"seniors":seniors, "is_senior":False})


# def showSlamBooks_all_PageView(request):
#     seniors = senior_users.objects.all()
#     colors = {"#CFD0FF", "#FFF3C3", "#FECCCB", "#A3E9C6", "#a6dcef", "#9aceff", "#a7e9af", "#a0ffe6", "#d5fffd", "#ffa5b0", "#f6def6"}
#     zipped = list(zip(seniors, colors))
#     print(zipped)
#     print(seniors)
#     return render(request, 'dashboard/showSlamBooks_all.html', {'zip':zipped})

# def showSlamBooks_my_PageView(request):
#     slams = tableThree.objects.all()   # <---- this is to be changed!!!
#     return render(request, 'dashboard/showSlambook_my.html')

# def show_slambook_entry_PageView(request):
#     slam = tableThree.objects.get(id = 1) # <----- this is temporary!!!
#     return render(request, 'dashboard/show_slambook_entry.html', {'slam':slam})

 # naman's work
def fillSlambook_PageView(request):
    form = forms.fillSlambook()
    if request.method == 'POST':
        form = forms.fillSlambook(request.POST)

        if form.is_valid():
            print("all good")
            junior="naman" # must be taken from login
            senior="naman" # must be taken from login
            obj = tableThree(
                junior=junior,
                senior=senior,
                ans1=form.cleaned_data['ans1'],
                ans2=form.cleaned_data['ans2'],
                ans3=form.cleaned_data['ans3'],
                ans4=form.cleaned_data['ans4'],
                ans5=form.cleaned_data['ans5'],
                ans6=form.cleaned_data['ans6'],
                ans7=form.cleaned_data['ans7'],
                ans8=form.cleaned_data['ans8'],
                ans9=form.cleaned_data['ans9'],
                ans10=form.cleaned_data['ans10'],
                ans11=form.cleaned_data['ans11'],
                ans12=form.cleaned_data['ans12'],
                ans13=form.cleaned_data['ans13'],
                ans14=form.cleaned_data['ans14'],
                ans15=form.cleaned_data['ans15']
            )
            obj.save()
            print("data saved")
    if (senior_users.objects.filter(email=request.user.email).exists()):
        return render(request,'dashboard/fillSlambook.html',{'form':form, "is_senior":True})
    return render(request,'dashboard/fillSlambook.html',{'form':form, "is_senior":False})

class showSlambooksAll(LoginRequiredMixin,ListView):
    template_name='dashboard/showSlamBooks_all.html'
    # print("hello")
    colors = ["#CFD0FF", "#FFF3C3", "#FECCCB", "#A3E9C6", "#a6dcef", "#9aceff", "#a7e9af", "#a0ffe6", "#d5fffd", "#ffa5b0", "#f6def6", "#CFD0FF", "#FFF3C3", "#FECCCB", "#A3E9C6", "#a6dcef", "#9aceff", "#a7e9af", "#a0ffe6", "#d5fffd", "#ffa5b0", "#f6def6", "#f2aaaa", "#dbc6eb", "#bbf1cb", "#abc2e8", "b4f2e1"] 
    queryset = list(zip(senior_users.objects.all(), colors))
    context_object_name = 'zip'
    # def test_func(self):
    #     return senior_users.objects.filter(email=request.user.email).exists()


class showSlambooksMyListView(LoginRequiredMixin,ListView, UserPassesTestMixin):
    template_name='dashboard/showSlamBooks_my.html'
    colors = ["#CFD0FF", "#FFF3C3", "#FECCCB", "#A3E9C6", "#a6dcef", "#9aceff", "#a7e9af", "#a0ffe6", "#d5fffd", "#ffa5b0", "#f6def6", "#CFD0FF", "#FFF3C3", "#FECCCB", "#A3E9C6", "#a6dcef", "#9aceff", "#a7e9af", "#a0ffe6", "#d5fffd", "#ffa5b0", "#f6def6"] 
    queryset = list(zip(tableThree.objects.all(), colors))
    context_object_name = 'zip'
    # def test_func(self):
    #     return senior_users.objects.filter(email=request.user.email).exists()

class showSlambookMyDetailView(LoginRequiredMixin,DetailView):
    model = tableThree
    template_name='dashboard/show_slambook_entry.html'
    context_object_name= 'tableThree'
    # def test_func(self):
    #     return senior_users.objects.filter(email=request.user.email).exists()


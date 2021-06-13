import random

from django.shortcuts import render, redirect

import Foods
from Foods.forms import LoginForm, Qform, NewUserForm
from Foods.models import User, Food, SpecialDiet


#317008179875395
#endpoint database-1.c0htqdcgj0ky.ap-southeast-2.rds.amazonaws.com
def home(request):
    note = " Please insert your Username/Password or register if you are a new user"
    if request.method == 'POST':
        userpass = LoginForm(request.POST)
        if userpass.is_valid():
            _username = userpass.cleaned_data['username']
            _password = userpass.cleaned_data['password']
            try:
                instance = User.objects.get(username=_username)
                if instance.password == _password:

                    return redirect(mainpage, s_id= instance.pk)

                else:
                    note = "Wrong Password! Try again."
                    newform = LoginForm()
                    return render(request, 'Foods/home.html', {'userid': newform, 'note':note})
            except User.DoesNotExist:
                instance = None
            newform = LoginForm()
            return render(request, 'Foods/home.html', {'userid': newform, })
    else:
        form = LoginForm()
        return render(request, 'Foods/home.html', {'userid': form, 'note':note})

def mainpage(request, s_id):
    fimage = {}
    query = Qform()
    note = ""
    try:
        qresult=None
        user = User.objects.get(pk=s_id)

        diets = user.diet.all()
        if diets.count()>0:
            availableFoods = Food.objects.filter(diet__in=diets)
        else:
            availableFoods = Food.objects.all()
        foods = availableFoods.order_by('?')[:7]



    except User.DoesNotExist:
        raise home(request)
    if request.method == 'POST':

        query = Qform(request.POST)
        if query.is_valid():
            qresult= []

            criteria2 = query.cleaned_data["diet"] if len(query.cleaned_data["diet"] )!= 0 else " "
            #Food.objects.filter(title__contains= criteria1, fat = None).delete()
            #Food.objects.filter(diet__in=criteria2, title=None).delete()
            #Food.objects.filter(title=None).delete()
            d= SpecialDiet.objects.filter(diet__in=criteria2)
            qresult2 = Food.objects.filter(diet__in= d)

            qresult = qresult2
            foods = qresult.order_by('?')[:7]

            if len(qresult)==0:
                note= "No result found"

    return render(request, 'Foods/mainpage.html', {'user': user, 'query': query, 'qresult': qresult, 'note': note, 'foods': foods, })

def signup(request):
    note = ""
    if request.method == 'POST':
        registered = NewUserForm(request.POST, request.FILES)

        form = LoginForm()
        if registered.is_valid():

            if registered.valid_password():
                registered.save()
                note = " You are registered now!"
            else:
                note = "Your password should be match in both fields"
                registered = NewUserForm()
                print("not match")
                return render(request, 'Foods/registration.html', {'registered': registered, 'note': note,})

        return render(request, 'Foods/home.html', {'userid': form, 'note': note, })
    else:
        registered = NewUserForm()
        return render(request, 'Foods/registration.html', {'registered': registered, })
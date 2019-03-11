from django.shortcuts import render,redirect
from django .http import HttpResponse
from .forms import CreateNewUserForm,NewrecipeForm
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    return render(request,'recipeApp/homepage.html')


def newuser(request):


    if request.method == "POST":
        print(request.method)

        form = CreateNewUserForm(request.POST)

        if form.is_valid():
            form.save()
            User.objects.create_user(request.POST["username"], "", request.POST["password"])
            return redirect("index")

    else:
        form = CreateNewUserForm()
        context = {"form": form}
        return render(request, "recipeApp/newuser.html", context)


    form = CreateNewUserForm(request.POST or None)
    context = {"form": form}
    return render(request, 'recipeApp/newuser.html', context)

def login(request):
    form = CreateNewUserForm(request.POST or None)
    # form = CreateNewUserForm()
    context={

        "form":form
    }
    print(request.POST)
    print(form)
    print(context)
    return render(request,'registration/login.html',context)




def logout(request):
    return render(request,'registration/logged_out.html')

def all_recipes(request):
    form=NewrecipeForm(request.POST or None)
    context={
        "form":form
    }
    return render(request,'recipeApp/addrecipe.html',context)
def profile_page(request):
    return HttpResponse("me")

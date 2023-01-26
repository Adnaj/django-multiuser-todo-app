from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login as loginUser,logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import TodoForm
from .models import Todo

# Create your views here.
@login_required(login_url='login')
def home(request):
    if request.user.is_authenticated:
        user=request.user
        forms=TodoForm()
        todos=Todo.objects.filter(user=user)
        if request.method == 'POST':
            form=TodoForm(request.POST)
            if form.is_valid():
                todo=form.save(commit=False)
                todo.user=user
                todo.save()
                context={'forms':forms,'todos':todos,'user':user}
                return render(request,'index.html',context)
            else:
                context={'forms':forms,'todos':todos,'user':user}
                return render(request,'index.html',context)
            
        context={'forms':forms,'todos':todos,'user':user}
        return render(request,'index.html',context)
    
    


def login(request):
    form=AuthenticationForm()
    context={'forms':form}
    if request.method == 'GET':
        return render(request,'login.html',context)
    else:
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username = username, password = password)
            if user is not None:
                loginUser(request,user)
                return redirect('home')
        else:
            return render(request,'login.html',context)
        

def signup(request):
    form = UserCreationForm()
    context = {'forms':form}
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            if user is not None:
                user.save()
                return redirect('home')
            else:
                return render(request,'signup.html',context)
            
    else:
        return render(request,'signup.html',context)
    
    

    
    
def signout(request):
    logout(request)
    return redirect('login')

def tododelete(request,id):
    Todo.objects.get(pk=id).delete()
    return redirect ('home')

def todoupdate(request,id):
    if request.user.is_authenticated:
        post=Todo.objects.get(pk=id)
        form =TodoForm(instance=post)
        if request.method == 'POST':
            form=TodoForm(request.POST,instance=post)
            user=request.user
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return redirect('home')
    context={'forms':form} 
    return render(request,'index.html',context)  
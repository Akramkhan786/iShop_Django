from django.contrib.auth.models import User
from django.shortcuts import render, redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def signup(request):
    if request.method == 'POST':
        # get the post parameters
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']

        #check for errorneous inputs
        if len(username) > 10:
            messages.error(request,  "Username must be under 10 characters!")
            return redirect('/shop')
        if not username.isalnum():
            messages.error(request, "Username should only contain letters and numbers!")
            return redirect('/shop')
        if password1 != password2:
            messages.error(request, "Passwords do not match!")
            return redirect('/shop')

       #Checks for signup
        myuser = User.objects.create_user(username, email, password1)
        myuser.first_name = first_name
        myuser.last_name = last_name
        myuser.save()
        messages.success(request, "Your iShop account has been created successfully!")
        return redirect('/shop')
    else:
       return render(request, 'accounts/signup.html')

def handlelogin(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        myuser = authenticate(username=username, password=password)
        if myuser is not None:
            login(request, myuser)
            messages.success(request, "You Are Successfully Logged in, Please Continue your shopping!")
            return redirect('/')
        elif messages.error(request, "Invalid Credentials Please Try Again!"):
            return redirect('/')

    return render(request, 'accounts/login.html')

def handlelogout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out!")
    return redirect('/')
    return HttpResponse("handlelogout")



from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,redirect
from django.contrib import messages


from .models import *

# # Create your views here.
# defe interface:(request):
    
#     return render(request,"user_interface.html"),


def User_interface(request):
    
        return render(request,"user_interface.html")


def User_register(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password= request.POST['password']
        confirmpassword = request.POST['confirmpassword']
        if password == confirmpassword:
                if User_signin.objects.filter(email=email).exists():
                        messages.info(request, 'This email already exists. Sign up again')
                        return redirect('User_register')
            
            
                else:
                    user = User_signin.objects.create(username=username,email=email,
                                                password=password)
                    user.save()
                    return redirect("User_signin")
        else:
                messages.info(request, 'Password and confirm password does not match')
                return redirect('User_register')
        
    return render(request,"user_registration.html")
            





def User_signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            username = user.username
            # messages.success(request, "Logged In Sucessfully!!")
            return render(request, "index.html",{"username":username})
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('User_signin')
    
    return render(request, "signin.html")

   


# def userreg(request):
    
#     v=Addnewplatform.objects.all
# c=Course.objects.al


# return render(request,'user_register.html',{'v':v,'c':c})



def User_index(request):
    
        return render(request,"index.html")



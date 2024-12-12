from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User


# Create your views here.

#Login function
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        #verify the user
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid creandials')
            return redirect('login')

    else:
        return render(request, 'login.html')

#Register function
def register(request):
    

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

         #some validations
         #the passwords are machng or not
        if password1 == password2:

            #the user is already exists or not
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username taken')
                return redirect('register')

            #check the email are exists or not
            elif User.objects.filter(email=email).exists():
               messages.info(request,"email taken")
               return redirect('register')

                
            else:
                 #create a object for database
    #left side is a model and right side is a variable
                user = User.objects.create_user(
                first_name = first_name,
                last_name = last_name,
                username = username,
                email = email,
                password = password1
            )

                #save the datas to database
                user.save()
                messages.success(request,'User created successfully')
                return redirect('login')

        else:
           messages.info(request,'password doesnot match')
           return redirect('register')

    
    else:
        return render(request, 'register.html')
    
#logout functionality
def logout(request):
    auth.logout(request)
    return redirect('/')
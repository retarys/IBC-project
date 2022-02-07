from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.contrib import messages


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None and user.is_staff:
            auth.login(request,user)
            return redirect('/')
            
        if user is not None:
            auth.login(request,user)
            return render(request, 'clients_main.html')
        
        else:
            messages.info(request, 'you have not loged in')
            return redirect('login')
    else:
        return render(request, 'login.html')






def logout(request):
    auth.logout(request)
    return render(request, 'login.html')





def register(request):

    if request.method == 'POST':

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                return render(request, 'alert_page.html')
            elif User.objects.filter(email=email).exists():
                return render(request, 'alert_page.html')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                print("THIS SHIT IS ACTUALLY WORKING!!!")

        else:
            return render(request, 'alert_page.html')        
        return redirect('/')

    else:
        return render(request, 'register.html')




def clients_vz(request):
    return render(request, 'clients_vz.html')  

def clients_main(request):
    return render(request, 'clients_main.html')
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from contacts.models import Contact

# Create your views here.
def register(request):
    if request.method == 'POST':
        #    messages.error(request, 'Testing Error Message')     Eğer mesaj error mesajı ise ve kullanıcı submite bastığında(PORT metodu) error gelmişse bunu yazılan error mesajı ile birlikte mesaj error mekanizmasına gönder.
        # Get form values
        first_name = request.POST['first_name'] # html dosyasındaki name attributelerine göre
        last_name = request.POST['last_name'] 
        username = request.POST['username']
        email = request.POST['email'] 
        password = request.POST['password'] 
        password2 = request.POST['password2']

        # Check if passwords match
        if password == password2:
            # Check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken!')
                return redirect('register')
            else:
                # Check email
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is being used!')
                    return redirect('register')
                else:
                    # Looks good
                    user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)

                    #Login after register. Below method is usefull library to log in the user of django.
                    #auth.login(request,user)
                    #messages.success(request, 'You have successfully logged in.')
                    #return redirect('index')

                    # User will be redirected to login page to login after registration. This way will be used on this project
                    user.save()
                    messages.success(request, 'You are now registered and can login')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match') 
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You have successfully logged out')
        return redirect('index')

def dashboard(request):
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)

    context = {
        'contacts': user_contacts
    }

    return render(request, 'accounts/dashboard.html', context)
from django.shortcuts import redirect, render
from userauths.forms import UserRegisterForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.conf import settings

User = settings.AUTH_USER_MODEL

def RegisterView(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            print('successful')
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hey {username}, Your account was created succesfully')
            new_user = authenticate(username = form.cleaned_data['email'], #same with .cleaned_data.get('email')
                                    password = form.cleaned_data['password1'] #password1 == password authenticate field
                                    ) 
            login(request, new_user)
            return redirect('core:index') #return to index.html in core app

    else:
        form = UserRegisterForm()
        print('unsuccessful')

    context = {
        'form': form,
    }

    return render(request, "userauths/sign-up.html", context)

def LogInView(request):
    if request.user.is_authenticated:
        messages.warning(request, f'Hey, you are already logged in')
        return redirect('core:index')
    
    if request.method ==  'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email = email)
        except:
            messages.warning(request,f'User with {email} does not exist')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'You are logged in')
            return redirect('core:index')
        else:
            messages.warning(request, 'User does not exist, create an account')

    context = {}

    return render(request, 'userauths/sign-in.html', context)

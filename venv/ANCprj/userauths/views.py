from django.shortcuts import redirect, render
from userauths.forms import UserRegisterForm
from django.contrib.auth import login, authenticate
from django.contrib import messages


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

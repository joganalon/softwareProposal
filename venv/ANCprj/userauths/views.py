from django.shortcuts import render
from userauths.forms import UserRegisterForm

def RegisterView(request):

    if request.method == 'post':
        form = UserRegisterForm(request.post)
        if form.is_valid():
            form.save()

    else:
        form = UserRegisterForm()

    context = {
        'form': form,
    }

    return render(request, "userauths/sign-up.html", context)

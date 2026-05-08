from django.shortcuts import render, redirect
from django.contrib import messages
from users.forms import RegisterForm


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully")
            return redirect('homepage')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

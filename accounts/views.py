from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm, ContactForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView

def RegisterView(request):

    """ View for registration form """

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('bedrijfsnaam')
            raw_password = form.cleaned_data.get('password')

            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('Index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

class Login(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True
    form = LoginView

class Logout(LogoutView):
    template_name = 'login.html'
    redirect_authenticated_user = True
    form = LoginView

def ContactView(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send_email()
            return redirect('Index')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm
from .shortcuts import get_current_site
from django.template.loader import render_to_string


@login_required
def profile(request):
    return render(request, 'accounts/profile.html', {'section': 'profile'})


def accounts_register(request):
    if request.method == 'POST':
        registerForm = RegistrationForm(request.POST)
        if registerForm.is_valid():
            user = registerForm.save(commit=False)
            user.email = registerForm.cleaned_data['email']
            user.set_password(registerForm.cleaned_data['password'])
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = render_to_string('registration/account_activation_email.html', {


            })

    else:
        registerForm = RegistrationForm()

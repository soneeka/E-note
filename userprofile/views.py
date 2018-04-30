from django.shortcuts import render,redirect
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.models import User
from django.contrib.auth.views import login

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.contrib import messages

from .token import account_activation_token

from .forms import SignUpForm
from .token import account_activation_token
# Create your views here.
def account_activation_sent(request):
    return render(request, 'account_activation_sent.html',)

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)

    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active= True
        user.profile.email_confirmed= True
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'account_activation_invalid.html')


def signup(request):
    template_name = 'signup.html'
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            email = form.cleaned_data.get('email')
            first_name = form.cleaned_data.get('first_name')
            current_site = get_current_site(request)
            subject = 'Activate your Account'
            message = render_to_string('account_activation_email.html', {
            'user': user,
            'domain':current_site.domain,
            'uuid':urlsafe_base64_encode(force_bytes(user.pk)),
            'token':account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            messages.success(request, 'Signup Successfully!')
            messages.warning(request, 'Please check your email to activate your account')
            return redirect('/')

    else:
        form = SignUpForm()

    context = {'form': form}
    return render(request, template_name, context)

from django.views import generic
from django.contrib.auth.models import User
from django.urls import reverse_lazy

from django.contrib.auth.forms import UserCreationForm


class UserRegisterView(generic.CreateView):
    """User registration controller."""
    model = User
    form_class = UserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

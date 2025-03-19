from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from .models import CustomUser


class MyUserCreateView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'registration/registration_form.html'
    success_url = reverse_lazy('pages:homepage')

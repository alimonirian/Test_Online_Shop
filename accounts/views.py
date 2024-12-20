from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# from django.contrib.auth import login, logout
from django.views import generic

from .forms import CustomUserCreationForm


class SignUpViews(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')


# def user_logout(request):
#     # Log out the user
#     logout(request)
#
#     # Redirect to a page after logout, e.g., home page
#     return reverse_lazy('home')  # Replace 'home' with your URL name or path
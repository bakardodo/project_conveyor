from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from project_conveyor.account_user.forms import CreateProfileForm
from project_conveyor.conveyor_app.models import Order
from project_conveyor.conveyor_app.utils import cookieCart


class UserRegisterView(TemplateView):
    template_name = 'conveyor_app/register.html'
    form_class = CreateProfileForm
    success_url = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)


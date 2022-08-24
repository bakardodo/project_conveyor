from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView

from project_conveyor.conveyor_app.forms import CreateAskForm, CreateUCFaskform, PurchaseForm

count = 0
# def create_conveyor_question(request):
#     if request.method == 'POST':
#         form = CreateAskForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('conveyor questions')
#     else:
#         form = CreateAskForm()
#     context = {
#         'form': form,
#     }
#
#     return render(request, 'conveyor_app/dashboard.html', context)
from project_conveyor.conveyor_app.models import AskModel, UCFnumber, UCFLbodies


class CreateHomeView(TemplateView):
    template_name = 'conveyor_app/dashboard.html'

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super().get_context_data(**kwargs)
        list_items = AskModel.objects.filter(user=user)
        items = list_items.count()
        context['all_items'] = items
        return context


class CreateConveyorBeltView(CreateView):
    model = AskModel
    template_name = 'conveyor_app/conveyor_belts.html'
    form_class = CreateAskForm
    success_url = reverse_lazy('conveyor belt')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class CreateBearingBodyView(TemplateView):
    template_name = 'conveyor_app/bearing_bodies.html'

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super().get_context_data(**kwargs)
        list_items = AskModel.objects.filter(user=user)
        items = list_items.count()
        context['all_items'] = items
        return context


class CreateUCFBearingView(CreateView):
    template_name = 'conveyor_app/UCF.html'
    form_class = CreateUCFaskform
    success_url = reverse_lazy('UCF')
    # def get_queryset(self):
    #     user = self.request.user
    #     expense_list = Expense.objects.filter(user=user)  # we give only objects from this user
    #
    #     return expense_list
    success = False

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super().get_context_data(**kwargs)

        # items_belt = AskModel.objects.filter(user=user).count()
        items_bearing_UCF = UCFnumber.objects.filter(user=user).count()
        conveyor = AskModel.objects.all()
        context['all_items'] = items_bearing_UCF
        context['conveyor'] = conveyor
        return context

class CreateUCFLBearingView(CreateView):
    template_name = 'conveyor_app/UCFL.html'
    success_url = reverse_lazy('UCFL')
    form_class = PurchaseForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        items = UCFLbodies.objects.all()

        context['items'] = items
        return context

#
# def create_ucf_bearing(request):
#     if request.method == 'POST':
#         form = CreateUCFaskform(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()



class CreateInsideShoppingCartView(ListView):
    template_name = 'conveyor_app/shopping_cart.html'

    def get_queryset(self):
        user = self.request.user
        ucf = UCFnumber.objects.filter(user=user)  # we give only objects from this user

        return ucf


    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super().get_context_data(**kwargs)
        list_items = AskModel.objects.filter(user=user)
        items = list_items.count()
        context['all_items'] = items
        return context


class CreateBearingBodies(CreateView):
    pass

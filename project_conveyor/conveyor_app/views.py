from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView

from project_conveyor.conveyor_app.forms import CreateAskForm

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
from project_conveyor.conveyor_app.models import AskModel, Product, Order


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

class CreateUCFBearingView(TemplateView):
    template_name = 'conveyor_app/UCF.html'

class CreateUCFLBearingView(TemplateView):
    template_name = 'conveyor_app/UCFL.html'

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super().get_context_data(**kwargs)
        products = Product.objects.all()
        context['products'] = products
        return context

def cart(request, pk):
    if request.user.is_authenticated:
        customer = request.user.pk
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []

    context = {'items':items}
    return render(request, 'conveyor_app/shopping_cart.html', context)



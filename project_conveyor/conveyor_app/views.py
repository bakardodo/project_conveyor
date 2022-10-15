import json

from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import JsonResponse
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView

from project_conveyor.conveyor_app.forms import CreateAskForm, ShippingAddressForm


def get_products(context):
    products = Product.objects.all()
    context['products'] = products
    return context


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
from project_conveyor.conveyor_app.models import AskModel, Product, Order, ShippingAdress, OrderItem


def create_home_view(request):
    customer = request.user.pk
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()

    context = {'items': items, 'order': order}
    return render(request, 'conveyor_app/dashboard.html', context)


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
        context = super().get_context_data(**kwargs)
        products = Product.objects.all()
        context['products'] = products
        return context


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}


    context = {'items': items, 'order': order}
    return render(request, 'conveyor_app/shopping_cart.html', context)


# class CheckoutPage(CreateView):
#     model = ShippingAdress
#     template_name = 'conveyor_app/checkout.html'
#     form_class = ShippingAddressForm
#     success_url = reverse_lazy('home')
#
#     def get_form_kwargs(self):
#         kwargs = super().get_form_kwargs()
#         kwargs['user'] = self.request.user
#         return kwargs
#
#     def get_queryset(self):
#         customer = self.request.user
#         order, created = Order.objects.get_or_create(customer=customer, complete=False)
#         items = order.orderitem_set.all()
#         return items

def checkout(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
    context = {'items': items, 'order': order}
    return render(request, 'conveyor_app/checkout.html', context)
    # form = ShippingAddressForm
    # if request.user.is_authenticated:
    #     customer = request.user.pk
    #     order, created = Order.objects.get_or_create(customer=customer, complete=False)
    #     items = order.orderitem_set.all()
    #     if request.method == 'POST':
    #         form = ShippingAddressForm(request.POST)
    #         if form.is_valid():
    #             form.save()
    #             return redirect('conveyor questions')
    #     else:
    #         form = ShippingAddressForm(request.user)
    # else:
    #     items = []
    #     order = {'get_cart_total': 0, 'get_cart_items': 0}
    #     if request.method == 'POST':
    #         form = ShippingAddressForm(request.POST)
    #         if form.is_valid():
    #             form.save()
    #             return redirect('conveyor questions')
    #     else:
    #         form = ShippingAddressForm(request.user)
    #
    # context = {'items': items, 'order': order, 'form': form}
    # return render(request, 'conveyor_app/checkout.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('productId:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)


import datetime
import json
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import JsonResponse
# Create your views here.
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, CreateView, ListView

from project_conveyor.account_user.forms import CreateProfileForm
from project_conveyor.conveyor_app.forms import CreateAskForm, ShippingAddressForm
from project_conveyor.conveyor_app.utils import cookieCart, cartData
from django.core.mail import send_mail


def get_products(context):  # get all our products of database
    products = Product.objects.all()
    context['products'] = products
    return context


from project_conveyor.conveyor_app.models import AskModel, Product, Order, ShippingAdress, OrderItem, Customer


def create_home_view(request):
    cart_items = None
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cart_items = order.get_cart_items
    else:
        try:
            cart = json.loads(request.COOKIES['cart'])
        except:
            cart = {}
        print('Cart:', cart)
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cart_items = order['get_cart_items']

        for i in cart:
            cart_items += cart[i]["quantity"]
    context = {'items': items, 'order': order, 'cart_items': cart_items}
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        customer = self.request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cart_items = order.get_cart_items
        context['cart_items'] = cart_items
        context['shipping'] = False
        return get_products(context)


def bearing_bodies_view(request):
    cart_items = None
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cart_items = order.get_cart_items
    else:
        try:
            cart = json.loads(request.COOKIES['cart'])
        except:
            cart = {}
        print('Cart:', cart)
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cart_items = order['get_cart_items']

        for i in cart:
            cart_items += cart[i]["quantity"]

    context = {'items': items, 'order': order, 'cart_items': cart_items}
    return render(request, 'conveyor_app/bearing_bodies.html', context)


# class CreateBearingBodyView(TemplateView):
#     template_name = 'conveyor_app/bearing_bodies.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         customer = self.request.user.customer
#         order, created = Order.objects.get_or_create(customer=customer, complete=False)
#         items = order.orderitem_set.all()
#         cart_items = order.get_cart_items
#         context['cart_items'] = cart_items
#         context['shipping'] = False
#         return get_products(context)


def ucf_bearing_view(request):
    cart_items = None
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cart_items = order.get_cart_items
    else:
        try:
            cart = json.loads(request.COOKIES['cart'])
        except:
            cart = {}
        print('Cart:', cart)
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cart_items = order['get_cart_items']

        for i in cart:
            cart_items += cart[i]["quantity"]

    context = {'items': items, 'order': order, 'cart_items': cart_items}
    return render(request, 'conveyor_app/UCF.html', context)


# class CreateUCFBearingView(TemplateView):
#     template_name = 'conveyor_app/UCF.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         customer = self.request.user.customer
#         order, created = Order.objects.get_or_create(customer=customer, complete=False)
#         items = order.orderitem_set.all()
#         cart_items = order.get_cart_items
#         context['cart_items'] = cart_items
#         context['shipping'] = False
#         return get_products(context)


def ucfl_bearing_body(request):
    data = cartData(request)
    cart_items = data['cart_items']

    products = Product.objects.all()
    context = {'cart_items': cart_items, 'products': products}
    return render(request, 'conveyor_app/UCFL.html', context)


def cart(request):
    data = cartData(request)
    cart_items = data['cart_items']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order, 'cart_items': cart_items}
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
        cart_items = order.get_cart_items
    else:
        cookieData = cookieCart(request)
        cart_items = cookieData['cart_items']
        order = cookieData['order']
        items = cookieData['items']

    context = {'items': items, 'order': order, 'cart_items': cart_items}
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


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    all_products = []
    address = data['shipping']['address']
    city = data['shipping']['city']
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)

    else:
        print('User is not logged in..')

        print('COOKIES:', request.COOKIES)
        ordered_products = []
        name = data['form']['name']
        email = data['form']['email']

        cookieData = cookieCart(request)
        items = cookieData['items']

        customer, created = Customer.objects.get_or_create(
            email=email,
        )

        customer.name = name
        customer.save()

        order = Order.objects.create(
            customer=customer,
            complete=False,
        )

        for item in items:
            product = Product.objects.get(id=item['product']['id'])
            product_name = product.name
            all_products.append(product_name)
            orderItem = OrderItem.objects.create(
                product=product,
                order=order,
                quantity=item['quantity']
            )

    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == float(order.get_cart_total):
        order.complete = True
    order.save()

    if order.shipping == True:
        ShippingAdress.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            state=data['shipping']['state'],
            zipcode=data['shipping']['zipcode'],
        )


    result = 'Име на потребителя:'
    result += '\n'
    result += f'-- {customer.name}'
    result += '\n'
    result += '\n'
    result += 'Пожелани продукти от потребителя:'
    result += '\n-- '
    result += str('\n-- '.join(all_products))
    result += '\n'
    result += '\n'
    result += 'Адрес за доставка:'
    result += '\n'
    result += f'-- {str(address)}'
    result += '\n'
    result += '\n'
    result += 'Град:'
    result += '\n'
    result += f'-- {city}'

    send_mail('YANEV Corporation', str(result), 'bakardjievstoqn@gmail.com',
              ['bakardjievstoqn@gmail.com'], fail_silently=False)
    return JsonResponse('Payment complete', safe=False)


class UserRegisterView(CreateView):
    template_name = 'conveyor_app/register.html'
    form_class = CreateProfileForm
    success_url = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)
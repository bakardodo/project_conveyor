from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from project_conveyor.conveyor_app.views import CreateConveyorBeltView, \
    cart, create_home_view, checkout, \
    updateItem, processOrder, bearing_bodies_view, ucf_bearing_view, ucfl_bearing_body, belt_washer, chain_wheel, \
    cylindric_wheel, electric_motor, modul_rail, reducer, roller_chain

urlpatterns = (
    # path('', create_conveyor_question, name='conveyor questions'),
    path('', create_home_view, name='home'),
    path('conveyor/belt/', CreateConveyorBeltView.as_view(), name='conveyor belt'),
    path('shopping/cart/', csrf_exempt(cart), name='shopping cart'),
    path('bearing/body/', bearing_bodies_view, name='bearing body'),
    path('bearing/UCF/', ucf_bearing_view, name='UCF'),
    path('bearing/UCFL/', ucfl_bearing_body, name='UCFL'),
    path('checkout/', csrf_exempt(checkout), name='checkout'),
    path('update-item/', updateItem, name='update-item'),
    path('process_order/', csrf_exempt(processOrder), name='process_order'),
    path('belt_washer/', belt_washer, name='belt washer'),
    path('chain_wheel/', chain_wheel, name='chain wheel'),
    path('electric_motor/', electric_motor, name='electric motor'),
    path('cylindric_wheel/', cylindric_wheel, name='cylindric wheel'),
    path('modul_rail/', modul_rail, name='modul rail'),
    path('reducer/', reducer, name='reducer'),
    path('roller_chain/', roller_chain, name='roller chain'),
    # path('register/', register_page, name='register'),
    # path('login/', login_page, name='login'),

)

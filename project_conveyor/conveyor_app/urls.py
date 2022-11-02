from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from project_conveyor.conveyor_app.views import CreateConveyorBeltView, \
    cart, create_home_view, checkout, \
    updateItem, processOrder, bearing_bodies_view, ucf_bearing_view, ucfl_bearing_body, UserRegisterView

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
    path('create/profile/', UserRegisterView.as_view(), name='profile')

)

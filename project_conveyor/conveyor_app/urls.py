from django.urls import path

from project_conveyor.conveyor_app.views import CreateConveyorBeltView, \
    CreateBearingBodyView, CreateUCFBearingView, CreateUCFLBearingView, cart, create_home_view, checkout, \
    updateItem

urlpatterns = (
    # path('', create_conveyor_question, name='conveyor questions'),
    path('', create_home_view, name='home'),
    path('conveyor/belt/', CreateConveyorBeltView.as_view(), name='conveyor belt'),
    path('shopping/cart/', cart, name='shopping cart'),
    path('bearing/body/', CreateBearingBodyView.as_view(), name='bearing body'),
    path('bearing/UCF/', CreateUCFBearingView.as_view(), name='UCF'),
    path('bearing/UCFL/', CreateUCFLBearingView.as_view(), name='UCFL'),
    path('checkout/', checkout, name='checkout'),
    path('update-item/', updateItem, name='update-item'),

)

from django.urls import path

from project_conveyor.conveyor_app.views import CreateHomeView, CreateConveyorBeltView, CreateInsideShoppingCartView, \
    CreateBearingBodyView, CreateUCFBearingView, CreateUCFLBearingView

urlpatterns = (
    # path('', create_conveyor_question, name='conveyor questions'),
    path('', CreateHomeView.as_view(), name='home'),
    path('conveyor/belt/', CreateConveyorBeltView.as_view(), name='conveyor belt'),
    path('shopping/cart/', CreateInsideShoppingCartView.as_view(), name='shopping cart'),
    path('bearing/body/', CreateBearingBodyView.as_view(), name='bearing body'),
    path('bearing/UCF/', CreateUCFBearingView.as_view(), name='UCF'),
    path('bearing/UCFL/', CreateUCFLBearingView.as_view(), name='UCFL'),
)

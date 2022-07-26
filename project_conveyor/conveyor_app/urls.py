from django.urls import path

from project_conveyor.conveyor_app.views import CreateHomeView, CreateConveyorBeltView, CreateInsideShoppingCartView, \
    CreateBearingBodyView

urlpatterns = (
    # path('', create_conveyor_question, name='conveyor questions'),
    path('', CreateHomeView.as_view(), name='home'),
    path('conveyor/belt/', CreateConveyorBeltView.as_view(), name='conveyor belt'),
    path('shopping/cart/', CreateInsideShoppingCartView.as_view(), name='shopping cart'),
    path('bearing/body/', CreateBearingBodyView.as_view(), name='bearing body'),
    path('conveyor/belt/', CreateConveyorBeltView.as_view(), name='conveyor belt'),
    path('conveyor/belt/', CreateConveyorBeltView.as_view(), name='conveyor belt'),
    path('conveyor/belt/', CreateConveyorBeltView.as_view(), name='conveyor belt'),
)

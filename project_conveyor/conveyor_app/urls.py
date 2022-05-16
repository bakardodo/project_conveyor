from django.urls import path

from project_conveyor.conveyor_app.views import CreateHomeView, CreateConveyorBeltView

urlpatterns = (
    # path('', create_conveyor_question, name='conveyor questions'),
    path('', CreateHomeView.as_view(), name='home'),
    path('conveyor/belt/', CreateConveyorBeltView.as_view(), name='conveyor belt'),

)
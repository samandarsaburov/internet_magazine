from django.urls import path
from .views import (GetAll , Create, Update,Delete)

urlpatterns = [
    path('get/',GetAll.as_view(),name='get'),
    path('create/',Create.as_view(),name="create"),
    path('update/<int:pk>',Update.as_view(),name="update"),
    path('delete/<int:pk>',Delete.as_view(),name="delete"),
]

from django.urls import path
from .views import (Get_all, Create,Delete, Update)

urlpatterns = [
    path('get/',Get_all.as_view(),name='get'),
    path('create/',Create.as_view(),name='create'),
    path('delete/<int:pk>', Delete.as_view(),name='del'),
    path('update/<int:pk>',Update.as_view(),name='update'),
]

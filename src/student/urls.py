from django.urls import path
from .views import student_create,details


urlpatterns = [
    path('create/',student_create),
    path('details/',details),
    ]
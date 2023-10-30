from django.urls import path
from . import views

urlpatterns = [
    path('', views.allclasses, name='allclasses'),
    path('<int:class_id>/', views.detail, name="class_detail"),
]

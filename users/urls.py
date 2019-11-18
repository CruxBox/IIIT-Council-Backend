from django.urls import path
from users import views

urlpatterns = [
    path('director/add', views.CreateDirectorView.as_view())
]
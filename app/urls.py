from .views import FileView
from django.urls import path

app_name = "app"

urlpatterns = [

    path('', FileView.as_view(), name="home")
]

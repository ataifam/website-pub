from django.urls import path
from django.contrib import admin
from . import views

app_name = "main"
urlpatterns = [
path("", views.home, name="home"),
path('admin/', admin.site.urls),
path("resume/", views.resume, name="resume"),
path("projects/", views.projects, name="projects"),
path("contact/", views.contact, name="contact"),
]
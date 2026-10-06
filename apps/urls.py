
from django import views
from django.urls import path
from . import views
urlpatterns = [
    path('', views.StartingPageView.as_view(), name="starting_page"),
    path('about/', views.AboutView.as_view(), name="about_data"),
    path('contact/', views.ContactView.as_view(), name="contact"),
    path("resume/", views.ResumeView.as_view(), name="resume"),
    path("project/", views.ProjectView.as_view(), name="project"),
]


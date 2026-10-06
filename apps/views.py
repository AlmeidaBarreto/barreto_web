from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import ListView, TemplateView
from django.db.models import Prefetch

from .models import (
    ProjectWeb,
    StartingPage,
    About,
    ContactInfo,
    ContactMessage,
    ResumeSummary,
    Education,
    Experience,
    TechnicalSkill, ExperienceResponsibility, MainTechnicalSkill, Project, NonFormalEducationCourse, NonFormalEducation,ProjectService
)

# Create your views here.

class StartingPageView(ListView):
    model = StartingPage
    template_name = "apps/index.html"
    context_object_name = "starting_page"

class AboutView(ListView):
    template_name = "apps/about.html"
    context_object_name = "about_data"

    def get_queryset(self):
        return About.objects.all()


class ContactView(TemplateView):
    template_name = "apps/contact.html"

    # GET request
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["contact_info"] = ContactInfo.objects.first()

        return context

    # POST request
    def post(self, request, *args, **kwargs):

        ContactMessage.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            subject=request.POST.get("subject"),
            message=request.POST.get("message"),
        )

    
        messages.success(
            request,
            "Your message has been sent successfully!"
        )

        return redirect("contact")




class ResumeView(TemplateView):
    template_name = "apps/resume.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Only one summary
        context["summary"] = ResumeSummary.objects.first()

        # Multiple education records
        context["education_data"] = Education.objects.all()

        # Multiple work experience records
        context["experience_data"] = Experience.objects.all() 

        context["experience_responsibilities"] = ExperienceResponsibility.objects.all() #Concept in SQL = SELECT * FROM experience_responsibility;

        context["technical_skill_data"] = TechnicalSkill.objects.all()

        
        context["main_technical_skill_data"] = MainTechnicalSkill.objects.all()

           # Non-Formal Education Title
        context["non_formal_education_data"] = (
            NonFormalEducationCourse.objects.prefetch_related(
                Prefetch(
                    "education_data",
                    queryset=NonFormalEducation.objects.order_by("-start_year")
                )
            )
        )

        

        return context

# class ProjectView(ListView):
#     template_name = "apps/project.html"
#     context_object_name = "project_data"

#     def get_queryset(self):
#         return Project.objects.all()  
# 
# 

# class ProjectView(ListView):

#     model = Project

#     template_name = "apps/project.html"

#     context_object_name = "project_data"

#     def get_context_data(self, **kwargs):

#         context = super().get_context_data(**kwargs)

#         context["project_categories"] = Project.objects.all()

#         return context 
    
class ProjectView(TemplateView):
    template_name = "apps/project.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["project_web_data"] = ProjectWeb.objects.all()
        context["project_service_data"] = ProjectService.objects.all()

        return context  

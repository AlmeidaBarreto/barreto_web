from django.contrib import admin
from .models import StartingPage, About, ContactInfo, ContactMessage, ResumeSummary, Education, Experience,ExperienceResponsibility, MainTechnicalSkill, TechnicalSkill, Project, NonFormalEducation, NonFormalEducationCourse, ProjectService,ProjectWeb

# Register your models here.
class StartingPageAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'content','caption')
admin.site.register(StartingPage, StartingPageAdmin)

class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'description', 'birthday', 'website', 'phone', 'city', 'age', 'degree', 'email', 'freelance', 'bottom_description')
admin.site.register(About, AboutAdmin)


class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('address', 'phone', 'email')
admin.site.register(ContactInfo, ContactInfoAdmin)

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message', 'created_at')
admin.site.register(ContactMessage, ContactMessageAdmin)


class ResumeSummaryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'address', 'phone', 'email')
admin.site.register(ResumeSummary, ResumeSummaryAdmin)

class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'start_year', 'end_year', 'description')
admin.site.register(Education, EducationAdmin)

class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('position', 'company', 'start_date', 'end_date')
admin.site.register(Experience, ExperienceAdmin)

class ExperienceResponsibilityAdmin(admin.ModelAdmin):
    list_display = ('experience', 'description')
admin.site.register(ExperienceResponsibility, ExperienceResponsibilityAdmin)

class TechnicalSkillAdmin(admin.ModelAdmin):
    list_display = ('title',)
admin.site.register(TechnicalSkill,TechnicalSkillAdmin)

class MainTechnicalSkillAdmin(admin.ModelAdmin):
    list_display = ("technical_skill", "description")
admin.site.register(MainTechnicalSkill, MainTechnicalSkillAdmin)

class NonFormalEducationCourseAdmin(admin.ModelAdmin):
    list_display = ("course_name",)
admin.site.register(NonFormalEducationCourse,NonFormalEducationCourseAdmin)

class NonFormalEducationAdmin(admin.ModelAdmin):
    list_display = ("course","start_year","end_year","institution",
                    "location",)
admin.site.register(NonFormalEducation, NonFormalEducationAdmin)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title","category","description")
admin.site.register(Project,ProjectAdmin)

class ProjectServiceAdmin(admin.ModelAdmin):
    list_display = ("title","description","image")
admin.site.register(ProjectService,ProjectServiceAdmin)

class ProjectWebAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "year",
        "featured",
        "description",
        "technologies", 
    )

    list_filter = (
        "year",
        "featured",
    )

    search_fields = (
        "title",
        "description",
        "technologies",
    )
admin.site.register(ProjectWeb, ProjectWebAdmin)

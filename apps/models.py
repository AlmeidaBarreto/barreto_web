from django.db import models


class StartingPage(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="uploads/")
    content = models.TextField()
    caption = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class About(models.Model):
    image = models.ImageField(upload_to="about/")
    title = models.CharField(max_length=200)
    subtitle = models.TextField()
    description = models.TextField()

    birthday = models.CharField(max_length=50, blank=True)
    website = models.URLField(blank=True)
    phone = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=100, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    degree = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    freelance = models.CharField(max_length=100, blank=True)

    bottom_description = models.TextField()

    def __str__(self):
        return self.title


class ContactInfo(models.Model):
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.email


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject


# Resume Summary
class ResumeSummary(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=150)
    description = models.TextField()
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.name


# Education
class Education(models.Model):
    degree = models.CharField(max_length=200)
    start_year = models.CharField(max_length=20)
    end_year = models.CharField(max_length=20)
    institution = models.CharField(max_length=255)
    location = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.degree


# Main Technical Skill Category
class TechnicalSkill(models.Model):
    icon = models.CharField(
        max_length=100,
        blank=True,
        help_text="Example: bi-broadcast"
    )

    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


# Technical Skill Description
# class MainTechnicalSkill(models.Model):
#     technical_skill = models.ForeignKey(
#         TechnicalSkill,
#         on_delete=models.CASCADE,
#         related_name="skill_data"
#     )

#     description = models.TextField()

#     def __str__(self):
#         return self.description[:50]

class MainTechnicalSkill(models.Model):
    technical_skill = models.ForeignKey(
        TechnicalSkill,
        on_delete=models.CASCADE,
        related_name="skill_data"
    )

    description = models.TextField()


# Professional Experience
class Experience(models.Model):
    position = models.CharField(max_length=200)
    start_date = models.CharField(max_length=50)
    end_date = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    company = models.CharField(max_length=255)
    location = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.position} - {self.company}"


# Experience Responsibilities
class ExperienceResponsibility(models.Model):
    experience = models.ForeignKey(
        Experience,
        on_delete=models.CASCADE,
        related_name="responsibilities"
    )

    description = models.TextField()

    def __str__(self):
        return self.description[:50]

    
class NonFormalEducationCourse(models.Model):
    course_name = models.CharField(max_length=200)

    def __str__(self):
        return self.course_name


class NonFormalEducation(models.Model):
    course = models.ForeignKey(
        NonFormalEducationCourse,
        on_delete=models.CASCADE,
        related_name="education_data"
    )

    start_year = models.IntegerField()

    end_year = models.IntegerField(null=True, blank=True)

    institution = models.CharField(max_length=255)

    location = models.CharField(
        max_length=150,
        blank=True
    )
    # class Meta:
    #     ordering = ["start_year"]

    def __str__(self):
        return f"{self.course} - {self.institution}"
    





class Project(models.Model):
    CATEGORY_CHOICES = [
        ("web", "Web Development"),
        ("network", "Network & IT"),
        ("django", "Django"),
        ("python", "Python"),
        ("other", "Other"),
    ]

    title = models.CharField(max_length=200)

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default="other"
    )

    image = models.ImageField(
        upload_to="projects/"
    )

    description = models.TextField()

    project_url = models.URLField(
        blank=True,
        null=True
    )

    github_url = models.URLField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title

    
class ProjectWeb(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="projects/web/")
    year = models.PositiveIntegerField()
    technologies = models.CharField(max_length=500, blank=True)
    case_study_url = models.URLField(blank=True)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class ProjectService(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="projects/services/")
    icon = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title
from autoslug import AutoSlugField
from colorfield.fields import ColorField
from django.core.exceptions import ValidationError
from django.core.validators import (FileExtensionValidator, MaxLengthValidator,
                                    RegexValidator)
from django.db import models
from django.utils import timezone
from PIL import Image

# Create your models here.

class Application(models.Model):
    name = models.CharField(max_length=50, validators=[
        RegexValidator(
            regex=r'^[A-Za-z\s]{3,}$',
            message='Name must contain at least 3 letters.',
            code='invalid_name'
        ),
    ])
    email = models.EmailField()
    course = models.CharField(max_length=100)
    contact = models.CharField(max_length=10, validators=[
        RegexValidator(
            regex=r'^\d{10}$',
            message='Contact must be a 10-digit number.',
            code='invalid_contact'
        ),
    ])
    created_at=models.DateTimeField(default=timezone.now)

class Nav_Contact(models.Model):
    email = models.EmailField()
    contact_number = models.CharField(max_length=10, validators=[
        RegexValidator(
            regex=r'^\d{10}$',
            message='Contact must be a 10-digit number.',
            code='invalid_contact'
        ),
    ])
    image_url = models.ImageField(
        upload_to='logo_images/',default=" ",
        validators=[
            FileExtensionValidator(allowed_extensions=['png']),
        ]
    )

    def __str__(self):
        return self.email

class Home_HomeSlider(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    button_text = models.CharField(max_length=50)
    button_link = models.URLField(default="")
    background_image = models.ImageField(
        upload_to='slider_images/',
        validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']),
        ]
    )

    def __str__(self):
        return self.title

class Home_Service(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    icon_class = models.CharField(max_length=50)
    bg_color = ColorField()

    def __str__(self):
        return self.title

class Home_key_Image(models.Model):
    background_image = models.ImageField(
        upload_to='background_images/',
        validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']),
        ]
    )

class Home_KeyPoint(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

class Home_KeyService(models.Model):
    subtitle = models.CharField(max_length=255)
    subcontent = models.TextField()
    icon_class = models.CharField(max_length=50, validators=[MaxLengthValidator(limit_value=50)])

def clean(self):
    if not self.icon_class.startswith('flaticon-'):
        raise ValidationError("Icon class must start with 'flaticon-'.")
    if self.background_image:
        max_size = 5 * 1024 * 1024
        if self.background_image.size > max_size:
            raise ValidationError("Image size must be less than 5 MB.")

class Home_AboutSection(models.Model):
    background_image = models.ImageField(upload_to='about_section/')
    about_image = models.ImageField(upload_to='about_section/')
    video_url = models.URLField(default=" ")
    title = models.CharField(max_length=255)
    description = models.TextField()
    trainer_count=models.IntegerField(help_text="Enter the number of Trainers",default=1)
    students_count=models.IntegerField(help_text="Enter the number of Students",default=1)
    course_count=models.IntegerField(help_text="Enter the number of Courses offered",default=1)
    seminar_count=models.IntegerField(help_text="Enter the number of Seminar Conduct",default=1)

    def __str__(self):
        return self.title

class Home_Course(models.Model):
    subtitle=models.CharField(max_length=255)
    instructor = models.CharField(max_length=255)
    duration = models.CharField(max_length=20)
    image = models.ImageField(upload_to='course_images/')
    description = models.TextField()
    instructor_icon_class = models.CharField(max_length=50, default='fas fa-user')
    duration_icon_class = models.CharField(max_length=50, default='fas fa-calendar-alt')

class Home_Coursetitle(models.Model):
    title = models.CharField(max_length=255)

class Home_Quote(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    background_image1 = models.ImageField(upload_to='quote_request_images/',default="")

class Home_QuoteRequest(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    course_selection = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

class Home_BlogPost(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='blog_images/')
    content = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    author = models.CharField(max_length=100)
    slug=AutoSlugField(unique=True,null=True,blank=True,populate_from='title')

class Home_BlogSection(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

class Home_Testimonial(models.Model):
    user_img = models.ImageField(upload_to='testimonial_images/')
    quote = models.TextField()
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)

class Home_TestimonialSection(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

class Home_GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery_images/')
    icon_class = models.CharField(max_length=50, default='')

    def __str__(self):
        return f"{self.image.url} - {self.icon_class}"

class Footer_Address(models.Model):
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.address

class About_AboutUs(models.Model):
    title = models.CharField(max_length=255)
    subtitle1 = models.CharField(max_length=255,default='')
    subtitle2 = models.CharField(max_length=255,default='')
    url = models.CharField(max_length=255,default='')
    icon_class = models.CharField(max_length=50, default='')
    background_image = models.ImageField(upload_to='about_images/')

    def __str__(self):
        return self.title

class About_About(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='about_images/')
    content = models.TextField()

    def __str__(self):
        return self.title
    
class About_AboutSection(models.Model):
    background_image = models.ImageField(upload_to='about_section/')
    about_image = models.ImageField(upload_to='about_section/')
    video_url = models.URLField(default=" ")
    title = models.CharField(max_length=255)
    description = models.TextField()
    trainer_count=models.IntegerField(help_text="Enter the number of Trainers",default=1)
    students_count=models.IntegerField(help_text="Enter the number of Students",default=1)
    course_count=models.IntegerField(help_text="Enter the number of Courses offered",default=1)
    seminar_count=models.IntegerField(help_text="Enter the number of Seminar Conduct",default=1)

    def __str__(self):
        return self.title

class About_TimelineEvent(models.Model):
    date = models.CharField(max_length=10)
    title = models.CharField(max_length=255)
    description = models.TextField()

class About_Timeline_Heading(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

class About_MissionVision(models.Model):
    title1 = models.CharField(max_length=255)
    icon_class1 = models.CharField(max_length=50)
    content1 = models.TextField()
    title2 = models.CharField(max_length=255,default="")
    icon_class2 = models.CharField(max_length=50,default="")
    content2 = models.TextField(default="")
    background_image1 = models.ImageField(upload_to='mission_vision_images/')
    background_image2 = models.ImageField(upload_to='mission_vision_images/',default="")

    def __str__(self):
        return self.title1

class About_DedicatedTeam(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    image = models.ImageField(upload_to='team_images/')
    facebook_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)

class About_DedicatedTeamTitle(models.Model):
    title=models.CharField(max_length=225)

class About_Testimonials(models.Model):
    user_img = models.ImageField(upload_to='testimonial_images/')
    quote = models.TextField()
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)

class About_TestimonialsSection(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

class CourseDetail_Course(models.Model):
    image = models.ImageField(upload_to='course_detail_images/',default="")
    title = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    description = models.TextField()

class Staff_CertifiedTrainer(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    image = models.ImageField(upload_to='certified_trainers/')
    description = models.TextField()

class Staff_CertifiedTrainerSection(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

class Contact_ContactForm(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

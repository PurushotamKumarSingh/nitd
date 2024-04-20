# Create your views here.
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from blogapp.models import *

from .forms import *
from .models import *


@require_POST
@csrf_exempt
def submit_application(request):
   if request.method == "POST":
      form = ApplicationForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect('index')
   else:
      form = ApplicationForm()

   return JsonResponse({'success': True,'form':form})

def home(request):
   try:
      contacts=Nav_Contact.objects.all()
   except Nav_Contact.DoesNotExist:
      contacts= None
   try:
      home_sliders = Home_HomeSlider.objects.all()
   except Home_HomeSlider.DoesNotExist:
      home_sliders= None
   try:
      services = Home_Service.objects.all()
   except Home_Service.DoesNotExist:
      services= None
   try:
      key_points = Home_KeyPoint.objects.all()
   except  Home_KeyPoint.DoesNotExist:
      key_points= None
   try:
      keyservices = Home_KeyService.objects.all()
   except Home_KeyService.DoesNotExist:
      keyservices= None
   try:
      image = Home_key_Image.objects.all()
   except Home_key_Image.DoesNotExist:
      image= None
   try:
      about_section = Home_AboutSection.objects.all()
   except Home_AboutSection.DoesNotExist:
      about_section= None
   try:
      courses = Home_Course.objects.all()
   except Home_Course.DoesNotExist:
      courses= None
   try:
      coursetitles=Home_Coursetitle.objects.all()
   except Home_Coursetitle.DoesNotExist:
      coursetitles= None
   try:
      quote = Home_Quote.objects.all()
   except Home_Quote.DoesNotExist:
      quote= None
   try:
      blog_posts = Home_BlogPost.objects.all()
   except Home_BlogPost.DoesNotExist:
      blog_posts= None
   try:
      blog_section = Home_BlogSection.objects.first()
   except Home_BlogSection.DoesNotExist:
      blog_section= None
   try:
      testimonials = Home_Testimonial.objects.all()
   except Home_Testimonial.DoesNotExist:
      testimonials= None
   try:
      testimonial_section = Home_TestimonialSection.objects.first()
   except Home_TestimonialSection.DoesNotExist:
      testimonial_section= None
   try:
      images = Home_GalleryImage.objects.all()
   except Home_GalleryImage.DoesNotExist:
      images= None
   try:
      if request.method == "POST":
         form = QuoteRequestForm(request.POST)
         if form.is_valid():
            form.save()
            return redirect('index')
      else:
         form = QuoteRequestForm()
   except Home_QuoteRequest.DoesNotExist:
      images= None
   try:
      footer_contact = Footer_Address.objects.first()
   except Footer_Address.DoesNotExist:
      footer_contact= None

   return render(request, 'index.html',{'home_sliders': home_sliders, 'services': services, 'key_points': key_points, 'keyservices': keyservices, 'image': image
   ,'about_section': about_section,'courses': courses, 'coursetitles':coursetitles,'blog_posts': blog_posts,
   'blog_section': blog_section,'testimonials': testimonials,'testimonial_section': testimonial_section, 'images': images,'contacts': contacts,
   'footer_contact': footer_contact,'quote': quote,'form':form})

def about(request):
   try:
      contacts = Nav_Contact.objects.all()
   except Nav_Contact.DoesNotExist:
      contacts= None
   try:
      testimonials = About_Testimonials.objects.all()
   except  About_Testimonials.DoesNotExist:
      testimonials= None
   try:
      testimonials_section = About_TestimonialsSection.objects.first()
   except About_TestimonialsSection.DoesNotExist:
      testimonials_section= None
   try:
      about_section = About_AboutSection.objects.all()
   except About_AboutSection.DoesNotExist:
      about_section= None
   try:
      about_content = About_AboutUs.objects.all()
   except About_AboutUs.DoesNotExist:
      about_content= None
   try:
      abouts_content = About_About.objects.first()
   except About_About.DoesNotExist:
      abouts_content= None
   try:
      entries = About_MissionVision.objects.all()
   except About_MissionVision.DoesNotExist:
      entries= None
   try:
      events = About_TimelineEvent.objects.all()
   except About_TimelineEvent.DoesNotExist:
      events= None
   try:
      heading = About_Timeline_Heading.objects.all()
   except About_Timeline_Heading.DoesNotExist:
      heading= None
   try:
      team_members = About_DedicatedTeam.objects.all()
   except About_DedicatedTeam.DoesNotExist:
      team_members= None
   try:
      title = About_DedicatedTeamTitle.objects.all()
   except About_DedicatedTeamTitle.DoesNotExist:
      title= None
   try:
      footer_contact = Footer_Address.objects.first()
   except Footer_Address.DoesNotExist:
      footer_contact= None

   return render(request, 'about.html', {'contacts': contacts,'footer_contact': footer_contact,'testimonials': testimonials,'testimonials_section': testimonials_section,
                  'about_content': about_content,'abouts_content': abouts_content,'entries': entries,'events': events,'heading':heading,'team_members': team_members,
                  'title':title,'about_section': about_section})

def course(request):
   try:
      contacts = Nav_Contact.objects.all()
   except Nav_Contact.DoesNotExist:
      contacts= None
   try:
      courses = Home_Course.objects.all()
   except Home_Course.DoesNotExist:
      courses= None
   try:
      coursetitles=Home_Coursetitle.objects.all()
   except Home_Coursetitle.DoesNotExist:
      coursetitles= None
   try:
      footer_contact = Footer_Address.objects.first()
   except Footer_Address.DoesNotExist:
      footer_contact= None

   return render(request, 'course.html', {'contacts': contacts,'footer_contact': footer_contact,'courses': courses, 'coursetitles':coursetitles})

def course_detail(request):
   try:
      contacts = Nav_Contact.objects.all()
   except Nav_Contact.DoesNotExist:
      contacts= None
   try:
      courses = CourseDetail_Course.objects.all()
   except  CourseDetail_Course.DoesNotExist:
      courses= None
   try:
      footer_contact = Footer_Address.objects.first()
   except Footer_Address.DoesNotExist:
      footer_contact= None
   
   return render(request, 'course-detail.html',{'contacts': contacts,'footer_contact': footer_contact,'courses': courses })

def staff(request):
   try:
      contacts = Nav_Contact.objects.all()
   except Nav_Contact.DoesNotExist:
      contacts= None
   try:
      trainers = Staff_CertifiedTrainer.objects.all()
   except Staff_CertifiedTrainer.DoesNotExist:
      trainers= None
   try:
      staff_sections = Staff_CertifiedTrainerSection.objects.first()
   except Staff_CertifiedTrainerSection.DoesNotExist:
      staff_sections= None
   try:
      footer_contact = Footer_Address.objects.first()
   except Footer_Address.DoesNotExist:
      footer_contact= None

   return render(request, 'staff.html', {'contacts': contacts, 'footer_contact': footer_contact,'trainers': trainers,'staff_sections':staff_sections})

def blog(request):
   # blog = Home_BlogPost.objects.get(slug=slug)
   # data={
   #    'blog':blog
   # }
   try:
      contacts = Nav_Contact.objects.all()
   except Nav_Contact.DoesNotExist:
      contacts= None
   try:
      blog_posts = Home_BlogPost.objects.all()
   except Home_BlogPost.DoesNotExist:
      blog_posts= None
   try:
      blog_section = Home_BlogSection.objects.first()
   except Home_BlogSection.DoesNotExist:
      blog_section= None
   try:
      footer_contact = Footer_Address.objects.first()
   except Footer_Address.DoesNotExist:
      footer_contact= None

   return render(request, 'blog.html', {'contacts': contacts,'footer_contact': footer_contact,'blog_posts': blog_posts,
   'blog_section': blog_section})

def contact(request):
   try:
      contacts = Nav_Contact.objects.all()
   except Nav_Contact.DoesNotExist:
      contacts= None
   try:
      footer_contact = Footer_Address.objects.first()
   except Footer_Address.DoesNotExist:
      footer_contact= None

   return render(request, 'contact.html', {'contacts': contacts,'footer_contact': footer_contact})

def save_contact(request):
   if request.method == "POST":
      form = ContactForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect('contact')
   else:
      form = ContactForm()

   return render(request, 'contact.html', {'form': form})

def blog_data(request, slug):
   blog_data = Home_BlogPost.objects.get(slug=slug)
   try:
      contacts = Nav_Contact.objects.all()
   except Nav_Contact.DoesNotExist:
      contacts= None
   try:
      footer_contact = Footer_Address.objects.first()
   except Footer_Address.DoesNotExist:
      footer_contact= None
   try:
      blog_posts = BlogPost.objects.all()
   except BlogPost.DoesNotExist:
      blog_posts= None
   try:
      testimonials = Testimonial.objects.all()
   except Testimonial.DoesNotExist:
      testimonials= None
   
   return render(request, 'blogs.html', {'blog_data ':blog_data,'contacts': contacts,'footer_contact': footer_contact,'blog_posts': blog_posts, 'testimonials': testimonials })

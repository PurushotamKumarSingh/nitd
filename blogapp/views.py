from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from mainapp.models import *

from .forms import *
# Create your views here.
from .models import *


def blogs(request):
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

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs')
    else:
        form = CommentForm()
    
    return render( request ,'blogs.html',{'contacts': contacts,'footer_contact': footer_contact,'blog_posts': blog_posts, 'testimonials': testimonials
                                        ,'form': form})


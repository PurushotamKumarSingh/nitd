from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):

    Nav1Obj = Nav1.objects.all()
    SliderObj = HomePage_Slider.objects.all()
    HeadCard1Obj = HomePage_HeadCard1.objects.all()
    HeadCard2Obj = HomePage_HeadCard2.objects.all()
    HeadCard3Obj = HomePage_HeadCard3.objects.all()
    HeadCard4Obj = HomePage_HeadCard4.objects.all()
    KeyPointsObj = HomePage_KeyPoints.objects.all()
    AboutNITDObj = HomePage_AboutNITD.objects.all()
    CourseHomeObj = HomePage_CourseHome.objects.all()
    RequestQuoteObj = HomePage_RequestQuote.objects.all()
    ReviewObj = HomePage_Review.objects.all()
    GalleryObj = HomePage_Gallery.objects.all()

    context = { 'Nav1Obj' : Nav1Obj,
                'SliderObj' : SliderObj,
                'HeadCard1Obj' : HeadCard1Obj,
                'HeadCard2Obj' : HeadCard2Obj,
                'HeadCard3Obj' : HeadCard3Obj,
                'HeadCard4Obj' : HeadCard4Obj,
                'KeyPointsObj' : KeyPointsObj,
                'AboutNITDObj' : AboutNITDObj,
                'CourseHomeObj' : CourseHomeObj,
                'RequestQuoteObj' : RequestQuoteObj,
                'ReviewObj' : ReviewObj,
                'GalleryObj' : GalleryObj,
              }

    return render(request, 'index.html',context)

def about(request):

    Nav1Obj = Nav1.objects.all()
    HeadObj = AboutPage_Head.objects.all()
    StablishObj = AboutPage_Stablish.objects.all()
    MissionVisionObj = AboutPage_MissionVision.objects.all()
    # WhyUsObj = AboutPage_WhyUs.objects.all()
    dedicated_teamObj = AboutPage_dedicated_team.objects.all()

    context = { 'Nav1Obj' : Nav1Obj,
                'HeadObj' : HeadObj,
               'StablishObj' : StablishObj,
               'MissionVisionObj' : MissionVisionObj,
               'dedicated_teamObj' : dedicated_teamObj,
            #    'WhyUsObj' : WhyUsObj,
               }

    return render(request, 'about.html',context)

def course(request):

    Nav1Obj = Nav1.objects.all()
    CourseHomeObj = HomePage_CourseHome.objects.all()

    context = { 'Nav1Obj' : Nav1Obj,
               'CourseHomeObj' : CourseHomeObj,
    }

    return render(request, 'course.html',context)

def faculty(request):
    
    Nav1Obj = Nav1.objects.all()
    dedicated_teamObj = AboutPage_dedicated_team.objects.all()

    context = { 'Nav1Obj' : Nav1Obj,
               'dedicated_teamObj' : dedicated_teamObj,
    }

    return render(request, 'faculty.html',context)


def contact(request):
    
    Nav1Obj = Nav1.objects.all()

    context = { 'Nav1Obj' : Nav1Obj,
    }

    return render(request, 'contact.html',context)

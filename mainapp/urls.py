from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from mainapp import views

urlpatterns = [
    path('', views.home, name='index'),
    path('about',views.about,name='about'),
    path('course',views.course,name='course'),
    path('course-detail',views.course_detail,name='course-detail'),
    path('staff',views.staff,name='staff'),
    path('blog',views.blog,name='blog'),
    path('blog_data/<slug>',views.blog_data,name='blog_data'),
    path('contact',views.contact,name='contact'),
    path('saveContact/', views.save_contact, name='save_contact'),
    path('submit_application/', views.submit_application, name='submit_application'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
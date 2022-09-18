from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='index'),
    path('blog', views.blog,name='blog'),
    path('package', views.package,name='package'),
    path('testimonial', views.testimonial,name='testimonial'),
    path('login', views.loginpage,name='login'),
    path('signup', views.signup,name='signup'),
    path('about', views.about,name='about'),
    path('booking', views.about,name='booking'),
    path('navbar', views.navbar,name='navbar')
]
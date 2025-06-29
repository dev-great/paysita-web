"""
URL configuration for Masco project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from Masco import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.index),
    path('about', views.about),
    path('contact', views.contact),
    path('faq', views.faq),
    path('portfolio', views.portfolio),
    path('blog', include('blog.urls')),
    path('privacypolicy', views.privacypolicy),
    path('termscondition', views.termscondition),
    path('ckeditor/', include('ckeditor_uploader.urls')),   # Add this line
]

# serve media files in development
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""
URL configuration for AIwave project.

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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from AIwave import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Main Pages
    path('', views.index, name='home'),
    path('index.html', views.index, name='index'),
    path('roadmap/', views.roadmap, name='roadmap'),
    path('utilize/', views.utilize, name='utilize'),
    path('privacy-policy/', views.privacyPolicy, name='privacy-policy'),

    # Pages (inside /pages/)
    path('pages/style-guide/', views.styleGuide, name='style-guide'),
    path('pages/blog/', views.blog, name='blog'),
    path('pages/blog-details/', views.blogDetails, name='blog-details'),
    path('pages/pricing/', views.pricing, name='pages-pricing'),
    path('pages/contact/', views.contact, name='pages-contact'),
    path('pages/signin/', views.signin, name='signin'),
    path('pages/signup/', views.signup, name='signup'),
    path('pages/team/', views.team, name='team'),
    path('pages/terms-policy/', views.termsPolicy, name='terms-policy'),
    path('pages/privacy-policy/', views.privacyPolicy, name='pages-privacy-policy'),
    path('pages/profile-details/', views.profileDetails, name='profile-details'),
    path('pages/notification/', views.notification, name='notification'),
    path('pages/chat-export/', views.chatExport, name='chat-export'),
    path('pages/appearance/', views.appearance, name='appearance'),
    path('pages/plans-billing/', views.plansBilling, name='plans-billing'),
    path('pages/sessions/', views.sessions, name='sessions'),
    path('pages/application/', views.application, name='application'),
    path('pages/release-notes/', views.releaseNotes, name='release-notes'),
    path('pages/help/', views.help, name='help'),

    # Tools
    path('tools/text-generator/', views.textGenerator, name='text-generator'),
    path('tools/image-generator/', views.imageGenerator, name='image-generator'),
    path('tools/code-generator/', views.codeGenerator, name='code-generator'),
    path('tools/image-editor/', views.imageEditor, name='image-editor'),
    path('tools/video-generator/', views.videoGenerator, name='video-generator'),
    path('tools/email-generator/', views.emailGenerator, name='email-generator'),
]

# Serve static files in development
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])

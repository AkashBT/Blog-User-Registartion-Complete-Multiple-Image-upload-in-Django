"""filestoragesystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from blog import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('signup/',views.signup,name="signup"),
    path('signin/',views.signin,name="signin"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('logout/',views.user_logout,name="logout"),
    path('profile/',views.profile,name="profile"),
    path('changepass/',views.changepass,name="changepass"),
    path('userdetail/<int:id>/',views.userdetail,name="userdetail"),


    path('addblog/',views.addblog,name="addblog"),
    path('updateblog/<int:id>',views.updateblog,name="updateblog"),
    path('deleteblog/<int:pk>',views.deleteblog,name="deleteblog"),
    path('myblogs/',views.myblogs,name='myblogs'),
    path('view/<int:pk>',views.viewblog,name='viewblog'),
    path('deleteimage/<int:pk>',views.deleteimage,name='deleteimage'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

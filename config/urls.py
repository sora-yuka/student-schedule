"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(openapi.Info(
    title="KGTU schedule",
    default_version="0.0.2",
    description="This project used to help for KGTU's students in free plan"
), public=True)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui(renderer="swagger")),
    path('api/v1/account/', include('apps.account.urls')),
    path('api/v1/schedule/', include('apps.schedule.urls')),
    path('api/v1/lessons/', include('apps.lessons.urls')),
    path('api/v1/faculty/', include('apps.faculties.urls')),
    path('api/v1/news/', include('apps.news.urls')),
]

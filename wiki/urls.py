"""wiki URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path,include
from learnapp import views as learn_views
from django.conf import settings

import os
urlpatterns = [
    path('', learn_views.index, name='index'),
    path(r'ueditor/', include('DjangoUeditor.urls')),
    path('email/', learn_views.send),
    path('admin/', admin.site.urls),
]
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


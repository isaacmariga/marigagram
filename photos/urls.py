from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path
                                                                                  

urlpatterns=[
  path('', views.post,name = 'post')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

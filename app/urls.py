from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import dashboard, join_hood, leave_hood


urlpatterns=[
    path('', dashboard, name='dashboard'),
    path('join_hood/<id>', join_hood, name='join-hood'),
    path('leave_hood/<id>', leave_hood, name='leave-hood'),
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

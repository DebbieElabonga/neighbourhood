from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import dashboard, join_hood, leave_hood,profile, hood, business, post, signup



urlpatterns=[
    path('', dashboard, name='dashboard'),
    path('join_hood/<id>', join_hood, name='join-hood'),
    path('leave_hood/<id>', leave_hood, name='leave-hood'),
    path('profile/<username>/', profile, name='profile'),
    path('hood/<id>', hood, name='hood'),
    path('<id>/create_business', business, name='business'),
    path('<id>/create_post', post, name='post'),
    path('signup/', signup, name='signup'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

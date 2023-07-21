from django.contrib import admin
from django.urls import path
from form.views import CreateUser, ListUser
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', CreateUser.as_view(), name='user'),
    path('list/', ListUser.as_view(), name='list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

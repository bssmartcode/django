from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('smartcode/', include('smartcode.urls')),
    path('admin/', admin.site.urls),
]
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path
from main_page import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('biography/', views.about_me, name='about_me'),
    path('my_cat/', views.about_my_pets, name='about_my_pets'),
    path('time_now/', views.system_time, name='system_time')
]
urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,
                      document_root=settings.STATIC_ROOT)
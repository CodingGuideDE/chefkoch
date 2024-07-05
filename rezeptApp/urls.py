from base import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , views.home, name='home'),
    path('cook/<str:pk>' , views.cook, name='cook')

]

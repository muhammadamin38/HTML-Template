from django.contrib import admin
from django.urls import path
from core.views import AboutView, IndexView 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', AboutView.as_view()),
    path('index/', IndexView.as_view()),
    
]

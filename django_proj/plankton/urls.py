from django.contrib import admin
from django.urls import include, path
from .views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('scraping', include('scraping.urls')),  # scraping app
    path('admin/', admin.site.urls),
]
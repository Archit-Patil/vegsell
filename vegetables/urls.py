from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='vegetables-home'),
    path('shopping/', views.shopping, name='vegetables-shopping'),
    path('about/', views.about, name='vegetables-about'),
    path('<int:id>/productdetail', views.productdetail, name='vegetables-productdetail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

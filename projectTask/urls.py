from registration import views
from django.contrib import admin
from django.urls import path,include
from auction import views
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register('apis',views.Api,basename='auctions')




urlpatterns = [
    path('admin/', admin.site.urls),
    path('auction/',include('auction.urls')),
    path('api/',include(router.urls)),
    path('', include('registration.urls')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


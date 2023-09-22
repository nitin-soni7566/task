from django.contrib import admin
from django.urls import path,include
from auctions import views
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static


router = DefaultRouter()
router.register('apis',views.Api,basename='auctions')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auctions/',include('auctions.urls')),
    path('api/',include(router.urls)),
    path('', include('accounts.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
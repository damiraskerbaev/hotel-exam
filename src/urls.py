from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.booking.urls')),
    path('api/', include('apps.guest.urls')),
    path('api/', include('apps.hotel.urls')),
    path('api/', include('apps.room.urls')),
    path('api/dj-rest-auth/', include('dj_rest_auth.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(), name='redoc'),
    path('api/schema/swagger/', SpectacularSwaggerView.as_view(), name='swagger'),

    path('', include('apps.hotel.urls')),
    path('', include('apps.room.urls')),
    path('',include('apps.guest.urls'))
]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)


from django.contrib import admin
from django.urls import path, include
from core.views import home

urlpatterns = [
    path('', home, name='home'),  # Página de inicio personalizada
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),  # Incluir las rutas de la aplicación core
]

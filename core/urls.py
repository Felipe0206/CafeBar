from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductoViewSet, OrdenViewSet, PagoViewSet, InventarioViewSet, ReservaViewSet, ProveedorViewSet, MenuViewSet

router = DefaultRouter()
router.register(r'productos', ProductoViewSet)
router.register(r'ordenes', OrdenViewSet)
router.register(r'pagos', PagoViewSet)
router.register(r'inventarios', InventarioViewSet)
router.register(r'reservas', ReservaViewSet)
router.register(r'proveedores', ProveedorViewSet)
router.register(r'menus', MenuViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

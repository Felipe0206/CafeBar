from rest_framework import viewsets
from django.http import JsonResponse
from .models import Producto, Orden, Pago, Inventario, Reserva, Proveedor, Menu
from .serializers import ProductoSerializer, OrdenSerializer, PagoSerializer, InventarioSerializer, ReservaSerializer, ProveedorSerializer, MenuSerializer

# Controlador para manejar productos
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    def perform_create(self, serializer):
        serializer.save()

    def actualizar_stock(self, producto_id, cantidad):
        producto = Producto.objects.get(id=producto_id)
        producto.stock += cantidad
        producto.save()

    def modificar_precio(self, producto_id, nuevo_precio):
        producto = Producto.objects.get(id=producto_id)
        producto.precio = nuevo_precio
        producto.save()

# Controlador para manejar órdenes
class OrdenViewSet(viewsets.ModelViewSet):
    queryset = Orden.objects.all()
    serializer_class = OrdenSerializer

    def perform_create(self, serializer):
        serializer.save()

    def agregar_producto(self, orden_id, producto_id, cantidad):
        orden = Orden.objects.get(id=orden_id)
        producto = Producto.objects.get(id=producto_id)
        orden.agregar_producto(producto, cantidad)

    def eliminar_producto(self, orden_id, producto_id):
        orden = Orden.objects.get(id=orden_id)
        producto = Producto.objects.get(id=producto_id)
        orden.eliminar_producto(producto)

    def confirmar_pedido(self, orden_id):
        orden = Orden.objects.get(id=orden_id)
        orden.estado = "Confirmado"
        orden.save()

    def cancelar_pedido(self, orden_id):
        orden = Orden.objects.get(id=orden_id)
        orden.estado = "Cancelado"
        orden.save()

# Controlador para manejar pagos
class PagoViewSet(viewsets.ModelViewSet):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer

    def perform_create(self, serializer):
        serializer.save()

    def procesar_pago(self, pago_id):
        pago = Pago.objects.get(id=pago_id)
        pago.estado = "Procesado"
        pago.save()

    def generar_factura(self, pago_id):
        pago = Pago.objects.get(id=pago_id)
        factura = f"Factura para el pago {pago_id}: Monto {pago.monto}, Estado {pago.estado}"
        return factura

# Controlador para manejar inventario
class InventarioViewSet(viewsets.ModelViewSet):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer

    def perform_create(self, serializer):
        serializer.save()

    def actualizar_inventario(self, producto_id, cantidad):
        inventario = Inventario.objects.get(producto_id=producto_id)
        inventario.cantidad += cantidad
        inventario.save()

    def registrar_compra(self, producto_id, cantidad, proveedor_id):
        inventario = Inventario.objects.get(producto_id=producto_id)
        inventario.cantidad += cantidad
        inventario.save()
        proveedor = Proveedor.objects.get(id=proveedor_id)
        # Registrar la compra en un historial (si aplica)
        return f"Compra registrada: {cantidad} unidades de {inventario.producto.nombre} por {proveedor.nombre}"

# Controlador para manejar reservas
class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

    def perform_create(self, serializer):
        serializer.save()

    def crear_reserva(self, usuario_id, fecha, hora, cantidad_personas):
        reserva = Reserva.objects.create(
            usuario_id=usuario_id,
            fecha=fecha,
            hora=hora,
            cantidad_personas=cantidad_personas,
            estado="Pendiente"
        )
        return reserva

    def cancelar_reserva(self, reserva_id):
        reserva = Reserva.objects.get(id=reserva_id)
        reserva.estado = "Cancelada"
        reserva.save()

# Controlador para manejar proveedores
class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer

    def perform_create(self, serializer):
        serializer.save()

    def registrar_proveedor(self, nombre, contacto, productos_suministrados):
        proveedor = Proveedor.objects.create(
            nombre=nombre,
            contacto=contacto,
            productos_suministrados=productos_suministrados
        )
        return proveedor

    def actualizar_datos(self, proveedor_id, nuevos_datos):
        proveedor = Proveedor.objects.get(id=proveedor_id)
        for key, value in nuevos_datos.items():
            setattr(proveedor, key, value)
        proveedor.save()

# Controlador para manejar menú
class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

def home(request):
    return JsonResponse({"message": "Bienvenido a la API de CafeBar"})

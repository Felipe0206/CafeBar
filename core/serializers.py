from rest_framework import serializers
from .models import Producto, Orden, DetalleOrden, Usuario, Inventario, Reserva, Proveedor, Pago, Menu

# Serializador para Usuario
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nombre', 'correo', 'telefono', 'tipo_usuario']

# Serializador para Producto
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'descripcion', 'precio', 'categoria', 'disponibilidad']

# Serializador para DetalleOrden
class DetalleOrdenSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleOrden
        fields = ['id', 'producto', 'cantidad', 'subtotal']

# Serializador para Orden
class OrdenSerializer(serializers.ModelSerializer):
    detalles = DetalleOrdenSerializer(many=True, read_only=True)

    class Meta:
        model = Orden
        fields = ['id', 'fecha', 'estado', 'usuario', 'total', 'detalles']

# Serializador para Pago
class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = ['id', 'monto', 'metodo_pago', 'fecha', 'orden']

# Serializador para Inventario
class InventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventario
        fields = ['id', 'producto', 'cantidad', 'proveedor', 'fecha_ingreso']

# Serializador para Reserva
class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = ['id', 'usuario', 'fecha', 'hora', 'cantidad_personas', 'estado']

# Serializador para Proveedor
class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = ['id', 'nombre', 'contacto', 'productos_suministrados']

# Serializador para Menú
class MenuSerializer(serializers.ModelSerializer):
    productos = ProductoSerializer(many=True, read_only=True)

    class Meta:
        model = Menu
        fields = ['id', 'nombre', 'descripcion', 'productos', 'fecha_creacion']

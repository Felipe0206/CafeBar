from django.contrib import admin
from .models import Usuario, Producto, Orden, Pago, Inventario, Reserva, Proveedor, DetalleOrden, Menu

admin.site.register(Usuario)
admin.site.register(Orden)
admin.site.register(Pago)
admin.site.register(Inventario)
admin.site.register(Reserva)
admin.site.register(Proveedor)
admin.site.register(DetalleOrden)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'categoria', 'disponibilidad')
    search_fields = ('nombre', 'categoria')
    list_filter = ('categoria', 'disponibilidad')

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_creacion')
    search_fields = ('nombre',)
    filter_horizontal = ('productos',)

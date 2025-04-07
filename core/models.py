from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.core.exceptions import ValidationError

# Modelo para Usuario
class Usuario(models.Model):
    TIPOS_USUARIO = [
        ('Cliente', 'Cliente'),
        ('Administrador', 'Administrador'),
        ('Mesero', 'Mesero'),
        ('Barista', 'Barista'),
    ]
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    contraseña = models.CharField(max_length=128)
    tipo_usuario = models.CharField(max_length=20, choices=TIPOS_USUARIO)

    def registrarse(self):
        if Usuario.objects.filter(correo=self.correo).exists():
            raise ValidationError("El correo ya está registrado.")
        self.contraseña = make_password(self.contraseña)
        self.save()

    def iniciar_sesion(self, correo, contraseña):
        try:
            usuario = Usuario.objects.get(correo=correo)
            if check_password(contraseña, usuario.contraseña):
                return usuario
            else:
                raise ValidationError("Contraseña incorrecta.")
        except Usuario.DoesNotExist:
            raise ValidationError("El usuario no existe.")

    def __str__(self):
        return self.nombre

# Modelo para Producto
class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=50)
    disponibilidad = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

# Modelo para Orden
class Orden(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=[('Pendiente', 'Pendiente'), ('Completada', 'Completada')])
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Orden {self.id} - {self.estado}"

# Modelo para Pago
class Pago(models.Model):
    id = models.AutoField(primary_key=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pago = models.CharField(max_length=50)
    fecha = models.DateTimeField(auto_now_add=True)
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE)

    def __str__(self):
        return f"Pago {self.id} - {self.monto}"

# Modelo para Inventario
class Inventario(models.Model):
    id = models.AutoField(primary_key=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    proveedor = models.CharField(max_length=100)
    fecha_ingreso = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Inventario {self.id} - {self.producto.nombre}"

# Modelo para Reserva
class Reserva(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    cantidad_personas = models.PositiveIntegerField()
    estado = models.CharField(max_length=20, choices=[('Pendiente', 'Pendiente'), ('Cancelada', 'Cancelada')])

    def __str__(self):
        return f"Reserva {self.id} - {self.estado}"

# Modelo para Proveedor
class Proveedor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)
    productos_suministrados = models.TextField()

    def __str__(self):
        return self.nombre

# Modelo intermedio para DetalleOrden
class DetalleOrden(models.Model):
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        self.subtotal = self.cantidad * self.producto.precio
        super().save(*args, **kwargs)

# Modelo para Menu
class Menu(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    productos = models.ManyToManyField(Producto, related_name='menus')
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

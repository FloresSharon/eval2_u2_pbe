from django.db import models

# Create your models here.

class Cuenta(models.Model):
    usuario = models.CharField(max_length=80, unique=True)
    correo = models.EmailField()

    class Meta:
        verbose_name_plural = 'Cuentas'
        ordering = ['usuario']

    def __str__(self):
        return self.usuario

class Categoria(models.Model):
    nombre = models.CharField(max_length=120)
    tipo = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = 'Categorias'
        ordering = ['nombre']

    def __str__(self):
        return f"{self.nombre} {self.tipo}"

class Personaje(models.Model):

    raza = models.CharField(max_length=20)
    descripcion = models.TextField(null=True)
    nivel = models.PositiveIntegerField()
    ban = models.BooleanField(default=False)
    creado = models.DateTimeField(auto_now_add=True)

    cuentas = models.ManyToManyField(Cuenta, related_name='cuentas')

    class Meta:
        verbose_name_plural = 'Personajes'
        ordering = ['nivel']

    def __str__(self):
        return f"{self.raza} {self.descripcion} {self.nivel}"

class Item(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    nivel = models.PositiveIntegerField()
    cantidad = models.PositiveIntegerField(default=1, null=True)

    personaje = models.ForeignKey(Personaje, on_delete=models.CASCADE, related_name='personaje')

    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='categoria')

    class Meta:
        verbose_name_plural = 'Items'
        ordering = ['nombre']

    def __str__(self):
        return f"{self.nombre} {self.descripcion} {self.nivel}"
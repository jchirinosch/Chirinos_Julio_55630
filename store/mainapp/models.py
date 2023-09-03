from django.db import models
from django.contrib.auth.models import User

class Guitarra(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    origen = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Guitarra"
        verbose_name_plural = "Guitarras"
        ordering =['modelo'] 

    def __str__(self):
        return f"{self.modelo}"
    
class Bajo(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    origen = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Bajo"
        verbose_name_plural = "Bajos"
        ordering =['modelo'] 

    def __str__(self):
        return f"{self.modelo}"

class Percusion(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    origen = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
   
    class Meta:
        verbose_name = "Percusion"
        verbose_name_plural = "Percusiones"
        ordering =['modelo'] 

    def __str__(self):
        return f"{self.modelo}"
    
class Sucursal(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.TextField()
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
 
    class Meta:
        verbose_name = "Sucursal"
        verbose_name_plural = "Sucursales"
        ordering =['nombre'] 

    def __str__(self):
        return f"{self.nombre}"

class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"       
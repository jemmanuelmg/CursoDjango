from django.db import models
from datetime import datetime


class Employee(models.Model):

    # verbose_name permite definir un label para cuando este campo se use en un formulario
    names = models.CharField(max_length=150, verbose_name='Nombres')
    dni = models.CharField(max_length=10, verbose_name='Cédula', unique=True)
    date_joined = models.DateField(default=datetime.now, verbose_name='Fecha de Registro')
    date_creation = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    age = models.IntegerField(default=0)
    salario = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    state = models.BooleanField(default=True)
    avatar = models.ImageField(upload_to='avatar', null=True, blank=True)
    cvitae = models.FileField(upload_to='cvitae', null=True, blank=True)

    def __str__(self):
        return self.names

    # La clase interna Meta define ciertos detalles de la tabla como su nombre plural, singular, etc.
    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        db_table = 'empleado'
        ordering = ['id']

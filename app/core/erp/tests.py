from app.wsgi import *
from django.test import TestCase
from core.erp.models import Type

# Listar
query = Type.objects.all()
print(query)

# Insertar
t = Type()
t.name = 'Ejemplo'
t.save()

# Actualizar
t = Type.objects.get(id=1)
t.name = 'Accionista'
t.save()

# Eliminacion
t = Type.objects.get(id=1)
t.delete()

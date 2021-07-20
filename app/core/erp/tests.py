# # Listar
# query = Type.objects.all()
# print(query)
#
# # Insertar
# t = Type()
# t.name = 'Ejemplo'
# t.save()
#
# # Actualizar
# t = Type.objects.get(id=1)
# t.name = 'Accionista'
# t.save()
#
# Eliminacion
# t = Type.objects.get(id=1)
# t.delete()
from models import Category
from choices import *

data = ['Leche y derivados', 'Carnes, pescados y huevos', 'Patatas, legumbres, frutos secos',
        'Verduras y Hortalizas', 'Frutas', 'Cereales y derivados, azúcar y dulces',
        'Grasas, aceite y mantequilla']

for i in data:
    cat = Category(name=i)
    cat.save()
    print('Guardado registro N°{}'.format(cat.id))
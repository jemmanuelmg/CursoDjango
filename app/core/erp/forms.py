from django.forms import ModelForm, TextInput, Textarea
from core.erp.models import Category

# Formulario para crear una categoría. En esta clase se especifica que
# el modelo sobre el cual va a actuar es Category, y que al renderizar un
# formulario para crear una categoría debe usar los siguientes campos y widgets (inputs)
# para cada campo. Esta clase hereda de ModelForm un mètodo para guardar un registro
# del tipo seleccionado, en este caso de Category. El método se llama save() y se puede llamar
# desde una view en el método POST.
class CategoryForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'

    # Sobreescritura del metodo save para capturar excepciones y retornarlas
    # a el usuario
    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

    class Meta:
        model = Category
        fields = '__all__'
        labels = {
            'name' : 'Nombre de la categoría'
        }
        widgets = {
            'name': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese un nombre',
                    'autocomplete': 'off'
                }
            ),
            'desc': Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Describa la categoría',
                    'autocomplete': 'off',
                    'rows': 3,
                    'cols': 3
                }
            ),
        }
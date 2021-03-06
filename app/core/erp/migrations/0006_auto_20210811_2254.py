# Generated by Django 3.2.5 on 2021-08-12 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0005_alter_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='desc',
            field=models.CharField(default='(Sin Descripción)', max_length=500, verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=150, unique=True, verbose_name='Nombre'),
        ),
    ]

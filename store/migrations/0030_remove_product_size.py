# Generated by Django 4.0.3 on 2022-05-07 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0029_size_alter_product_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='size',
        ),
    ]
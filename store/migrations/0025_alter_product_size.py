# Generated by Django 4.0.3 on 2022-04-24 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0024_product_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.ForeignKey(default='Unknown', on_delete=django.db.models.deletion.CASCADE, to='store.size'),
        ),
    ]
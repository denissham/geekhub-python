# Generated by Django 4.0.1 on 2022-02-09 01:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category_fk',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.category'),
        ),
    ]
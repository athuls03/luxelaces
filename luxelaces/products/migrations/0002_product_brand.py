# Generated by Django 5.1.3 on 2025-02-10 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.CharField(default='exit', max_length=200),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.2 on 2023-06-23 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stripe_id',
            field=models.TextField(blank=True, default=None),
        ),
    ]

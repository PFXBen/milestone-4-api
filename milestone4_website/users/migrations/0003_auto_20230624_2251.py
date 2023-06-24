# Generated by Django 3.2 on 2023-06-24 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address_1',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='address_2',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='address_city',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='address_country',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='stripe_customer_id',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
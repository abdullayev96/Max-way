# Generated by Django 4.0.7 on 2022-08-23 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_category_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderproduct',
            name='category',
        ),
        migrations.RemoveField(
            model_name='orderproduct',
            name='description',
        ),
        migrations.RemoveField(
            model_name='orderproduct',
            name='title',
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
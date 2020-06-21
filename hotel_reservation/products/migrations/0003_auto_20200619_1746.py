# Generated by Django 3.0.7 on 2020-06-19 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_reservation'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='how_many_accepts',
            field=models.IntegerField(default=2),
        ),
        migrations.AddField(
            model_name='reservation',
            name='how_many_users',
            field=models.IntegerField(default=1),
        ),
    ]
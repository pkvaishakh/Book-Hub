# Generated by Django 4.2.15 on 2024-08-11 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, upload_to='bookImages/'),
        ),
    ]

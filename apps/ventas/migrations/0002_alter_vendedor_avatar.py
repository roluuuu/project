# Generated by Django 4.2.1 on 2023-06-16 02:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ventas", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="vendedor",
            name="avatar",
            field=models.ImageField(blank=True, null=True, upload_to="avatars"),
        ),
    ]

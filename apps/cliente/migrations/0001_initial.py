# Generated by Django 4.2.1 on 2023-05-29 19:31

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cliente",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("telefono", models.CharField(max_length=20)),
                ("direccion", models.CharField(max_length=200)),
            ],
        ),
    ]
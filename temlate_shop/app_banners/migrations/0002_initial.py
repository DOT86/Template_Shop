# Generated by Django 4.2 on 2023-07-12 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("app_catalog", "0001_initial"),
        ("app_banners", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="banner",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="app_catalog.product"
            ),
        ),
    ]

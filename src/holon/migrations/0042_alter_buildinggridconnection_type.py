# Generated by Django 4.1.9 on 2023-06-05 11:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("holon", "0041_biogasmethaneconverter_dieselconsumptionasset_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="buildinggridconnection",
            name="type",
            field=models.CharField(
                choices=[
                    ("STORE", "Store"),
                    ("OFFICE", "Office"),
                    ("LOGISTICS", "Logistics"),
                    ("FARM", "Farm"),
                    ("VILLAGE", "Village"),
                ],
                max_length=100,
            ),
        ),
    ]

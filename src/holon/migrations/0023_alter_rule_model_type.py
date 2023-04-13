# Generated by Django 4.1.7 on 2023-03-28 13:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("holon", "0022_merge_20230328_1312"),
    ]

    operations = [
        migrations.AlterField(
            model_name="rule",
            name="model_type",
            field=models.CharField(
                choices=[
                    ("Actor", "Actor"),
                    ("Contract", "Contract"),
                    ("EnergyAsset", "Energyasset"),
                    ("GridNode", "Gridnode"),
                    ("GridConnection", "Gridconnection"),
                    ("Policy", "Policy"),
                ],
                max_length=255,
            ),
        ),
    ]

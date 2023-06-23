# Generated by Django 4.1.9 on 2023-06-23 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("holon", "0058_datamodelqueryrule_self_conversion_factor_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="actor",
            name="group",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="holon.actorgroup",
            ),
        ),
    ]

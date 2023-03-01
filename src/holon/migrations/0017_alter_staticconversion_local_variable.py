# Generated by Django 4.1.7 on 2023-03-01 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("holon", "0016_alter_staticconversion_value"),
    ]

    operations = [
        migrations.AlterField(
            model_name="staticconversion",
            name="local_variable",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="holon.floatkeyvaluepair",
            ),
        ),
    ]

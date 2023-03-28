# Generated by Django 4.1.7 on 2023-03-28 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("holon", "0020_merge_20230327_1111"),
    ]

    operations = [
        migrations.AddField(
            model_name="scenario",
            name="cloned_from",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="holon.scenario",
            ),
        ),
    ]

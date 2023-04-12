# Generated by Django 4.1.3 on 2022-11-01 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("customdocument", "0003_auto_20190209_1710"),
        ("api", "0003_scenario_remove_slider_slider_locked_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="scenario",
            name="config_file",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="customdocument.customdocument",
            ),
        ),
        migrations.AddField(
            model_name="scenario",
            name="etm_scenario_id",
            field=models.IntegerField(default=123456),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="scenario",
            name="force_uncached",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="scenario",
            name="log_exceptions",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="scenario",
            name="model_name",
            field=models.CharField(default="", max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="scenario",
            name="parallelize",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="scenario",
            name="show_progress",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="scenario",
            name="timestep_hours",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
            preserve_default=False,
        ),
    ]

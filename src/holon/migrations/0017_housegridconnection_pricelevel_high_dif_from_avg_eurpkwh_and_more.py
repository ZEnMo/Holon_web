# Generated by Django 4.1.7 on 2023-03-02 16:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("holon", "0016_remove_buildinggridconnection_heatmodel_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="housegridconnection",
            name="pricelevel_high_dif_from_avg_eurpkWh",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="housegridconnection",
            name="pricelevel_low_dif_from_avg_eurpkWh",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="housegridconnection",
            name="smart_assets",
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="housegridconnection",
            name="temp_setpoint_day_degC",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="housegridconnection",
            name="temp_setpoint_day_start_hr",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="housegridconnection",
            name="temp_setpoint_night_degC",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="housegridconnection",
            name="temp_setpoint_night_start_hr",
            field=models.FloatField(blank=True, null=True),
        ),
    ]

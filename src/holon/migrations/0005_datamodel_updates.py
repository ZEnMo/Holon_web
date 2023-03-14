# Generated by Django 4.1.7 on 2023-03-09 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("holon", "0004_alter_interactiveelement_level_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contract",
            name="contractScope",
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to="holon.actor"),
        ),
        migrations.CreateModel(
            name="ActorGroup",
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
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="ActorSubGroup",
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
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name="actor",
            name="group",
        ),
        migrations.RemoveField(
            model_name="actor",
            name="subgroup",
        ),
        migrations.AddField(
            model_name="actor",
            name="group",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="holon.actorgroup",
            ),
        ),
        migrations.AddField(
            model_name="actor",
            name="subgroup",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="holon.actorsubgroup",
            ),
        ),
        migrations.RemoveField(
            model_name="gridconnection",
            name="nfATO_capacity_kw",
        ),
        migrations.RemoveField(
            model_name="gridconnection",
            name="nfATO_endtime",
        ),
        migrations.RemoveField(
            model_name="gridconnection",
            name="nfATO_starttime",
        ),
        migrations.DeleteModel(
            name="NonFirmActor",
        ),
        migrations.AddField(
            model_name="gridconnection",
            name="electrolyser_mode",
            field=models.CharField(
                blank=True,
                choices=[("BALANCE", "Balance"), ("PRICE", "Price")],
                max_length=100,
                null=True,
            ),
        ),
        migrations.RemoveField(
            model_name="housegridconnection",
            name="pricelevelHighDifFromAvg_eurpkWh",
        ),
        migrations.RemoveField(
            model_name="housegridconnection",
            name="pricelevelLowDifFromAvg_eurpkWh",
        ),
        migrations.RemoveField(
            model_name="housegridconnection",
            name="tempSetpointDay_degC",
        ),
        migrations.RemoveField(
            model_name="housegridconnection",
            name="tempSetpointDay_start_hr",
        ),
        migrations.RemoveField(
            model_name="housegridconnection",
            name="tempSetpointNight_degC",
        ),
        migrations.RemoveField(
            model_name="housegridconnection",
            name="tempSetpointNight_start_hr",
        ),
        migrations.AddField(
            model_name="builtenvironmentgridconnection",
            name="pricelevelHighDifFromAvg_eurpkWh",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="builtenvironmentgridconnection",
            name="pricelevelLowDifFromAvg_eurpkWh",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="builtenvironmentgridconnection",
            name="tempSetpointDay_degC",
            field=models.FloatField(default=20.0),
        ),
        migrations.AddField(
            model_name="builtenvironmentgridconnection",
            name="tempSetpointDay_start_hr",
            field=models.FloatField(default=8.0),
        ),
        migrations.AddField(
            model_name="builtenvironmentgridconnection",
            name="tempSetpointNight_degC",
            field=models.FloatField(default=16.0),
        ),
        migrations.AddField(
            model_name="builtenvironmentgridconnection",
            name="tempSetpointNight_start_hr",
            field=models.FloatField(default=20.0),
        ),
    ]

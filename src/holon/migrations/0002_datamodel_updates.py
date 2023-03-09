# Generated by Django 4.1.7 on 2023-03-09 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("holon", "0001_initial"),
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
    ]

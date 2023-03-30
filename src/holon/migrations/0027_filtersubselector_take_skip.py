# Generated by Django 4.1.7 on 2023-03-30 10:19

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("holon", "0026_alter_ruleactionchangeattribute_static_value"),
    ]

    operations = [
        migrations.CreateModel(
            name="FilterSubSelector",
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
                ("use_interactive_element_value", models.BooleanField(default=True)),
                ("number_of_items", models.IntegerField(blank=True, null=True)),
                (
                    "polymorphic_ctype",
                    models.ForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="polymorphic_%(app_label)s.%(class)s_set+",
                        to="contenttypes.contenttype",
                    ),
                ),
            ],
            options={
                "abstract": False,
                "base_manager_name": "objects",
            },
        ),
        migrations.CreateModel(
            name="Take",
            fields=[
                (
                    "filtersubselector_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="holon.filtersubselector",
                    ),
                ),
                (
                    "mode",
                    models.CharField(
                        choices=[("FIRST", "First"), ("RANDOM", "Random")],
                        max_length=32,
                    ),
                ),
                (
                    "rule",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="subselector_takes",
                        to="holon.rule",
                    ),
                ),
            ],
            options={
                "abstract": False,
                "base_manager_name": "objects",
            },
            bases=("holon.filtersubselector",),
        ),
        migrations.CreateModel(
            name="Skip",
            fields=[
                (
                    "filtersubselector_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="holon.filtersubselector",
                    ),
                ),
                (
                    "rule",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="subselector_skips",
                        to="holon.rule",
                    ),
                ),
            ],
            options={
                "abstract": False,
                "base_manager_name": "objects",
            },
            bases=("holon.filtersubselector",),
        ),
    ]

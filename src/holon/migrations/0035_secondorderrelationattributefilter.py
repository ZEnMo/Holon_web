# Generated by Django 4.1.7 on 2023-04-06 12:28

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ("holon", "0034_alter_builtenvironmentgridconnection_heating_type_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="SecondOrderRelationAttributeFilter",
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
                (
                    "model_attribute",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "comparator",
                    models.CharField(
                        choices=[
                            ("EQUAL", "Equal"),
                            ("LESS THAN", "Less Than"),
                            ("GREATER THAN", "Greater Than"),
                            ("NOT EQUAL", "Not Equal"),
                        ],
                        max_length=255,
                    ),
                ),
                ("value", models.JSONField(blank=True, null=True)),
                ("relation_field", models.CharField(max_length=255)),
                (
                    "relation_field_subtype",
                    models.CharField(blank=True, max_length=255),
                ),
                ("second_order_relation_field", models.CharField(max_length=255)),
                (
                    "second_order_relation_field_subtype",
                    models.CharField(blank=True, max_length=255),
                ),
                (
                    "invert_filter",
                    models.BooleanField(
                        default=False,
                        help_text="Filter models that don't satisfy the model attribute comparison",
                    ),
                ),
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
                (
                    "rule",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="second_order_relation_attribute_filters",
                        to="holon.rule",
                    ),
                ),
            ],
            options={
                "verbose_name": "RelationAttributeFilter",
            },
        ),
    ]

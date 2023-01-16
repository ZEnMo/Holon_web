# Generated by Django 4.1.5 on 2023-01-16 11:17

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0031_casusoverviewpage_casuspage"),
    ]

    operations = [
        migrations.CreateModel(
            name="CasusFilter",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                (
                    "slug",
                    autoslug.fields.AutoSlugField(editable=False, populate_from="name"),
                ),
                (
                    "icon",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("book", "Book"),
                            ("bell", "Bell"),
                            ("cog", "Cog"),
                            ("folder", "Folder"),
                            ("heart", "Heart"),
                            ("info", "Info"),
                            ("lightning", "Lightning bolt"),
                            ("mapmarker", "Map marker"),
                            ("rocket", "Rocket"),
                            ("star", "Star"),
                            ("user", "User"),
                        ],
                        default="green",
                        help_text="Icon shown in storyline overview page",
                        max_length=20,
                    ),
                ),
            ],
            options={
                "verbose_name": "CasusFilter",
                "verbose_name_plural": "CasusFilters",
                "ordering": ["name"],
            },
        ),
    ]

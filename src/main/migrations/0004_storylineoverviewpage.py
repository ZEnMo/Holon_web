# Generated by Django 4.1.2 on 2022-10-20 11:24

from django.db import migrations, models
import django.db.models.deletion
import wagtail.blocks
import wagtail.fields
import wagtail_headless_preview.models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0003_wikipage"),
    ]

    operations = [
        migrations.CreateModel(
            name="StorylineOverviewPage",
            fields=[
                (
                    "basepage_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="main.basepage",
                    ),
                ),
                (
                    "storyline",
                    wagtail.fields.StreamField(
                        [
                            (
                                "storylineoverview",
                                wagtail.blocks.StructBlock(
                                    [
                                        (
                                            "visible",
                                            wagtail.blocks.BooleanBlock(default=True),
                                        )
                                    ]
                                ),
                            )
                        ],
                        blank=True,
                        null=True,
                        use_json_field=True,
                    ),
                ),
            ],
            options={
                "verbose_name": "StorylineOverview",
            },
            bases=(
                wagtail_headless_preview.models.HeadlessPreviewMixin,
                "main.basepage",
            ),
        ),
    ]

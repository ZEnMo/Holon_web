# Generated by Django 4.1.2 on 2022-10-13 11:12

from django.db import migrations
import wagtail.blocks
import wagtail.embeds.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0004_storylinepage_remove_articlepage_basepage_ptr_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="storylinepage",
            name="storyline",
            field=wagtail.fields.StreamField(
                [
                    (
                        "intro",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "text",
                                    wagtail.blocks.RichTextBlock(
                                        help_text="Add your text",
                                        required=True,
                                        rows=15,
                                    ),
                                ),
                                (
                                    "media",
                                    wagtail.blocks.StreamBlock(
                                        [
                                            (
                                                "image",
                                                wagtail.images.blocks.ImageChooserBlock(
                                                    required=False
                                                ),
                                            ),
                                            (
                                                "video",
                                                wagtail.embeds.blocks.EmbedBlock(
                                                    required=False
                                                ),
                                            ),
                                        ],
                                        help_text="Choose an image or paste an embed url",
                                        max_num=1,
                                    ),
                                ),
                                (
                                    "grid_layout",
                                    wagtail.blocks.ChoiceBlock(
                                        choices=[
                                            ("25_75", "25% - 75%"),
                                            ("50_50", "50% - 50%"),
                                            ("75_25", "75% - 25%"),
                                        ]
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "section",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "scenario",
                                    wagtail.blocks.ChoiceBlock(
                                        choices=[
                                            ("scenario-1", "Scenario 1"),
                                            ("scenario-2", "Scenario 2"),
                                            ("scenario-3", "Scenario 3"),
                                        ]
                                    ),
                                )
                            ]
                        ),
                    ),
                ],
                use_json_field=True,
            ),
        ),
    ]

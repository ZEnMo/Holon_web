# Generated by Django 4.1.2 on 2022-10-20 14:07

from django.db import migrations, models
import django.db.models.deletion
import main.blocks.storyline_section
import wagtail.blocks
import wagtail.embeds.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0003_scenario_remove_slider_slider_locked_and_more"),
        ("main", "0004_storylinepage_remove_articlepage_basepage_ptr_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="storylinepage",
            name="scenario",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="api.scenario",
            ),
        ),
        migrations.AlterField(
            model_name="storylinepage",
            name="storyline",
            field=wagtail.fields.StreamField(
                [
                    (
                        "text_and_media",
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
                                    "content",
                                    wagtail.blocks.StreamBlock(
                                        [
                                            ("text", wagtail.blocks.RichTextBlock()),
                                            (
                                                "slider",
                                                wagtail.blocks.StructBlock(
                                                    [
                                                        (
                                                            "slider",
                                                            wagtail.blocks.ChoiceBlock(
                                                                choices=main.blocks.storyline_section.get_sliders
                                                            ),
                                                        ),
                                                        (
                                                            "visible",
                                                            wagtail.blocks.BooleanBlock(
                                                                required=False
                                                            ),
                                                        ),
                                                        (
                                                            "locked",
                                                            wagtail.blocks.BooleanBlock(
                                                                required=False
                                                            ),
                                                        ),
                                                    ]
                                                ),
                                            ),
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

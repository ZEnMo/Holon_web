# Generated by Django 4.1.3 on 2022-11-16 09:27

from django.db import migrations
import main.blocks.holon_image_chooser
import main.blocks.rich_text_block
import main.blocks.storyline_section
import wagtail.blocks
import wagtail.embeds.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0013_alter_homepage_content_alter_staticpage_content_and_more"),
    ]

    operations = [
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
                                    "grid_layout",
                                    wagtail.blocks.StructBlock(
                                        [
                                            (
                                                "grid",
                                                wagtail.blocks.ChoiceBlock(
                                                    choices=[
                                                        ("33_66", "33% - 66%"),
                                                        ("50_50", "50% - 50%"),
                                                        ("66_33", "66% - 33%"),
                                                    ]
                                                ),
                                            )
                                        ],
                                        required=True,
                                    ),
                                ),
                                (
                                    "background",
                                    wagtail.blocks.StructBlock(
                                        [
                                            (
                                                "color",
                                                wagtail.blocks.ChoiceBlock(
                                                    choices=[
                                                        ("block__bg-white", "White"),
                                                        ("block__bg-gray", "Pale gray"),
                                                        (
                                                            "block__bg-purple",
                                                            "Pale purple",
                                                        ),
                                                    ]
                                                ),
                                            ),
                                            (
                                                "size",
                                                wagtail.blocks.ChoiceBlock(
                                                    choices=[
                                                        (
                                                            "bg__full",
                                                            "Full backgroundcolor",
                                                        ),
                                                        (
                                                            "bg__left",
                                                            "Only backgroundcolor in the left block",
                                                        ),
                                                    ]
                                                ),
                                            ),
                                        ]
                                    ),
                                ),
                                (
                                    "text",
                                    main.blocks.rich_text_block.RichtextBlock(
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
                                                main.blocks.holon_image_chooser.HolonImageChooserBlock(
                                                    required=False
                                                ),
                                            ),
                                            (
                                                "video",
                                                wagtail.embeds.blocks.EmbedBlock(
                                                    help_text="Youtube url of vimeo url",
                                                    required=False,
                                                ),
                                            ),
                                        ],
                                        help_text="Choose an image or paste an embed url",
                                        max_num=1,
                                    ),
                                ),
                                (
                                    "alt_text",
                                    wagtail.blocks.CharBlock(
                                        help_text="Fill in this alt-text only when you want to describe the image (for screenreaders and SEO)",
                                        required=False,
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
                                    "background",
                                    wagtail.blocks.StructBlock(
                                        [
                                            (
                                                "color",
                                                wagtail.blocks.ChoiceBlock(
                                                    choices=[
                                                        ("block__bg-white", "White"),
                                                        ("block__bg-gray", "Pale gray"),
                                                        (
                                                            "block__bg-purple",
                                                            "Pale purple",
                                                        ),
                                                    ]
                                                ),
                                            ),
                                            (
                                                "size",
                                                wagtail.blocks.ChoiceBlock(
                                                    choices=[
                                                        (
                                                            "bg__full",
                                                            "Full backgroundcolor",
                                                        ),
                                                        (
                                                            "bg__left",
                                                            "Only backgroundcolor in the left block",
                                                        ),
                                                    ]
                                                ),
                                            ),
                                        ]
                                    ),
                                ),
                                (
                                    "grid_layout",
                                    wagtail.blocks.StructBlock(
                                        [
                                            (
                                                "grid",
                                                wagtail.blocks.ChoiceBlock(
                                                    choices=[
                                                        ("33_66", "33% - 66%"),
                                                        ("50_50", "50% - 50%"),
                                                        ("66_33", "66% - 33%"),
                                                    ]
                                                ),
                                            )
                                        ],
                                        required=True,
                                    ),
                                ),
                                (
                                    "content",
                                    wagtail.blocks.StreamBlock(
                                        [
                                            (
                                                "text",
                                                main.blocks.rich_text_block.RichtextBlock(),
                                            ),
                                            (
                                                "slider",
                                                wagtail.blocks.StructBlock(
                                                    [
                                                        (
                                                            "interactive_input",
                                                            wagtail.blocks.ChoiceBlock(
                                                                choices=main.blocks.storyline_section.get_interactive_inputs
                                                            ),
                                                        ),
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
                                            (
                                                "static_image",
                                                main.blocks.holon_image_chooser.HolonImageChooserBlock(
                                                    required=False
                                                ),
                                            ),
                                            (
                                                "animation",
                                                wagtail.blocks.ChoiceBlock(
                                                    choices=[
                                                        (
                                                            "animation1",
                                                            "Animatie 1 (Test)",
                                                        ),
                                                        (
                                                            "solar_and_windmills",
                                                            "Solarpanels and windmills",
                                                        ),
                                                        (
                                                            "animation1",
                                                            "Animatie 3 (Test)",
                                                        ),
                                                    ],
                                                    required=False,
                                                ),
                                            ),
                                        ],
                                        block_counts={
                                            "animation": {"max_num": 1},
                                            "static_image": {"max_num": 1},
                                        },
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "heroblock",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "background_color",
                                    wagtail.blocks.ChoiceBlock(
                                        choices=[
                                            ("", "Default color"),
                                            ("block__bg-gray", "Pale gray"),
                                            ("block__bg-purple", "Pale purple"),
                                        ],
                                        required=False,
                                    ),
                                ),
                                (
                                    "title",
                                    wagtail.blocks.CharBlock(
                                        form_classname="title", required=True
                                    ),
                                ),
                                (
                                    "text",
                                    main.blocks.rich_text_block.RichtextBlock(
                                        required=True
                                    ),
                                ),
                                (
                                    "media",
                                    wagtail.blocks.StreamBlock(
                                        [
                                            (
                                                "image",
                                                main.blocks.holon_image_chooser.HolonImageChooserBlock(
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
                                    "alt_text",
                                    wagtail.blocks.CharBlock(
                                        help_text="Fill in this alt-text only when you want to describe the image (for screenreaders and SEO)",
                                        required=False,
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "title_block",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "background_color",
                                    wagtail.blocks.ChoiceBlock(
                                        choices=[
                                            ("", "Default color"),
                                            ("block__bg-gray", "Pale gray"),
                                            ("block__bg-purple", "Pale purple"),
                                        ],
                                        required=False,
                                    ),
                                ),
                                ("title", wagtail.blocks.CharBlock(required=True)),
                                (
                                    "size",
                                    wagtail.blocks.ChoiceBlock(
                                        blank=True,
                                        choices=[
                                            ("", "Select header size"),
                                            ("h1", "H1"),
                                            ("h2", "H2"),
                                        ],
                                    ),
                                ),
                                (
                                    "text",
                                    main.blocks.rich_text_block.RichtextBlock(
                                        required=False
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "card_block",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "cards",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.StructBlock(
                                            [
                                                (
                                                    "title",
                                                    wagtail.blocks.CharBlock(
                                                        required=False
                                                    ),
                                                ),
                                                (
                                                    "image_selector",
                                                    main.blocks.holon_image_chooser.HolonImageChooserBlock(),
                                                ),
                                                (
                                                    "text",
                                                    wagtail.blocks.CharBlock(
                                                        max_length=255, required=False
                                                    ),
                                                ),
                                                (
                                                    "card_background",
                                                    wagtail.blocks.ChoiceBlock(
                                                        choices=[
                                                            ("card__bg-gold", "Gold"),
                                                            ("card__bg-blue", "Blue"),
                                                            ("card__bg-gray", "Gray"),
                                                            (
                                                                "card__bg-purple",
                                                                "Purple",
                                                            ),
                                                            ("card__bg-pink", "Pink"),
                                                            (
                                                                "card__bg-orange",
                                                                "Orange",
                                                            ),
                                                        ],
                                                        required=False,
                                                    ),
                                                ),
                                            ]
                                        )
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

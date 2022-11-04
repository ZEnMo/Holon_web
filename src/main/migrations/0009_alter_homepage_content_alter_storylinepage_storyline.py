# Generated by Django 4.1.2 on 2022-11-04 12:28

from django.db import migrations
import main.blocks.holon_image_chooser
import main.blocks.storyline_section
import wagtail.blocks
import wagtail.embeds.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0008_alter_homepage_content_alter_storylinepage_storyline"),
    ]

    operations = [
        migrations.AlterField(
            model_name="homepage",
            name="content",
            field=wagtail.fields.StreamField(
                [
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
                                            ("block__bg-gray", "Pale purple"),
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
                                        required=False,
                                    ),
                                ),
                                ("text", wagtail.blocks.RichTextBlock(required=False)),
                            ]
                        ),
                    ),
                    (
                        "hero_block",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "background_color",
                                    wagtail.blocks.ChoiceBlock(
                                        choices=[
                                            ("", "Default color"),
                                            ("block__bg-gray", "Pale gray"),
                                            ("block__bg-gray", "Pale purple"),
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
                                ("text", wagtail.blocks.RichTextBlock(required=True)),
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
                        "text_image_block",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "background_color",
                                    wagtail.blocks.ChoiceBlock(
                                        choices=[
                                            ("", "Default color"),
                                            ("block__bg-gray", "Pale gray"),
                                            ("block__bg-gray", "Pale purple"),
                                        ],
                                        required=False,
                                    ),
                                ),
                                (
                                    "title",
                                    wagtail.blocks.CharBlock(
                                        help_text="Add your title", required=True
                                    ),
                                ),
                                (
                                    "size",
                                    wagtail.blocks.ChoiceBlock(
                                        blank=True,
                                        choices=[
                                            ("", "Select header size"),
                                            ("h2", "H2"),
                                            ("h3", "H3"),
                                            ("h4", "H4"),
                                            ("h5", "H5"),
                                        ],
                                        required=False,
                                    ),
                                ),
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
                                (
                                    "grid_layout",
                                    wagtail.blocks.ChoiceBlock(
                                        choices=[
                                            ("33_66", "33% - 66%"),
                                            ("50_50", "50% - 50%"),
                                            ("66_33", "66% - 33%"),
                                        ]
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
                                                        required=False
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
                blank=True,
                null=True,
                use_json_field=None,
                verbose_name="Page body",
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
                                    "background_color",
                                    wagtail.blocks.ChoiceBlock(
                                        choices=[
                                            ("", "Default color"),
                                            ("block__bg-gray", "Pale gray"),
                                            ("block__bg-gray", "Pale purple"),
                                        ],
                                        required=False,
                                    ),
                                ),
                                (
                                    "title",
                                    wagtail.blocks.CharBlock(
                                        help_text="Add your title", required=True
                                    ),
                                ),
                                (
                                    "size",
                                    wagtail.blocks.ChoiceBlock(
                                        blank=True,
                                        choices=[
                                            ("", "Select header size"),
                                            ("h2", "H2"),
                                            ("h3", "H3"),
                                            ("h4", "H4"),
                                            ("h5", "H5"),
                                        ],
                                        required=False,
                                    ),
                                ),
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
                                (
                                    "grid_layout",
                                    wagtail.blocks.ChoiceBlock(
                                        choices=[
                                            ("33_66", "33% - 66%"),
                                            ("50_50", "50% - 50%"),
                                            ("66_33", "66% - 33%"),
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
                                            ("block__bg-gray", "Pale purple"),
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
                                ("text", wagtail.blocks.RichTextBlock(required=True)),
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
                                            ("block__bg-gray", "Pale purple"),
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
                                        required=False,
                                    ),
                                ),
                                ("text", wagtail.blocks.RichTextBlock(required=False)),
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
                                                        required=False
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

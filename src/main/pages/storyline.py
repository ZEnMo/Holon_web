from django.utils.translation import gettext_lazy as _

from wagtail import blocks
from wagtail_headless_preview.models import HeadlessPreviewMixin
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField

from api.models import Slider

from .base import BasePage
from ..blocks import TextAndMediaBlock

scenarios = [
    ("scenario-1", "Scenario 1"),
    ("scenario-2", "Scenario 2"),
    ("scenario-3", "Scenario 3"),
]


def get_sliders():
    return [(slider.pk, slider.name) for slider in Slider.objects.all()]


class SliderBlock(blocks.StructBlock):
    slider = blocks.ChoiceBlock(choices=get_sliders)
    visible = blocks.BooleanBlock(required=False)


class StorylinePage(HeadlessPreviewMixin, BasePage):
    storyline = StreamField(
        [
            ("intro", TextAndMediaBlock()),
            (
                "section",
                blocks.StructBlock(
                    [
                        ("scenario", blocks.ChoiceBlock(choices=scenarios)),
                        (
                            "content",
                            blocks.StreamBlock(
                                [
                                    ("text", blocks.RichTextBlock()),
                                    ("slider", SliderBlock()),
                                    # ("radiobuttons", RadioButtonBlock()),
                                ]
                            ),
                        ),
                    ]
                ),
            ),
        ],
        block_counts={"intro": {"min_num": 1, "max_num": 1}},
        use_json_field=True,
    )

    content_panels = BasePage.content_panels + [
        FieldPanel("storyline"),
    ]

    class Meta:
        verbose_name = _("Storyline")

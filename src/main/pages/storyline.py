from django.utils.translation import gettext_lazy as _

from wagtail import blocks
from wagtail_headless_preview.models import HeadlessPreviewMixin
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField


from .base import BasePage
from ..blocks import TextAndMediaBlock, ScenarioBlock


class StorylinePage(HeadlessPreviewMixin, BasePage):
    storyline = StreamField(
        [
            ("text_and_media", TextAndMediaBlock()),
            ("scenario", ScenarioBlock()),
        ],
        block_counts={"text_and_media": {"min_num": 1, "max_num": 1}, "scenario": {"min_num": 1}},
        use_json_field=True,
    )

    serializer_class = "main.pages.StorylinePageSerializer"
    content_panels = BasePage.content_panels + [
        FieldPanel("storyline"),
    ]

    class Meta:
        verbose_name = _("Storyline")

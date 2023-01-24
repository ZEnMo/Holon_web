from django.utils.translation import gettext_lazy as _
from django.db import models
from django import forms

from wagtail.admin.edit_handlers import FieldPanel
from wagtail_headless_preview.models import HeadlessPreviewMixin

from .base import BasePage


class BestPracticePage(HeadlessPreviewMixin, BasePage):
    extra_panels = BasePage.extra_panels
    serializer_class = "main.pages.BestPracticePageSerializer"

    parent_page_types = ["main.BestPracticeOverviewPage"]
    subpage_types = []

    class Meta:
        verbose_name = _("Best Practice")
        verbose_name_plural = _("Best Practices")

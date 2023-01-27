from django.utils.translation import gettext_lazy as _
from django.db import models
from django.core.validators import MinValueValidator
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.core.models import Orderable
from wagtail.models import Page
from wagtail.admin.panels import PageChooserPanel

# from django.core.validators import MinValueValidator
from wagtail.snippets.models import register_snippet

CHOICE_SINGLESELECT = "single_select"
CHOICE_MULTISELECT = "multi_select"
CHOICE_CONTINUOUS = "continuous"
TYPE_CHOICES = (
    (CHOICE_SINGLESELECT, "Single Select"),
    (CHOICE_MULTISELECT, "Multi Select"),
    (CHOICE_CONTINUOUS, "Continuous (slider)"),
)

ANIMATION_NONE = "no-animation"
ANIMATION_TILES = "tiles"
ANIMATION_SOLAR_ROOF = "solarpanels-roof"
ANIMATION_TRANSPORT_ELECTRIFICATION = "transport-electrification"
ANIMATION_CHOICES = (
    (ANIMATION_NONE, "Geen animatie"),
    (ANIMATION_TILES, "Tegels"),
    (ANIMATION_SOLAR_ROOF, "Solarpanels on roof"),
    (ANIMATION_TRANSPORT_ELECTRIFICATION, "Transport electriciteit"),
)

COLOR_NONE = ""
COLOR_RED = "red"
COLOR_ORANGE = "orange"
COLOR_GREEN = "limegreen"
COLOR_CHOICES = (
    (COLOR_NONE, "No color"),
    (COLOR_RED, "Red"),
    (COLOR_ORANGE, "Orange"),
    (COLOR_GREEN, "Green"),
)

# Create your models here.
@register_snippet
class InteractiveInput(ClusterableModel):

    etm_key = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=100)
    type = models.CharField(
        max_length=14,
        choices=TYPE_CHOICES,
        default=CHOICE_CONTINUOUS,
    )
    animation_tag = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        choices=ANIMATION_CHOICES,
        default=ANIMATION_NONE,
    )
    asset_type = models.ForeignKey(
        "holon.Asset", on_delete=models.SET_NULL, null=True, blank=True, related_name="+"
    )

    panels = [
        FieldPanel("name"),
        FieldPanel("type"),
        FieldPanel("animation_tag"),
        FieldPanel("asset_type"),
        FieldPanel("etm_key"),
        InlinePanel(
            "options",
            heading="Options",
            label="Option",
            help_text=_(
                "Fill in the options for all the types of inputs, except the continuous input"
            ),
        ),
        InlinePanel(
            "continuous_values",
            heading="Continuous values",
            label="Continuous value",
            help_text=_("Fill in the options for the continuous input"),
            max_num=1,
        ),
    ]

    def __str__(self):
        name = self.name + ", " + dict(TYPE_CHOICES)[self.type]
        if self.type == CHOICE_SINGLESELECT or self.type == CHOICE_MULTISELECT:
            options = " (" + ", ".join([str(i) for i in self.options.all()]) + ")"
            name += options

        return name

    class Meta:
        verbose_name = "Interactive Input"


class InteractiveInputOptions(Orderable):
    input = ParentalKey(InteractiveInput, on_delete=models.CASCADE, related_name="options")
    option = models.CharField(max_length=255, help_text=_("Fill in your option"))
    label = models.CharField(
        max_length=255,
        help_text=_("Fill in the label that the user sees in a storyline"),
        null=True,
        blank=True,
    )
    default = models.BooleanField(
        null=True, blank=True, help_text=_("Should this option be default selected?")
    )
    legal_limitation = models.CharField(
        max_length=255,
        help_text=_("Fill in the status of the legal limitation"),
        null=True,
        blank=True,
    )
    color = models.CharField(
        max_length=10,
        choices=COLOR_CHOICES,
        null=True,
        blank=True,
    )

    link_wiki_page = models.ForeignKey(
        "main.WikiPage",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text=_("Use this to link to an internal page."),
    )

    content_panels = Page.content_panels + [
        PageChooserPanel("link_wiki_page"),
    ]

    def __str__(self):
        if self.label:
            return self.label
        else:
            return self.option


class InteractiveInputContinuousValues(models.Model):
    input = ParentalKey(
        InteractiveInput, on_delete=models.CASCADE, related_name="continuous_values"
    )
    slider_value_default = models.IntegerField(
        validators=[MinValueValidator(0)],
        blank=True,
        null=True,
        help_text=_("Default amount of the continuous input"),
    )
    slider_value_min = models.IntegerField(
        validators=[MinValueValidator(0)],
        blank=True,
        null=True,
        default=0,
        help_text=_("Minimum amount of the continuous input"),
    )
    slider_value_max = models.IntegerField(
        validators=[MinValueValidator(0)],
        blank=True,
        null=True,
        default=100,
        help_text=_("Maximum amount of the continuous input"),
    )

from django.utils.translation import gettext_lazy as _
from django.db import models
from django.core.validators import MinValueValidator
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.core.models import Orderable

# from django.core.validators import MinValueValidator
from wagtail.snippets.models import register_snippet

# Create your models here.
@register_snippet
class InteractiveInput(ClusterableModel):
    CHOICE_CHECKBOX = "checkbox"
    CHOICE_MULTIBUTTON = "multibutton"
    CHOICE_RADIOBUTTON = "radio"
    CHOICE_BUTTON = "button"
    CHOICE_CONTINUOUS = "continuous"
    TYPE_CHOICES = (
        (CHOICE_CHECKBOX, "Checkbox"),
        (CHOICE_MULTIBUTTON, "Multibutton"),
        (CHOICE_RADIOBUTTON, "Radiobutton"),
        (CHOICE_BUTTON, "Button"),
        (CHOICE_CONTINUOUS, "Continuous (slider)"),
    )

    name = models.CharField(max_length=100)
    type = models.CharField(
        max_length=12,
        choices=TYPE_CHOICES,
        default=CHOICE_CONTINUOUS,
    )

    panels = [
        FieldPanel("name"),
        FieldPanel("type"),
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
        return self.name

    class Meta:
        verbose_name = "Interactive Input"


class InteractiveInputOptions(Orderable):
    input = ParentalKey(InteractiveInput, on_delete=models.CASCADE, related_name="options")
    option = models.CharField(max_length=255, help_text=_("Fill in your option"))


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
        help_text=_("Minimum amount of the continuous input"),
    )
    slider_value_max = models.IntegerField(
        validators=[MinValueValidator(0)],
        blank=True,
        null=True,
        help_text=_("Maximum amount of the continuous input"),
    )

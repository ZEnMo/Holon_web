from django.utils.translation import gettext_lazy as _

from wagtail.core.blocks import StructBlock, CharBlock, ChoiceBlock, ListBlock
from .button import ButtonComponent
from .holon_image_chooser import HolonImageChooserBlock

COLOR_CHOICES = (
    ("card__bg-gold", "Gold"),
    ("card__bg-blue", "Blue"),
    ("card__bg-gray", "Gray"),
    ("card__bg-purple", "Purple"),
    ("card__bg-pink", "Pink"),
    ("card__bg-orange", "Orange"),
)


class CardComponent(StructBlock):
    title = CharBlock(required=False)
    image_selector = HolonImageChooserBlock()
    text = CharBlock(required=False)
    card_background = ChoiceBlock(
        choices=COLOR_CHOICES,
        required=False,
    )


class CardsBlock(StructBlock):
    """
    Custom block to include cards
    """

    cards = ListBlock(CardComponent())

    # button = ButtonComponent()

    class Meta:
        icon = "grip"

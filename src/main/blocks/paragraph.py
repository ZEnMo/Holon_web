""" Streamfields """
from wagtail.core import blocks
from main.blocks.rich_text_block import RichtextBlock
from .grid_chooser import GridChooserBlock
from .background_chooser import BackgroundChooserBlock


class ParagraphBlock(blocks.StructBlock):
    """Paragraph block"""

    grid_layout = GridChooserBlock(required=True)

    background = BackgroundChooserBlock()

    text = RichtextBlock(required=True, help_text="Add your text", rows=15)

    class Meta:  # NOQA
        icon = "text"
        label = "Paragraph"

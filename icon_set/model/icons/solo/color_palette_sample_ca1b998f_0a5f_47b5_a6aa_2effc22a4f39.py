'Upright palette: replace faceted perimeter with coherent curves and a smooth inward grip. Preserve asymmetric shape and original paint marks.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ca1b998f-0a5f-47b5-a6aa-2effc22a4f39'
SOURCE_PATH = 'pictographic-primitives/design/color palette sample_ca1b998f-0a5f-47b5-a6aa-2effc22a4f39.svg'
AUTHOR = 'gpt-6'

class ColorPaletteSample(Solo48):
    icon_id = 'color-palette-sample'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    categories = ('design', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('color', 'palette', 'sample', 'design')

    def build(self) -> None:
        # Upright asymmetric palette: shared tangent vectors at the top, side and grip.
        self.add_bezier('outline',(26,4),((34,4),(40,9),(40,17)),((40,24),(32,25),(32,32)),((32,39),(31,44),(24,44)),((14,44),(8,35),(8,25)),((8,15),(16,4),(26,4)))
        self.add_contour('body','outline',closed=True)
        self.add_line('paint-left',(19,21),(21,22))
        self.add_line('paint-top',(28,13),(28,17))
        self.add_line('paint-bottom',(19,33),(22,32))

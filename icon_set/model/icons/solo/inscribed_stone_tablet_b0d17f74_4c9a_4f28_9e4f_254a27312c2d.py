"""An inscribed stone slab with a broken upper left corner. VRECT_XL extremes (5,2)-(43,46). Retain three inscription rows, replace fine waves with broad strokes; fracture remains asymmetric."""

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b0d17f74-4c9a-4f28-9e4f-254a27312c2d'
SOURCE_PATH = 'pictographic-primitives/culture/batch-03/resetta stone_b0d17f74-4c9a-4f28-9e4f-254a27312c2d.svg'
AUTHOR = 'astra-chatgpt'


class InscribedStoneTablet(Solo48):
    icon_id = 'inscribed-stone-tablet'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "culture/objects"
    aliases = ()
    keywords = ('rosetta stone', 'tablet', 'inscription', 'hieroglyph', 'ancient', 'archaeology', 'stone', 'script')

    def build(self) -> None:
        self.add_line('fracture',(5,14),(21,2))
        self.add_line('top',(21,2),(37,2))
        self.add_arc('ne',(37,2),(43,8),radius_x=6)
        self.add_line('east',(43,8),(43,40))
        self.add_arc('se',(43,40),(37,46),radius_x=6)
        self.add_line('base',(37,46),(11,46))
        self.add_arc('sw',(11,46),(5,40),radius_x=6)
        self.add_line('west',(5,40),(5,14))
        self.add_contour('stone','fracture','top','ne','east','se','base','sw','west',closed=True)
        self.add_line('inscription-top',(16,18),(33,18))
        self.add_line('inscription-middle-left',(14,27),(20,27))
        self.add_line('inscription-middle-right',(28,27),(34,27))
        self.add_line('inscription-bottom',(14,36),(34,36))

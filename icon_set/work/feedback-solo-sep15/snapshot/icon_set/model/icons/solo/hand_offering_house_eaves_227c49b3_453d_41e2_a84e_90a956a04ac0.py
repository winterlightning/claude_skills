"""An open hand offers a house with short eaves. SQUARE extremes (6,6)-(42,42). Lucide hand-platter and house inform the coherent palm and mirrored roof. Preserve the eaves and rightward offering direction; omit door/window details absent from the source."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '227c49b3-453d-41e2-a84e-90a956a04ac0'
SOURCE_PATH = 'pictographic-primitives/symbol/give hand with house_227c49b3-453d-41e2-a84e-90a956a04ac0.svg'
AUTHOR = 'gpt-6'


class HandOfferingHouseEaves(Solo48):
    icon_id = 'hand-offering-house-eaves'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('hand', 'house', 'home', 'real-estate', 'property', 'care', 'mortgage', 'insurance')

    def build(self) -> None:
        self.add_line('hand-top',(6,30),(18,30))
        self.add_arc('thumb-top',(18,30),(22,34),radius_x=4)
        self.add_arc('thumb-bottom',(22,34),(18,38),radius_x=4)
        self.add_line('thumb-return',(18,38),(14,38))
        self.add_contour('thumb-stroke','hand-top','thumb-top','thumb-bottom','thumb-return')
        self.add_line('fingers-top',(22,34),(37,26))
        self.add_arc('fingertips',(37,26),(37,36),radius_x=5)
        self.add_line('fingers-bottom',(37,36),(30,40))
        self.add_arc('palm',(30,40),(18,40),radius_x=10)
        self.add_line('wrist-bottom',(18,40),(6,36))
        self.add_contour('hand','fingers-top','fingertips','fingers-bottom','palm','wrist-bottom')
        self.relate('connect','thumb-stroke','hand')
        self.add_polyline('house',(16,19),(16,12),(24,6),(32,12),(32,19),(16,19),closed=True)
        self.add_line('eave-left',(16,12),(13,15))
        self.add_line('eave-right',(32,12),(35,15))
        self.relate('connect','house','eave-left')
        self.relate('connect','house','eave-right')

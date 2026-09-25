"""An open hand offers a small house. SQUARE extremes (6,6)-(42,42). Lucide hand-platter informs the curled thumb and supporting palm; house informs the pitched roof. Omit unrequested door/window detail and preserve rightward offering direction."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '88de76fc-1b26-4dab-828b-a18a614b0df1'
SOURCE_PATH = 'pictographic-primitives/symbol/give hand house_88de76fc-1b26-4dab-828b-a18a614b0df1.svg'
AUTHOR = 'gpt-6'


class HandOfferingHouse(Solo48):
    icon_id = 'hand-offering-house'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    aliases = ()
    keywords = ('hand', 'house', 'home', 'real-estate', 'property', 'care', 'offer', 'insurance')

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

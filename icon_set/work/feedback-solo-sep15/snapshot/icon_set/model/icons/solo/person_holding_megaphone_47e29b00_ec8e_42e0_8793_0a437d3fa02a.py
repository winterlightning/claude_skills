"""Person raising a horn above their head. SQUARE extremes 6,6–42,42. Lucide megaphone informs flared horn; Lucide user-round informs head; omit sound rays to preserve held-object recognition."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '47e29b00-ec8e-42e0-8793-0a437d3fa02a'
SOURCE_PATH = 'pictographic-primitives/social/election campaign 3_47e29b00-ec8e-42e0-8793-0a437d3fa02a.svg'
AUTHOR = 'gpt-6'

class PersonHoldingMegaphone(Solo48):
    icon_id = 'person-holding-megaphone'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/social"
    aliases = ()
    keywords = ('person', 'megaphone', 'campaign', 'speaker', 'announcement', 'rally')

    def build(self):
        self.add_arc('head-top', (7,23), (17,23), radius_x=5)
        self.add_arc('head-bottom', (17,23), (7,23), radius_x=5)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_arc('body-shoulder', (6,42), (15,36), radius_x=9, radius_y=6)
        self.add_line('body-base', (15,36), (21,36))
        self.add_arc('arm-bend', (21,36), (30,27), radius_x=9, sweep=False)
        self.add_line('hand', (30,27), (28,21))
        self.add_contour('body', 'body-shoulder','body-base','arm-bend','hand')
        self.add_polyline('megaphone', (25,14), (32,6), (42,24), (28,21), (25,22), (25,14))
        self.relate('connect','body','megaphone')

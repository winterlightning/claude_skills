"""Uncuffed raised thumb with one readable finger crease. SQUARE centerlines 6,6–42,42. Lucide thumbs-up informs palm and hooked thumb; reduce three creases to one."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'fc83794c-c4dc-4f7e-884b-9c85a97943ce'
SOURCE_PATH = 'pictographic-primitives/social/like_fc83794c-c4dc-4f7e-884b-9c85a97943ce.svg'
AUTHOR = 'gpt-6'

class CurledFingerThumbsUp(Solo48):
    icon_id = 'curled-finger-thumbs-up'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/social"
    aliases = ()
    keywords = ('hand', 'thumb', 'like', 'approval', 'gesture', 'wrist')

    def build(self):
        self.add_line('wrist-top',(6,24),(14,24))
        self.add_arc('thumb-rise',(14,24),(24,14),radius_x=10,sweep=False)
        self.add_line('thumb-tip',(24,14),(24,6))
        self.add_arc('thumb-round',(24,6),(32,14),radius_x=8)
        self.add_line('thumb-inner',(32,14),(29,24))
        self.add_line('finger-top',(29,24),(38,24))
        self.add_arc('finger-round',(38,24),(42,28),radius_x=4)
        self.add_line('finger-upper',(42,28),(42,33))
        self.add_line('finger-lower',(42,33),(42,38))
        self.add_arc('palm-round',(42,38),(38,42),radius_x=4)
        self.add_line('palm-bottom',(38,42),(6,42))
        self.add_line('wrist',(6,42),(6,24))
        self.add_contour('hand','wrist-top','thumb-rise','thumb-tip','thumb-round','thumb-inner','finger-top','finger-round','finger-upper','finger-lower','palm-round','palm-bottom','wrist',closed=True)
        self.add_line('finger-crease',(42,33),(33,33))
        self.relate('connect','hand','finger-crease')

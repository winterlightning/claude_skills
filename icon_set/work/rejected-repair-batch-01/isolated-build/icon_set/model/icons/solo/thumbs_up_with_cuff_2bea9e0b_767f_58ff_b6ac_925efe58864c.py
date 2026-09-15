"""Raised thumb and curled palm. SQUARE extremes 6,6–42,42. Lucide thumbs-up informs single thumb/palm outline and attached cuff; omit crowded finger creases; rays version retains one clear ray."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2bea9e0b-767f-58ff-b6ac-925efe58864c'
SOURCE_PATH = 'pictographic-primitives/social/like_2bea9e0b-767f-58ff-b6ac-925efe58864c.svg'
AUTHOR = 'gpt-6'

class ThumbsUpWithCuff(Solo48):
    icon_id = 'thumbs-up-with-cuff'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/social"
    aliases = ()
    keywords = ('hand', 'thumb', 'like', 'approval', 'gesture', 'cuff')

    def build(self):
        self.add_line('wrist-top', (6,24), (14,24))
        self.add_line('thumb-rise', (14,24), (24,14))
        self.add_line('thumb-tip-rise', (24,14), (24,6))
        self.add_arc('thumb-round', (24,6), (32,14), radius_x=8)
        self.add_line('thumb-inner', (32,14), (29,24))
        self.add_line('fingers-top', (29,24), (38,24))
        self.add_arc('fingers-round-top', (38,24), (42,28), radius_x=4)
        self.add_line('fingers-side', (42,28), (42,38))
        self.add_arc('fingers-round-bottom', (42,38), (38,42), radius_x=4)
        self.add_line('palm-bottom', (38,42), (14,42))
        self.add_line('wrist-bottom', (14,42), (6,42))
        self.add_line('wrist-side', (6,42), (6,24))
        self.add_contour('hand', 'wrist-top','thumb-rise','thumb-tip-rise','thumb-round','thumb-inner','fingers-top','fingers-round-top','fingers-side','fingers-round-bottom','palm-bottom','wrist-bottom','wrist-side',closed=True)
        self.add_line('cuff', (14,24), (14,42))
        self.relate('connect','hand','cuff')

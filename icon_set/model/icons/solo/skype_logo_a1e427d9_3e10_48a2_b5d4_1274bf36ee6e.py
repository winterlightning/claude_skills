"""Soft square bubble and a centered rounded S. Preserve subtle corner mass through large equal radii; use one letter stroke rather than a heavy outline."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a1e427d9-3e10-48a2-b5d4-1274bf36ee6e'
SOURCE_PATH = 'pictographic-primitives/logos/skype logo_a1e427d9-3e10-48a2-b5d4-1274bf36ee6e.svg'
AUTHOR = 'gpt-6'

class SkypeLogo(Solo48):
    icon_id = 'skype-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('skype', 'microsoft', 'video-call', 'letter-s', 'logo', 'brand', 'chat')

    def build(self):
        # Plan: Soft square bubble and a centered rounded S. Preserve subtle corner mass through large equal radii; use one letter stroke rather than a heavy outline.
        # Exact keyshape ink extremes are owned by Keyshape.SQUARE on SOLO48.

        self.add_line('top',(20,6),(28,6))
        self.add_arc('tr',(28,6),(42,20),radius_x=14)
        self.add_line('right',(42,20),(42,28))
        self.add_arc('br',(42,28),(28,42),radius_x=14)
        self.add_line('bottom',(28,42),(20,42))
        self.add_arc('bl',(20,42),(6,28),radius_x=14)
        self.add_line('left',(6,28),(6,20))
        self.add_arc('tl',(6,20),(20,6),radius_x=14)
        self.add_contour('bubble','top','tr','right','br','bottom','bl','left','tl',closed=True)
        self.add_bezier('s',(30,18),((30,13),(18,13),(18,20)),((18,24),(30,24),(30,28)),((30,35),(18,35),(18,30)))


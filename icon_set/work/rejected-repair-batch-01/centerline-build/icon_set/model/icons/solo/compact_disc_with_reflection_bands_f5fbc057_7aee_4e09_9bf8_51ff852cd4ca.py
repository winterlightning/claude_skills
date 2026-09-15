"""Concentric disc and spindle hole. Two opposite reflection strokes share a rotational pair. Omit crowded intermediate hub ring and doubled bands. Radius 20 about (24,24); Lucide disc concentric loops."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f5fbc057-7aee-4e09-9bf8-51ff852cd4ca'
SOURCE_PATH = 'pictographic-primitives/music/cd playing_f5fbc057-7aee-4e09-9bf8-51ff852cd4ca.svg'
AUTHOR = 'gpt-6'

class CompactDiscWithReflectionBands(Solo48):
    icon_id = 'compact-disc-with-reflection-bands'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/music"
    aliases = ()
    keywords = ('cd', 'compact-disc', 'disc', 'music', 'playing', 'media', 'audio', 'album')

    def build(self):
        self.add_arc('disc-left',(24,4),(24,44),radius_x=20,sweep=False)
        self.add_arc('disc-right',(24,44),(24,4),radius_x=20,sweep=False)
        self.add_contour('disc','disc-left','disc-right',closed=True)
        cx, cy, radius = 24, 24, 3
        points = ((cx-radius,cy),(cx,cy-radius),(cx+radius,cy),(cx,cy+radius))
        for n in range(4):
            self.add_arc(f'spindle-{n}',points[n],points[(n+1)%4],radius_x=radius)
        self.add_contour('spindle', *[f'spindle-{n}' for n in range(4)], closed=True)
        self.add_line('reflection-upper',(24,4),(24,12))
        self.add_line('reflection-lower',(24,36),(24,44))
        self.relate('connect','reflection-upper','disc')
        self.relate('connect','reflection-lower','disc')

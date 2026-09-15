"""A rear figure pushes a shield-bearing figure facing left. Lucide person-standing informs circle heads and single-stroke limbs. Omit visor and doubled limbs; preserve the two-person action and upright shield. Deliberate leftward asymmetry."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3d641c7a-d705-4875-af71-ef2fe9826b56'
SOURCE_PATH = 'pictographic-primitives/protection/protest police shield_3d641c7a-d705-4875-af71-ef2fe9826b56.svg'
AUTHOR = 'gpt-6'


class ProtectionIcon(Solo48):
    icon_id = 'figure-pushing-shield-bearer'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/protection"
    aliases = ()
    keywords = ('protest', 'police', 'riot', 'shield', 'push', 'clash', 'figures', 'conflict')

    def build(self):
        # SQUARE centerline extremes (6, 6, 42, 42).

        # Two figures share a push contact; left figure owns an upright shield.
        for n,x in [('front',16),('rear',34)]:
            self.add_arc(n+'-head-top',(x-3,9),(x+3,9),radius_x=3)
            self.add_arc(n+'-head-bottom',(x+3,9),(x-3,9),radius_x=3)
            self.add_contour(n+'-head',n+'-head-top',n+'-head-bottom',closed=True)
            self.add_line(n+'-body',((30 if n == 'rear' else x),21),(x,30))
        self.add_polyline('front-legs',(8,42),(16,30),(24,42))
        self.add_polyline('rear-legs',(32,42),(34,30),(42,42))
        self.relate('connect','front-body','front-legs')
        self.relate('connect','rear-body','rear-legs')
        self.add_line('push',(16,21),(30,21))
        self.relate('connect','push','front-body')
        self.relate('connect','push','rear-body')
        self.add_polyline('shield',(6,16),(6,24),(6,34))
        self.add_polyline('front-arm',(6,24),(16,21))
        self.relate('connect','front-arm','shield')
        self.relate('connect','front-arm','front-body')
        self.relate('connect','front-arm','push')

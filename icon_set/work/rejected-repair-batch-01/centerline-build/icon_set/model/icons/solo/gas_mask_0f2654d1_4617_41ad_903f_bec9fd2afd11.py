"""A gas mask has two circular lenses and a round bottom filter. No useful exact Lucide match; use paired circles and a smooth face contour. Omit filter perspective depth."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0f2654d1-4617-41ad-903f-bec9fd2afd11'
SOURCE_PATH = 'pictographic-primitives/protection/mask_0f2654d1-4617-41ad-903f-bec9fd2afd11.svg'
AUTHOR = 'gpt-6'


class ProtectionIcon(Solo48):
    icon_id = 'gas-mask'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/protection"
    aliases = ()
    keywords = ('gas mask', 'respirator', 'mask', 'filter', 'toxic', 'protection', 'chemical', 'safety')

    def build(self):
        # SQUARE centerline extremes: (6,6)-(42,42).

        # Face and round filter share physical attachment points.
        self.add_arc('head-top',(6,20),(42,20),radius_x=18,radius_y=14)
        self.add_line('face-right',(42,20),(42,24))
        self.add_arc('jaw-right',(42,24),(30,36),radius_x=12)
        self.add_arc('jaw-left',(18,36),(6,24),radius_x=12)
        self.add_line('face-left',(6,24),(6,20))
        self.add_contour('face','jaw-left','face-left','head-top','face-right','jaw-right')
        for side,cx in [('left',17),('right',31)]:
            self.add_arc(side+'-top',(cx-2,20),(cx+2,20),radius_x=2)
            self.add_arc(side+'-bottom',(cx+2,20),(cx-2,20),radius_x=2)
            self.add_contour('eye-'+side,side+'-top',side+'-bottom',closed=True)
        self.add_arc('filter-top',(18,36),(30,36),radius_x=6)
        self.add_arc('filter-bottom',(30,36),(18,36),radius_x=6)
        self.add_contour('filter','filter-top','filter-bottom',closed=True)
        self.relate('connect','filter','face')

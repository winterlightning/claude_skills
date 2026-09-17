"""Round Pill Blister Pack.

Plan: Rounded pack owns a mirrored two-by-two pocket series. Drop seam and one row for clearance. Bounds (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2b0dcbd3-e258-56e3-8580-8f6e36094db4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/contraceptive pills panel_2b0dcbd3-e258-56e3-8580-8f6e36094db4.svg'
AUTHOR = 'gpt-6'


class RoundPillBlisterPack(Solo48):
    icon_id = 'round-pill-blister-pack'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/health'
    aliases = ()
    keywords = ('round', 'pill', 'blister', 'pack')

    def build(self):
        self.add_line('pack-top', (12,6),(36,6))
        self.add_arc('pack-tr',(36,6),(42,12),radius_x=6)
        self.add_line('pack-right',(42,12),(42,36))
        self.add_arc('pack-br',(42,36),(36,42),radius_x=6)
        self.add_line('pack-bottom',(36,42),(12,42))
        self.add_arc('pack-bl',(12,42),(6,36),radius_x=6)
        self.add_line('pack-left',(6,36),(6,12))
        self.add_arc('pack-tl',(6,12),(12,6),radius_x=6)
        self.add_contour('pack','pack-top','pack-tr','pack-right','pack-br','pack-bottom','pack-bl','pack-left','pack-tl',closed=True)
        for col in range(2):
            for row in range(2):
                x,y=17+14*col,17+14*row
                p=f'pill-{col}-{row}'
                self.add_arc(p+'-top',(x-2,y),(x+2,y),radius_x=2)
                self.add_arc(p+'-bottom',(x+2,y),(x-2,y),radius_x=2)
                self.add_contour(p,p+'-top',p+'-bottom',closed=True)

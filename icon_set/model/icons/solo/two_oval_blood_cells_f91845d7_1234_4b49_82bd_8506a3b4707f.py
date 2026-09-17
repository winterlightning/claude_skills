"""Two Oval Blood Cells.

Plan: Two unequal ovals arranged diagonally. Preserve simple cell grouping; upright ovals replace rotated source contours. Bounds (6,6)-(42,42). No useful Lucide direct match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f91845d7-1234-4b49-82bd-8506a3b4707f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/red blood cell good_f91845d7-1234-4b49-82bd-8506a3b4707f.svg'
AUTHOR = 'gpt-6'


class TwoOvalBloodCells(Solo48):
    icon_id = 'two-oval-blood-cells'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/health'
    aliases = ()
    keywords = ('two', 'oval', 'blood', 'cells')

    def build(self):
        for p,x,y,rx,ry in [('small', 14, 12, 8, 6), ('large', 30, 32, 12, 10)]:
            self.add_arc(p+'-top',(x-rx,y),(x+rx,y),radius_x=rx,radius_y=ry)
            self.add_arc(p+'-bottom',(x+rx,y),(x-rx,y),radius_x=rx,radius_y=ry)
            self.add_contour(p,p+'-top',p+'-bottom',closed=True)

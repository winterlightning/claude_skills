"""Two Red Blood Cells.

Plan: Two unequal ovals arranged diagonally. Preserve simple cell grouping; upright ovals replace rotated source contours. Bounds (6,6)-(42,42). No useful Lucide direct match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '27792980-efeb-455e-94ef-6dc2924206c1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/red blood cell two_27792980-efeb-455e-94ef-6dc2924206c1.svg'
AUTHOR = 'gpt-6'


class TwoRedBloodCells(Solo48):
    icon_id = 'two-red-blood-cells'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/health'
    aliases = ()
    keywords = ('two', 'red', 'blood', 'cells')

    def build(self):
        for p,x,y,rx,ry in [('small', 34, 12, 8, 6), ('large', 18, 32, 12, 10)]:
            self.add_arc(p+'-top',(x-rx,y),(x+rx,y),radius_x=rx,radius_y=ry)
            self.add_arc(p+'-bottom',(x+rx,y),(x-rx,y),radius_x=rx,radius_y=ry)
            self.add_contour(p,p+'-top',p+'-bottom',closed=True)
        self.add_line('depression',(16,32),(20,32))

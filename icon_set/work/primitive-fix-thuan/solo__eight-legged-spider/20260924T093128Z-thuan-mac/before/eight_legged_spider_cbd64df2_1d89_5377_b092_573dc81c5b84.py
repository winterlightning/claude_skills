"""Eight Legged Spider.

Plan: Eight jointed legs spread from a rounded two-part body. Shared side nodes, four legs per side, equal pitch and mirrored reach. Lucide bug informs body/leg joins. Bounds (4,8)-(44,40).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cbd64df2-1d89-5377-b092-573dc81c5b84'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/halloween spider_cbd64df2-1d89-5377-b092-573dc81c5b84.svg'
AUTHOR = 'gpt-6'

class EightLeggedSpider(Solo48):
    icon_id = 'eight-legged-spider'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/holidays"
    aliases = ()
    keywords = ('eight', 'legged', 'spider')

    def build(self):
        self.add_polyline('body-left',(16,16),(16,24),(16,32))
        self.add_arc('body-bottom',(16,32),(32,32),radius_x=8,sweep=False)
        self.add_polyline('body-right',(32,32),(32,24),(32,16))
        self.add_arc('body-top',(32,16),(16,16),radius_x=8,sweep=False)
        self.add_contour('body','body-left-1','body-left-2','body-bottom','body-right-1','body-right-2','body-top',closed=True)
        self.contours=[c for c in self.contours if c.contour_id not in ['body-left','body-right']]
        self.add_line('waist',(16,24),(32,24));self.relate('connect','body','waist')
        for side in [-1,1]:
         def p(x,y):return (24+side*x,y)
         n='left' if side<0 else 'right'
         for j,pts in enumerate([[p(8,16),p(16,8),p(20,8)],[p(8,16),p(20,16)],[p(8,32),p(20,32)],[p(8,32),p(16,40),p(20,40)]]):
          self.add_polyline(f'{n}-{j}',*pts);self.relate('connect','body',f'{n}-{j}')
         self.relate('connect',f'{n}-0',f'{n}-1');self.relate('connect',f'{n}-2',f'{n}-3')

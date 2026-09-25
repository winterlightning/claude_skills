"""Circular Adjustment Knob.
Plan: Concentric outer adjustment arc and knob, with an upper-right indicator. Radial visible envelope22.
Reference construction: rotate-ccw.
Reduction: Reduce the indicator to a dot and omit end ticks to keep three levels legible.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ca7a77eb-2106-47f3-8db1-90341d67e333'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/volume up_ca7a77eb-2106-47f3-8db1-90341d67e333.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'circular-adjustment-knob'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('circular', 'adjustment', 'knob')
    def build(self):

        def circle(name,cx,cy,r):
            pts=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
            for j,(a,b) in enumerate(zip(pts,pts[1:])):
                self.add_arc(f'{name}-{j}',a,b,radius_x=r)
            self.add_contour(name,*(f'{name}-{j}' for j in range(4)),closed=True)

        self.add_arc('adjustment-arc',(12,40),(44,24),radius_x=20,large_arc=True)
        circle('knob',24,24,11)
        self.add_dot('indicator',(26,22))

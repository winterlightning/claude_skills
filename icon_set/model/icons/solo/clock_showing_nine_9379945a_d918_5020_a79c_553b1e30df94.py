"""Clock Showing Nine.
Plan: Circular clock face with a single joined right-angle pair of hands at nine. Radial envelope22.
Reference construction: clock.
Reduction: Omit the two short hour ticks to maintain dial-to-hand clearance.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9379945a-d918-5020-a79c-553b1e30df94'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/time clock nine to twelve_9379945a-d918-5020-a79c-553b1e30df94.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'clock-showing-nine'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    aliases = ()
    keywords = ('clock', 'showing', 'nine')
    def build(self):

        def circle(name,cx,cy,r):
            pts=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
            for j,(a,b) in enumerate(zip(pts,pts[1:])):
                self.add_arc(f'{name}-{j}',a,b,radius_x=r)
            self.add_contour(name,*(f'{name}-{j}' for j in range(4)),closed=True)

        circle('face',24,24,20)
        self.add_polyline('hands',(14,24),(24,24),(24,14))

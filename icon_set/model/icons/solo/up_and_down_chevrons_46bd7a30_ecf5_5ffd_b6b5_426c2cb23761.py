"""Up and Down Chevrons — batch 52."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '46bd7a30-ecf5-5ffd-b6b5-426c2cb23761'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/scroll vertical_46bd7a30-ecf5-5ffd-b6b5-426c2cb23761.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'up-and-down-chevrons'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    aliases = ()
    keywords = ('up', 'and', 'down', 'chevrons')

    def build(self):
        # Plan: matched outward chevrons from a shared axis; broad central negative space.
        # VRECT_L extremes8,4,40,44. Lucide chevrons-up-down supplies open mirrored angles.
        for n,y,s in [('upper',4,1),('lower',44,-1)]:self.add_polyline(n,(8,y+s*12),(24,y),(40,y+s*12))


    def circle(self,n,x,y,r):
        pts=[(x+r,y),(x,y+r),(x-r,y),(x,y-r)]
        for j in range(4):self.add_arc(f'{n}-{j}',pts[j],pts[(j+1)%4],radius_x=r)
        self.add_contour(n,*[f'{n}-{j}' for j in range(4)],closed=True)


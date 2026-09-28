"""Vertical Double Arrow — batch 52."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '962de709-e4bd-471c-8cd4-d9c471b6ef01'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/expand vertical 3_962de709-e4bd-471c-8cd4-d9c471b6ef01.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'vertical-double-arrow-962de709-e4bd-471c-8cd4-d9c471b6ef01'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    categories = ("interface-essential", "primitives")
    aliases = ()
    keywords = ('vertical', 'double', 'arrow')

    def build(self):
        # Plan: single vertical shaft with equal outward heads mirrored about canvas center.
        # VRECT_M extremes10,4,38,44. Lucide move-vertical supplies shared head junctions.
        self.add_line('shaft',(24,4),(24,44))
        for n,y,s in [('upper',4,1),('lower',44,-1)]:
            self.add_polyline(n,(10,y+s*14),(24,y),(38,y+s*14));self.relate('connect','shaft',n)


    def circle(self,n,x,y,r):
        pts=[(x+r,y),(x,y+r),(x-r,y),(x,y-r)]
        for j in range(4):self.add_arc(f'{n}-{j}',pts[j],pts[(j+1)%4],radius_x=r)
        self.add_contour(n,*[f'{n}-{j}' for j in range(4)],closed=True)


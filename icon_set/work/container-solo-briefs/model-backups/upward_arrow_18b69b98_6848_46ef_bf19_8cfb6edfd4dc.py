"""Upward Arrow — batch 52."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '18b69b98-6848-46ef-bf19-8cfb6edfd4dc'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/keyboard arrow up_18b69b98-6848-46ef-bf19-8cfb6edfd4dc.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'upward-arrow'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    aliases = ()
    keywords = ('upward', 'arrow')

    def build(self):
        # Plan: one upright shaft with mirrored open head.
        # VRECT_M extremes10,4,38,44. Lucide arrow-up supplies a single shared junction.
        self.add_polyline('head',(10,18),(24,4),(38,18))
        self.add_line('shaft',(24,4),(24,44));self.relate('connect','shaft','head')


    def circle(self,n,x,y,r):
        pts=[(x+r,y),(x,y+r),(x-r,y),(x,y-r)]
        for j in range(4):self.add_arc(f'{n}-{j}',pts[j],pts[(j+1)%4],radius_x=r)
        self.add_contour(n,*[f'{n}-{j}' for j in range(4)],closed=True)


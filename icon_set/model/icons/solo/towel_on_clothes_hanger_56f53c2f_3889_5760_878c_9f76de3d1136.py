"""Towel on Clothes Hanger.
Plan: A compact hook joins a tall triangular hanger; a narrow towel hangs from its base. Ink (6,2)-(42,46).
Construction reference: shopping-cart.
Reduction: Narrow the hanging towel and omit its hem stripe to preserve hanger clearance.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '56f53c2f-3889-5760-878c-9f76de3d1136'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/hotels/bathroom hanger_56f53c2f-3889-5760-878c-9f76de3d1136.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'towel-on-clothes-hanger'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'hotels'
    aliases = ()
    keywords = ('towel', 'on', 'clothes', 'hanger')
    def build(self):

        def circle(name, cx, cy, r):
            self.add_arc(name+'-top', (cx-r,cy), (cx+r,cy), radius_x=r)
            self.add_arc(name+'-bottom', (cx+r,cy), (cx-r,cy), radius_x=r)
            self.add_contour(name,name+'-top',name+'-bottom',closed=True)
        def rect(name,x,y,w,h,r=2):
            pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r),(x+r,y)]
            for i,(a,b) in enumerate(zip(pts,pts[1:])):
                if i%2: self.add_arc(f'{name}-{i}',a,b,radius_x=r)
                else: self.add_line(f'{name}-{i}',a,b)
            self.add_contour(name,*(f'{name}-{i}' for i in range(8)),closed=True)

        self.add_arc('hook',(20,8),(28,8),radius_x=4)
        self.add_arc('hook-return',(28,8),(24,12),radius_x=4)
        self.add_contour('hook-stem','hook','hook-return')
        self.add_polyline('hanger',(19,30),(8,30),(24,12),(40,30),(29,30))
        self.relate('connect','hook-stem','hanger')
        self.add_polyline('towel',(19,30),(29,30),(29,44),(19,44),closed=True)
        self.relate('connect','hanger','towel')

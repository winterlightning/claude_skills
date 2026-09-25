"""A broad platform and double-crossed linkage; platform lip simplified for open spacing."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '75ec04e6-a5ce-5605-943f-f10814622f82'
SOURCE_PATH = 'pictographic-primitives/tools/clamps expand_75ec04e6-a5ce-5605-943f-f10814622f82.svg'
AUTHOR = 'gpt-6'

class ScissorJackStand(Solo48):
    icon_id = 'scissor-jack-stand'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "tools"
    aliases = ()
    keywords = ('scissor jack', 'jack', 'lift', 'stand', 'expand', 'platform', 'raise', 'clamp')

    def build(self) -> None:

        def box(n,x,y,w,h,r=0):
            if not r:
                self.add_polyline(n,(x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True)
                return
            pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
            for j in range(8):
                a,b=pts[j],pts[(j+1)%8]
                if j%2:self.add_arc(n+str(j),a,b,radius_x=r)
                else:self.add_line(n+str(j),a,b)
            self.add_contour(n,*[n+str(j) for j in range(8)],closed=True)

        box('platform',6,6,36,8,0)
        self.add_polyline('leg-left',(10,14),(34,28),(10,42))
        self.add_polyline('leg-right',(38,14),(14,28),(38,42))
        self.relate('connect','leg-left','leg-right')
        self.relate('connect','platform','leg-left')
        self.relate('connect','platform','leg-right')
        self.add_line('base',(6,42),(42,42))
        self.relate('connect','base','leg-left')
        self.relate('connect','base','leg-right')

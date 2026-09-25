"""A rectangular finishing float with offset neck and rounded hand grip; minor plate edge omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ad41eb23-04c0-48dd-ae6c-e2149735dfb2'
SOURCE_PATH = 'pictographic-primitives/tools/tools flattener square_ad41eb23-04c0-48dd-ae6c-e2149735dfb2.svg'
AUTHOR = 'gpt-6'

class FloatTrowel(Solo48):
    icon_id = 'float-trowel'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "tools"
    categories = ("primitives", "tools")
    aliases = ()
    keywords = ('trowel', 'float', 'plaster', 'flattener', 'masonry', 'concrete', 'construction', 'tool')

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

        box('grip',6,6,20,10,5)
        self.add_polyline('neck',(26,11),(32,16),(26,22),(26,30))
        self.relate('connect','neck','grip')
        self.add_polyline('plate',(26,22),(42,32),(30,42),(14,30),closed=True)
        self.relate('connect','neck','plate')

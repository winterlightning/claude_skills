"""A triangular pointing trowel with bent neck and rounded grip; tiny grip seams omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8a5c4bf7-50ed-4fe0-9a02-e101aedf445b'
SOURCE_PATH = 'pictographic-primitives/tools/tools flattener triangle_8a5c4bf7-50ed-4fe0-9a02-e101aedf445b.svg'
AUTHOR = 'gpt-6'

class PointingTrowel(Solo48):
    icon_id = 'pointing-trowel'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "tools"
    aliases = ()
    keywords = ('trowel', 'pointing trowel', 'masonry', 'mortar', 'brick', 'flattener', 'construction', 'tool')

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
        self.add_polyline('neck',(26,11),(22,22),(28,28))
        self.relate('connect','neck','grip')
        self.add_polyline('blade',(22,22),(42,42),(14,36),closed=True)
        self.relate('connect','neck','blade')

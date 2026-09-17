"""Wine Dining Table for Two.

Symbol plan: Mirrored chairs frame a pedestal wine table; one goblet retains dining identity; omit bottle.
Keyshape HRECT_L: visible ink extremes (2, 6, 46, 42); stroke centerlines inset 2.
Lucide construction reference: wine.
Source is visual subject evidence; geometry is freshly authored at 48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9da1fa5e-7a09-471e-8413-9fc362816283'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/drinks/wine restaurant_9da1fa5e-7a09-471e-8413-9fc362816283.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'small-wine-table-between-two-chairs'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/drink"
    aliases = ()
    keywords = ('wine', 'table', 'chairs', 'dining', 'bottle', 'glass', 'furniture', 'restaurant')

    def build(self):

        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*pts,closed=False): self.add_polyline(n,*pts,closed=closed)
        def arc(n,a,b,rx,ry=None,sweep=True):
            self.add_arc(n,a,b,radius_x=rx,radius_y=ry,sweep=sweep)
        def contour(n,*parts,closed=False):
            self.contours[:] = [c for c in self.contours if not set(c.members) & set(parts)]
            self.add_contour(n,*parts,closed=closed)
        def rect(n,x,y,w,h,r=0):
            if not r:
                poly(n,(x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True)
                return
            pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
            for i in range(8):
                a,b=pts[i],pts[(i+1)%8]
                if i%2: arc(n+str(i),a,b,r)
                else: line(n+str(i),a,b)
            contour(n,*(n+str(i) for i in range(8)),closed=True)
        for side in (-1,1):
         x=lambda u:24+side*u
         poly('chair'+str(side),(x(20),16),(x(18),30),(x(10),30),(x(10),40))
         line('leg'+str(side),(x(18),30),(x(20),40))
        poly('table',(14,22),(24,22),(34,22))
        line('pedestal',(24,22),(24,40))
        poly('foot',(22,40),(24,40),(26,40))
        poly('goblet',(20,8),(20,12),(24,16),(28,12),(28,8))
        line('stem',(24,16),(24,22))
        # Only true shared endpoints are physical connections. No proximity exemptions.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end} & {b.start,b.end}:
                    self.relate("connect",a.element_id,b.element_id)

"""Whiskey glass with ice cubes.

Symbol plan: Tapered tumbler; one tilted ice cube replaces three crowded cubes; a separate liquid line crosses the glass.
Keyshape SQUARE: visible ink extremes (4, 4, 44, 44); stroke centerlines inset 2.
Lucide construction reference: glass-water.
Source is visual subject evidence; geometry is freshly authored at 48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3ea71fda-2029-48a0-8232-ac104f668d31'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/drinks/drink whiskey_3ea71fda-2029-48a0-8232-ac104f668d31.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'whiskey-tumbler-with-three-unequal-ice-cubes'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/drink"
    aliases = ()
    keywords = ('whiskey', 'glass', 'ice', 'cubes', 'tumbler', 'drink', 'liquor', 'beverage')

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
        poly('glass',(6,6),(42,6),(41,14),(38,42),(10,42),(7,14),closed=True)
        line('liquid',(7,14),(41,14))
        poly('ice',(24,22),(30,28),(24,34),(18,28),closed=True)
        # Only true shared endpoints are physical connections. No proximity exemptions.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end} & {b.start,b.end}:
                    self.relate("connect",a.element_id,b.element_id)

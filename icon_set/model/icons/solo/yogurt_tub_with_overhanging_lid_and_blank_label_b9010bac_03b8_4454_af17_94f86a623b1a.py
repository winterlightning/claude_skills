"""Yogurt Cup Container.

Symbol plan: Symmetric yogurt tub with overhanging lid and a blank label; lid lip reduced to a single rim.
Keyshape HRECT_L: visible ink extremes (2, 6, 46, 42); stroke centerlines inset 2.
Lucide construction reference: bottle-wine.
Source is visual subject evidence; geometry is freshly authored at 48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b9010bac-03b8-4454-af17-94f86a623b1a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/drinks/snow family_b9010bac-03b8-4454-af17-94f86a623b1a.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'yogurt-tub-with-overhanging-lid-and-blank-label'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/drink"
    aliases = ()
    keywords = ('yogurt', 'tub', 'cup', 'lid', 'label', 'dairy', 'food', 'package')

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
        poly('lid',(4,8),(8,8),(40,8),(44,8))
        poly('body',(8,8),(8,36),(12,40),(36,40),(40,36),(40,8))
        rect('label',17,20,14,10,2)
        # Only true shared endpoints are physical connections. No proximity exemptions.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end} & {b.start,b.end}:
                    self.relate("connect",a.element_id,b.element_id)

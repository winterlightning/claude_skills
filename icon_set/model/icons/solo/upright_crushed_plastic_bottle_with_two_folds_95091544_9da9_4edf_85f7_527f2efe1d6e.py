"""Crushed Plastic Bottle.

Symbol plan: Upright bottle with broad cap, asymmetric body dents and two entering fold lines.
Keyshape VRECT_M: visible ink extremes (8, 2, 40, 46); stroke centerlines inset 2.
Lucide construction reference: bottle-wine.
Source is visual subject evidence; geometry is freshly authored at 48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '95091544-9da9-4edf-85f7-527f2efe1d6e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/ecology/compressed plastic bottle_95091544-9da9-4edf-85f7-527f2efe1d6e.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'upright-crushed-plastic-bottle-with-two-folds'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "ecology"
    aliases = ()
    keywords = ('bottle', 'plastic', 'crushed', 'folds', 'waste', 'recycling', 'cap', 'ecology')

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
        poly('outline',(18,4),(30,4),(30,12),(38,23),(34,33),(38,40),(34,44),(14,44),(10,40),(14,29),(10,22),(18,12),closed=True)
        line('cap',(18,12),(30,12))
        line('fold-left',(14,29),(24,25))
        line('fold-right',(34,33),(24,35))
        # Only true shared endpoints are physical connections. No proximity exemptions.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end} & {b.start,b.end}:
                    self.relate("connect",a.element_id,b.element_id)

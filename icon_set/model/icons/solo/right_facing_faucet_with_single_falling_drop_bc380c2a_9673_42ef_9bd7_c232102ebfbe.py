"""Dripping Water Faucet.

Symbol plan: Faucet with T handle, broad outlet, and one symmetric circular-ended falling drop.
Keyshape SQUARE: visible ink extremes (4, 4, 44, 44); stroke centerlines inset 2.
Lucide construction reference: no useful local match.
Source is visual subject evidence; geometry is freshly authored at 48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bc380c2a-9673-42ef-9bd7-c232102ebfbe'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/ecology/water protection faucet_bc380c2a-9673-42ef-9bd7-c232102ebfbe.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'right-facing-faucet-with-single-falling-drop'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/ecology"
    aliases = ()
    keywords = ('faucet', 'tap', 'water', 'drop', 'drip', 'plumbing', 'leak', 'ecology')

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
        poly('handle',(12,6),(22,6),(30,6))
        line('shaft',(22,6),(22,14))
        poly('top',(6,14),(22,14),(32,14))
        arc('spout',(32,14),(42,24),10)
        poly('bottom',(42,24),(32,24),(6,24))
        poly('drop',(38,33),(42,38))
        arc('drop-end',(42,38),(34,38),4)
        line('drop-side',(34,38),(38,33))
        contour('droplet','drop-1','drop-end','drop-side',closed=True)
        # Only true shared endpoints are physical connections. No proximity exemptions.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end} & {b.start,b.end}:
                    self.relate("connect",a.element_id,b.element_id)

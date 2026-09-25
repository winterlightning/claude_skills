"""Crushed Tin Can.

Symbol plan: Can with an elliptical top and asymmetric buckled walls; omit the tiny opening mark.
Keyshape VRECT_L: visible ink extremes (6, 2, 42, 46); stroke centerlines inset 2.
Lucide construction reference: no useful local match.
Source is visual subject evidence; geometry is freshly authored at 48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4910b875-813e-589a-81b7-c04f29759b82'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/ecology/compressed tin can_4910b875-813e-589a-81b7-c04f29759b82.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'crushed-can-with-tilted-elliptical-top'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "ecology"
    categories = ("primitives", "ecology")
    aliases = ()
    keywords = ('can', 'tin', 'metal', 'crushed', 'waste', 'recycling', 'opening', 'ecology')

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
        arc('rim-upper',(8,12),(40,12),16,8)
        arc('rim-lower',(40,12),(8,12),16,8)
        contour('rim','rim-upper','rim-lower',closed=True)
        poly('body',(40,12),(40,26),(34,32),(40,40),(36,44),(12,44),(8,40),(14,32),(8,26),(8,12))
        # Only true shared endpoints are physical connections. No proximity exemptions.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end} & {b.start,b.end}:
                    self.relate("connect",a.element_id,b.element_id)

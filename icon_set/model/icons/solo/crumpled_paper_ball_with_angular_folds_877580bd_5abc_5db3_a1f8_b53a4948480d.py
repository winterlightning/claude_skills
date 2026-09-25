"""Crumpled Paper Ball.

Symbol plan: Faceted paper silhouette; three broad folds meet at one shared interior junction.
Keyshape SQUARE: visible ink extremes (4, 4, 44, 44); stroke centerlines inset 2.
Lucide construction reference: no useful local match.
Source is visual subject evidence; geometry is freshly authored at 48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '877580bd-5abc-5db3-a1f8-b53a4948480d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/ecology/paper ball_877580bd-5abc-5db3-a1f8-b53a4948480d.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'crumpled-paper-ball-with-angular-folds'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "ecology"
    aliases = ()
    keywords = ('paper', 'crumpled', 'ball', 'waste', 'folds', 'recycling', 'trash', 'ecology')

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
        poly('outline',(6,17),(17,6),(31,6),(42,18),(42,31),(31,42),(17,42),(6,31),closed=True)
        poly('fold-left',(6,17),(22,24),(17,42))
        poly('fold-right',(22,24),(31,16),(31,6))
        # Only true shared endpoints are physical connections. No proximity exemptions.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end} & {b.start,b.end}:
                    self.relate("connect",a.element_id,b.element_id)

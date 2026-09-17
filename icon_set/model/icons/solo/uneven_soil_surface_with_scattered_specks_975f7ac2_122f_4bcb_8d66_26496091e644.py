"""Contaminated Soil Surface.

Symbol plan: Asymmetric ground mound and low undulations with a sparse four-speck field.
Keyshape HRECT_M: visible ink extremes (2, 8, 46, 40); stroke centerlines inset 2.
Lucide construction reference: no useful local match.
Source is visual subject evidence; geometry is freshly authored at 48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '975f7ac2-122f-4bcb-8d66-26496091e644'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/ecology/soil pollution_975f7ac2-122f-4bcb-8d66-26496091e644.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'uneven-soil-surface-with-scattered-specks'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/ecology"
    aliases = ()
    keywords = ('soil', 'contamination', 'ground', 'pollution', 'specks', 'surface', 'land', 'ecology')

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
        arc('mound',(4,26),(20,26),8,7)
        arc('valley',(20,26),(32,26),6,2,sweep=False)
        arc('hill',(32,26),(44,26),6,2)
        contour('ground','mound','valley','hill')
        for i,p in enumerate(((8,10),(29,10),(13,38),(37,38))): self.add_dot('speck'+str(i),p)
        # Only true shared endpoints are physical connections. No proximity exemptions.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end} & {b.start,b.end}:
                    self.relate("connect",a.element_id,b.element_id)

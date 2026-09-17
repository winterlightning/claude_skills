"""Airplane Spraying Crop Field.

Symbol plan: Side-view crop plane above three repeated open sprouts; spray reduced to two dots.
Keyshape SQUARE: visible ink extremes (4, 4, 44, 44); stroke centerlines inset 2.
Lucide construction reference: no useful local match.
Source is visual subject evidence; geometry is freshly authored at 48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e90b088e-df73-455c-88bd-5035e3e5a851'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/ecology/soil pollution plane_e90b088e-df73-455c-88bd-5035e3e5a851.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'airplane-spraying-over-three-crop-sprouts'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/ecology"
    aliases = ()
    keywords = ('airplane', 'spray', 'crops', 'field', 'farming', 'agriculture', 'pesticide', 'ecology')

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
        poly('plane-upper',(6,6),(12,14),(20,14),(26,6),(30,14),(36,14))
        arc('nose',(36,14),(36,22),4)
        poly('plane-lower',(36,22),(16,22),(6,22),(6,6))
        contour('plane','plane-upper-1','plane-upper-2','plane-upper-3','plane-upper-4','plane-upper-5','nose','plane-lower-1','plane-lower-2','plane-lower-3',closed=True)
        for i,x in enumerate((9,24,39)):
         poly('crop'+str(i),(x-3,38),(x,42),(x+3,38))
        for i,x in enumerate((19,31)): self.add_dot('spray'+str(i),(x,30))
        # Only true shared endpoints are physical connections. No proximity exemptions.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end} & {b.start,b.end}:
                    self.relate("connect",a.element_id,b.element_id)

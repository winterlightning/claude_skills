"""Dead Fish Symbol.

Symbol plan: Diagonal fish with forked tail and crossed eye; side fins omitted to preserve a broad body and clear eye.
Keyshape SQUARE: visible ink extremes (4, 4, 44, 44); stroke centerlines inset 2.
Lucide construction reference: fish.
Source is visual subject evidence; geometry is freshly authored at 48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6b2c77d3-0c2d-57e2-9129-cc5e7279aa93'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/ecology/pollution fish_6b2c77d3-0c2d-57e2-9129-cc5e7279aa93.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'diagonal-dead-fish-with-crossed-eye'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "ecology"
    aliases = ()
    keywords = ('fish', 'dead', 'eye', 'tail', 'fins', 'pollution', 'water', 'ecology')

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
        arc('back',(14,30),(30,6),16,24)
        line('nose-top',(30,6),(42,6))
        line('nose-right',(42,6),(42,18))
        arc('belly',(42,18),(18,34),24,16)
        poly('tail',(18,34),(16,42),(6,32),(14,30))
        contour('fish','back','nose-top','nose-right','belly','tail-1','tail-2','tail-3',closed=True)
        poly('eye-a',(27,17),(29,19),(31,21))
        poly('eye-b',(27,21),(29,19),(31,17))
        # Only true shared endpoints are physical connections. No proximity exemptions.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end} & {b.start,b.end}:
                    self.relate("connect",a.element_id,b.element_id)

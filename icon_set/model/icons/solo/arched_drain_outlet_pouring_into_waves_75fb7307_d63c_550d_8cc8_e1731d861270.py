"""Water Pollution Discharge Pipe.
Symbol plan: Concentric arched drain surround and open stream join a repeated wave baseline.
Reference construction: none.
SQUARE visible extremes: (4, 4, 44, 44); centerlines inset 2.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '75fb7307-d63c-550d-8cc8-e1731d861270'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/ecology/pollution water_75fb7307-d63c-550d-8cc8-e1731d861270.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'arched-drain-outlet-pouring-into-waves'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/ecology"
    aliases = ()
    keywords = ('drain', 'pipe', 'water', 'discharge', 'stream', 'pollution', 'outlet', 'ecology')
    def build(self):

        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*pts,closed=False): self.add_polyline(n,*pts,closed=closed)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry,sweep=sweep)
        def contour(n,*parts,closed=False):
            self.contours[:] = [c for c in self.contours if not set(c.members) & set(parts)]
            self.add_contour(n,*parts,closed=closed)
        def circle(n,x,y,r):
            arc(n+'a',(x-r,y),(x+r,y),r)
            arc(n+'b',(x+r,y),(x-r,y),r)
            contour(n,n+'a',n+'b',closed=True)
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
        arc('surround',(6,24),(42,24),18)
        arc('opening',(15,24),(33,24),9)
        line('flow-left',(15,40),(15,24))
        line('flow-right',(33,24),(33,40))
        contour('stream','flow-left','opening','flow-right')
        line('flow',(24,27),(24,33))
        poly('water',(6,42),(15,40),(24,42),(33,40),(42,42))
        # Declare only exact shared-endpoint contacts, not mere proximity.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end} & {b.start,b.end}: self.relate('connect',a.element_id,b.element_id)

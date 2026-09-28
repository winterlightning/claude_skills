"""Electrical Circuit Breaker.
Symbol plan: Breaker housing with mounting tabs and a broad horizontal toggle.
Reference construction: none.
VRECT_L visible extremes: (6, 2, 42, 46); centerlines inset 2.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b412020d-884e-44e7-9258-efc751bc3154'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/electronics/circuit breaker_b412020d-884e-44e7-9258-efc751bc3154.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'circuit-breaker-with-central-crosswise-toggle'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'electronics'
    categories = ('electronics', 'primitives')
    aliases = ()
    keywords = ('breaker', 'circuit', 'switch', 'toggle', 'housing', 'electric', 'power', 'electronics')
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
        poly('top',(12,10),(16,10),(16,4),(32,4),(32,10),(36,10))
        arc('top-right',(36,10),(40,14),4)
        line('right',(40,14),(40,34))
        arc('bottom-right',(40,34),(36,38),4)
        poly('bottom',(36,38),(32,38),(32,44),(16,44),(16,38),(12,38))
        arc('bottom-left',(12,38),(8,34),4)
        line('left',(8,34),(8,14))
        arc('top-left',(8,14),(12,10),4)
        contour('housing',*(['top-'+str(i) for i in range(1,6)]+['top-right','right','bottom-right']+['bottom-'+str(i) for i in range(1,6)]+['bottom-left','left','top-left']),closed=True)
        rect('toggle',17,20,14,8)
        # Declare only exact shared-endpoint contacts, not mere proximity.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end} & {b.start,b.end}: self.relate('connect',a.element_id,b.element_id)

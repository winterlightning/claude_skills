"""Industrial Oil Drum.
Symbol plan: Straight drum with upper and lower rims, two reinforcement bands and a raised bung.
Reference construction: barrel.
VRECT_L visible extremes: (6, 2, 42, 46); centerlines inset 2.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0811dee5-d46a-5e4e-b8de-fd242fdf30ca'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/ecology/fossil energy barrel_0811dee5-d46a-5e4e-b8de-fd242fdf30ca.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'straight-sided-oil-drum-with-top-bung'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/ecology"
    aliases = ()
    keywords = ('oil', 'drum', 'barrel', 'industrial', 'bung', 'storage', 'metal', 'container')
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
        poly('top',(8,12),(12,12),(28,12),(36,12),(40,12))
        poly('body',(12,12),(12,44),(36,44),(36,12))
        poly('bottom',(8,44),(12,44),(36,44),(40,44))
        for i,y in enumerate((24,34)):line('band'+str(i),(8,y),(40,y))
        poly('bung',(28,12),(28,4),(36,4),(36,12))
        # Declare only exact shared-endpoint contacts, not mere proximity.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end} & {b.start,b.end}: self.relate('connect',a.element_id,b.element_id)

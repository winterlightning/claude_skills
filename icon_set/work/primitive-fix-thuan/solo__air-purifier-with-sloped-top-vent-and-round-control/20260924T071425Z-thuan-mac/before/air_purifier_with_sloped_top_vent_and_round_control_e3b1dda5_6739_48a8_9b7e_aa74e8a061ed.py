"""Modern Air Purifier Device.
Symbol plan: Sloped-top air purifier with front control; top vent uses a broad horizontal opening.
Reference construction: air-vent.
VRECT_M visible extremes: (8, 2, 40, 46); centerlines inset 2.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e3b1dda5-6739-48a8-9b7e-aa74e8a061ed'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/ecology/air purifier 3_e3b1dda5-6739-48a8-9b7e-aa74e8a061ed.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'air-purifier-with-sloped-top-vent-and-round-control'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/ecology"
    aliases = ()
    keywords = ('purifier', 'air', 'device', 'vent', 'control', 'home', 'appliance', 'ecology')
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
        poly('body',(10,22),(14,4),(34,4),(38,22),(38,40),(34,44),(14,44),(10,40),closed=True)
        line('seam',(10,22),(38,22))
        line('vent',(21,13),(27,13))
        circle('control',24,33,2)
        # Declare only exact shared-endpoint contacts, not mere proximity.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end} & {b.start,b.end}: self.relate('connect',a.element_id,b.element_id)

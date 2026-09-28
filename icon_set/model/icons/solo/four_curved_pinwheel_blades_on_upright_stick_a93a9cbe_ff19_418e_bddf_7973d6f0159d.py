"""Four Blade Pinwheel.
Symbol plan: Four rotationally repeated curved blades about a central node; stick descends from that hub.
Reference construction: none.
VRECT_L visible extremes: (6, 2, 42, 46); centerlines inset 2.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a93a9cbe-ff19-418e-bddf-7973d6f0159d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/ecology/renewable energy paper turbine_a93a9cbe-ff19-418e-bddf-7973d6f0159d.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'four-curved-pinwheel-blades-on-upright-stick'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "ecology"
    categories = ("primitives", "ecology")
    aliases = ()
    keywords = ('pinwheel', 'wind', 'blades', 'rotation', 'stick', 'toy', 'energy', 'ecology')
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
        center=(24,20)
        def turn(p,k):
         x,y=p[0]-24,p[1]-20
         for _ in range(k):x,y=-y,x
         return (24+x,20+y)
        for i in range(4):
         a,b,c=[turn(p,i) for p in ((24,20),(8,4),(20,4))]
         line('blade-edge'+str(i),a,b)
         line('blade-tip'+str(i),b,c)
         arc('blade-curve'+str(i),c,a,16 if i%2 else 4,4 if i%2 else 16,sweep=True)
         contour('blade'+str(i),'blade-edge'+str(i),'blade-tip'+str(i),'blade-curve'+str(i),closed=True)
        line('stick',(24,20),(24,44))
        # Declare only exact shared-endpoint contacts, not mere proximity.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end} & {b.start,b.end}: self.relate('connect',a.element_id,b.element_id)

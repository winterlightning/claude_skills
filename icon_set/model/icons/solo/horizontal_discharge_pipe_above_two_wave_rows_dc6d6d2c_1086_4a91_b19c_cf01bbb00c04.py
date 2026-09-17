"""Water Pollution Pipe.
Symbol plan: Valve pipe with an attached broad collar and two rows of peaked water.
Reference construction: none.
SQUARE visible extremes: (4, 4, 44, 44); centerlines inset 2.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'dc6d6d2c-1086-4a91-b19c-cf01bbb00c04'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/ecology/pollution faucet water_dc6d6d2c-1086-4a91-b19c-cf01bbb00c04.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'horizontal-discharge-pipe-above-two-wave-rows'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/ecology"
    aliases = ()
    keywords = ('pipe', 'water', 'discharge', 'valve', 'pollution', 'outlet', 'waves', 'ecology')
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
        poly('upper-pipe',(6,14),(14,14),(24,14))
        line('lower-pipe',(6,22),(24,22))
        poly('collar',(24,14),(24,6),(32,6),(32,22),(24,22),(24,14))
        poly('valve',(8,6),(14,6),(20,6))
        line('valve-stem',(14,6),(14,14))
        arc('discharge',(41,17),(42,22),1,5)
        for i,y in enumerate((32,42)):poly('wave'+str(i),(6,y),(15,y-1),(24,y),(33,y-1),(42,y))
        # Declare only exact shared-endpoint contacts, not mere proximity.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end} & {b.start,b.end}: self.relate('connect',a.element_id,b.element_id)

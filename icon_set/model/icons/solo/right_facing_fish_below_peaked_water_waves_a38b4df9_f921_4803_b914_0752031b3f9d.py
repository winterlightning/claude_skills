"""Fish Swimming Under Water.
Symbol plan: Fish below a repeated row of peaked waves; one point eye and forked tail.
Reference construction: fish.
HRECT_L visible extremes: (2, 6, 46, 42); centerlines inset 2.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a38b4df9-f921-4803-b914-0752031b3f9d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/ecology/water protection fish_a38b4df9-f921-4803-b914-0752031b3f9d.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'right-facing-fish-below-peaked-water-waves'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "ecology"
    categories = ("primitives", "ecology")
    aliases = ()
    keywords = ('fish', 'water', 'waves', 'swimming', 'fins', 'tail', 'sea', 'ecology')
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
        for i in range(3): arc('wave'+str(i),(4+i*13,8),(17+i*13,8),8,5,sweep=False)
        contour('waves','wave0','wave1','wave2')
        arc('fish-top',(16,30),(44,30),14,10)
        arc('fish-bottom',(44,30),(16,30),14,10)
        poly('tail',(16,30),(4,22),(4,38),(16,30))
        contour('body','fish-top','fish-bottom',closed=True)
        self.add_dot('eye',(34,30))
        # Declare only exact shared-endpoint contacts, not mere proximity.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end} & {b.start,b.end}: self.relate('connect',a.element_id,b.element_id)

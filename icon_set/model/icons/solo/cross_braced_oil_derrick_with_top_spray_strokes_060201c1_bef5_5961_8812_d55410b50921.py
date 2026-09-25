"""Oil Derrick Tower.
Symbol plan: Triangular derrick with one cross-braced tier and three separated spray strokes.
Reference construction: none.
VRECT_L visible extremes: (6, 2, 42, 46); centerlines inset 2.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '060201c1-bef5-5961-8812-d55410b50921'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/ecology/fossil energy plant_060201c1-bef5-5961-8812-d55410b50921.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'cross-braced-oil-derrick-with-top-spray-strokes'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "ecology"
    aliases = ()
    keywords = ('oil', 'derrick', 'tower', 'braces', 'drilling', 'spray', 'industry', 'energy')
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
        poly('tower',(8,44),(16,29),(24,14),(32,29),(40,44),closed=True)
        poly('brace-left',(16,29),(24,34),(40,44))
        poly('brace-right',(32,29),(24,34),(8,44))
        line('spray-center',(24,4),(24,4+1))
        line('spray-left',(11,4),(14,7))
        line('spray-right',(37,4),(34,7))
        # Declare only exact shared-endpoint contacts, not mere proximity.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end} & {b.start,b.end}: self.relate('connect',a.element_id,b.element_id)

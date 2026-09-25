"""Plant Seedling with Underground Roots.
Symbol plan: Paired broad leaves join a stem, ground and mirrored branching roots.
Reference construction: sprout.
SQUARE visible extremes: (4, 4, 44, 44); centerlines inset 2.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'fee34e6e-f327-40d6-a855-932b65813edf'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/ecology/organic plant root_fee34e6e-f327-40d6-a855-932b65813edf.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'two-leaf-seedling-with-exposed-branching-roots'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "ecology"
    aliases = ()
    keywords = ('seedling', 'roots', 'plant', 'leaves', 'soil', 'growth', 'nature', 'ecology')
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
        arc('leaf-left-outer',(6,6),(24,22),18,16,sweep=False)
        arc('leaf-left-inner',(24,22),(6,6),18,16,sweep=False)
        contour('leaf-left','leaf-left-outer','leaf-left-inner',closed=True)
        arc('leaf-right-inner',(24,22),(42,6),18,16,sweep=False)
        arc('leaf-right-outer',(42,6),(24,22),18,16,sweep=False)
        contour('leaf-right','leaf-right-inner','leaf-right-outer',closed=True)
        poly('stem',(24,22),(24,30),(24,38),(24,42))
        poly('soil',(6,30),(24,30),(42,30))
        poly('roots',(12,42),(12,38),(24,38),(36,38),(36,42))
        # Declare only exact shared-endpoint contacts, not mere proximity.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end} & {b.start,b.end}: self.relate('connect',a.element_id,b.element_id)

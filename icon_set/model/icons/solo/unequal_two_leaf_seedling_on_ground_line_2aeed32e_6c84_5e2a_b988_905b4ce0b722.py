"""Seedling Growing From Soil.
Symbol plan: Unequal pointed leaves fork from a stem above a short ground line.
Reference construction: sprout.
SQUARE visible extremes: (4, 4, 44, 44); centerlines inset 2.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2aeed32e-6c84-5e2a-b988-905b4ce0b722'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/ecology/organic plant grow_2aeed32e-6c84-5e2a-b988-905b4ce0b722.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'unequal-two-leaf-seedling-on-ground-line'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "ecology"
    categories = ("primitives", "ecology")
    aliases = ()
    keywords = ('seedling', 'plant', 'leaves', 'stem', 'growth', 'soil', 'nature', 'ecology')
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
        arc('left-outer',(6,10),(24,26),18,16,sweep=False)
        arc('left-inner',(24,26),(6,10),18,16,sweep=False)
        contour('left-leaf','left-outer','left-inner',closed=True)
        arc('right-inner',(24,26),(42,6),18,20,sweep=False)
        arc('right-outer',(42,6),(24,26),18,20,sweep=False)
        contour('right-leaf','right-inner','right-outer',closed=True)
        poly('stem',(24,26),(24,32),(24,42))

        poly('ground',(10,42),(24,42),(38,42))
        # Declare only exact shared-endpoint contacts, not mere proximity.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end} & {b.start,b.end}: self.relate('connect',a.element_id,b.element_id)

"""Simple Wavy Organic Worm.
Symbol plan: Unsegmented worm made from two tangent S curves and semicircular endcaps.
Reference construction: worm.
SQUARE visible extremes: (4, 4, 44, 44); centerlines inset 2.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e0977fb0-a709-47e6-b9c3-35874f16aadd'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/ecology/organic worm_e0977fb0-a709-47e6-b9c3-35874f16aadd.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'smooth-s-shaped-worm-with-rounded-ends'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "ecology"
    categories = ("primitives", "ecology")
    aliases = ()
    keywords = ('worm', 'organic', 'curve', 'soil', 'nature', 'body', 'animal', 'ecology')
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
        arc('outer-lower',(6,37),(24,19),18)
        arc('inner-upper',(24,19),(32,11),8,sweep=False)
        arc('cap-upper',(32,11),(42,11),5)
        arc('outer-upper',(42,11),(24,29),18)
        arc('inner-lower',(24,29),(16,37),8,sweep=False)
        arc('cap-lower',(16,37),(6,37),5)
        contour('worm','outer-lower','inner-upper','cap-upper','outer-upper','inner-lower','cap-lower',closed=True)
        # Declare only exact shared-endpoint contacts, not mere proximity.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end} & {b.start,b.end}: self.relate('connect',a.element_id,b.element_id)

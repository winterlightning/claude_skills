"""Trash Can and Garbage Bag.
Symbol plan: Tied bag overlaps the lower left of a tall bin with protruding rubbish.
Reference construction: trash.
SQUARE visible extremes: (4, 4, 44, 44); centerlines inset 2.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2295a288-f526-406a-ae2e-c1f6bc4d44eb'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/ecology/garbage_2295a288-f526-406a-ae2e-c1f6bc4d44eb.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'tied-garbage-bag-beside-filled-trash-bin'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/ecology"
    aliases = ()
    keywords = ('trash', 'bin', 'bag', 'garbage', 'waste', 'rubbish', 'disposal', 'ecology')
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
        poly('bin',(26,16),(42,16),(39,42),(16,42))
        poly('rubbish',(26,16),(29,6),(39,8),(38,16))
        arc('bag-left',(16,26),(6,36),10,sweep=False)
        arc('bag-base-left',(6,36),(16,42),10,6,sweep=False)
        arc('bag-base-right',(16,42),(26,36),10,6,sweep=False)
        arc('bag-right',(26,36),(16,26),10,sweep=False)
        contour('bag','bag-left','bag-base-left','bag-base-right','bag-right',closed=True)
        poly('tie',(16,26),(8,16),(20,16),(16,26))
        # Declare only exact shared-endpoint contacts, not mere proximity.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end} & {b.start,b.end}: self.relate('connect',a.element_id,b.element_id)

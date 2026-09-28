"""Closed Curtains with Centre Seam.

Symbol plan: Mirrored long panels share one centre seam and rod. Two short top folds align symmetrically; tangent bottom corners.
Lucide construction: blinds; original and atomic-debug inspected.
Keyshape: SQUARE; centerline (6,6)-(42,42); ink (4,4)-(44,44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c81c6e70-d16e-4627-aaa2-da0fd110e63b'
SOURCE_PATH = 'pictographic-primitives/building/curtains closed_c81c6e70-d16e-4627-aaa2-da0fd110e63b.svg'
AUTHOR = 'gpt-6'


class ClosedCurtainsWithCentreSeam(Solo48):
    icon_id = 'closed-curtains-with-centre-seam'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'building'
    categories = ('building', 'primitives')
    aliases = ()
    keywords = ('closed', 'curtains', 'with', 'centre', 'seam')

    def build(self):
        self.path('rod',(6,6),(8,6),(16,6),(24,6),(32,6),(40,6),(42,6))
        self.path('curtain',(8,6),(8,36),(14,42,6,6,False),(24,42),(34,42),(40,36,6,6,False),(40,6))
        self.add_line('seam',(24,6),(24,42));self.relate('connect','seam','rod');self.relate('connect','seam','curtain');self.relate('connect','curtain','rod')
        for x in (16,32):
            self.add_line('fold-'+str(x),(x,6),(x,16));self.relate('connect','fold-'+str(x),'rod')

    def path(self, name, start, *steps, closed=False):
        members=[]
        point=start
        for i, step in enumerate(steps):
            member=f"{name}-{i+1}"
            if len(step)==2:
                self.add_line(member, point, step)
                point=step
            else:
                x,y,rx,ry,sweep=step
                self.add_arc(member, point, (x,y), radius_x=rx, radius_y=ry, sweep=sweep)
                point=(x,y)
            members.append(member)
        self.add_contour(name,*members,closed=closed)

    def circle(self, name, x, y, r):
        self.path(name,(x-r,y),(x+r,y,r,r,True),(x-r,y,r,r,True),closed=True)

    def rect(self, name, x, y, w, h, r=2):
        self.path(name,(x+r,y),(x+w-r,y),(x+w,y+r,r,r,True),
                  (x+w,y+h-r),(x+w-r,y+h,r,r,True),(x+r,y+h),
                  (x,y+h-r,r,r,True),(x,y+r),(x+r,y,r,r,True),closed=True)

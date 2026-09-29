"""Restore the left-facing pointed beak, small eye, rounded breast, swept wing and tapered tail with two legs."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '7e1a8309-f138-49c1-a543-a29fe848c8be'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__wild-bird/20260929T085457Z-thuan-mac/reference/wild bird 2_7e1a8309-f138-49c1-a543-a29fe848c8be.svg'
AUTHOR = "gpt-6"

class RevisedIcon(Solo48):
    icon_id = 'wild-bird'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/people" 
    aliases = ()
    keywords = ('wild bird 2',)
    # Symbol plan: Restore the left-facing pointed beak, small eye, rounded breast, swept wing and tapered tail with two legs.
    # Construction: lucide/original/bird.svg and atomic-debug/bird.svg: simple beak, sweep of breast and two short legs.

    def path(self, name, start, *segments, closed=False):
        ids = []
        point = start
        for j, segment in enumerate(segments):
            eid = f"{name}-{j}"
            if len(segment) == 2:
                self.add_line(eid, point, segment)
                end = segment
            else:
                end, rx, ry, sweep, large = segment
                self.add_arc(eid, point, end, radius_x=rx, radius_y=ry,
                             sweep=sweep, large_arc=large)
            ids.append(eid)
            point = end
        self.add_contour(name, *ids, closed=closed)

    def circle(self, name, x, y, r):
        self.path(name, (x-r,y), ((x+r,y),r,r,True,False),
                  ((x-r,y),r,r,True,False), closed=True)

    def oval(self, name, x, y, rx, ry):
        self.path(name, (x-rx,y), ((x+rx,y),rx,ry,True,False),
                  ((x-rx,y),rx,ry,True,False), closed=True)

    def box(self, name, x1,y1,x2,y2,r=3):
        self.path(name, (x1+r,y1), (x2-r,y1),
                  ((x2,y1+r),r,r,True,False), (x2,y2-r),
                  ((x2-r,y2),r,r,True,False), (x1+r,y2),
                  ((x1,y2-r),r,r,True,False), (x1,y1+r),
                  ((x1+r,y1),r,r,True,False), closed=True)

    def build(self):

        self.path('body',(13,10),((27,8),9,8,True,False),(41,36),
                  (32,33),((17,35),15,8,True,False),((11,18),10,18,True,False),(13,10),closed=True)
        self.path('beak',(12,11),(6,15),(11,18))
        self.add_dot('eye',(19,14))
        self.path('wing',(22,23),((28,27),7,6,False,False))
        self.add_line('leg-left',(20,36),(17,44))
        self.add_line('leg-right',(29,35),(27,44))
        self.relate('connect','beak','body')
     

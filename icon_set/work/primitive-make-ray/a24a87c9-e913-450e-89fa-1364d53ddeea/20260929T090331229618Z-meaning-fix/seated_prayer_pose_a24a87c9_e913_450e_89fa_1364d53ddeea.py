"""Show hands joined upright at the chest, bent elbows and a closed crossed-leg seat."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'a24a87c9-e913-450e-89fa-1364d53ddeea'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__seated-prayer-pose/20260929T085457Z-thuan-mac/reference/yoga meditation pose_a24a87c9-e913-450e-89fa-1364d53ddeea.svg'
AUTHOR = "gpt-6"

class RevisedIcon(Solo48):
    icon_id = 'seated-prayer-pose'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/people" 
    aliases = ()
    keywords = ('yoga meditation pose',)
    # Symbol plan: Show hands joined upright at the chest, bent elbows and a closed crossed-leg seat.
    # Construction: human_ref/full_body_ref.png

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

        self.circle('head',24,9,5)
        # Mirrored shoulder/elbow arcs leave an explicit upright prayer gesture.
        self.path('shoulders', (10,30), (12,25), ((19,22),10,5,True,False))
        self.path('shoulder-right',(29,22),((36,25),10,5,True,False),(38,30))
        self.path('praying-arms', (10,30), ((15,33),4,4,False,False),
                  (24,28), (24,22))
        self.path('right-forearm',(24,28),(33,33),((38,30),4,4,False,False))
        self.path('crossed-legs',(24,39),(12,35),((6,39),4,4,False,False),
                  ((11,43),5,4,False,False),(37,43),((42,39),5,4,False,False),
                  ((36,35),4,4,False,False),(24,39),(31,42))
        self.relate('connect','shoulders','praying-arms')
        self.relate('connect','shoulder-right','right-forearm')
        self.relate('connect','praying-arms','right-forearm')
     

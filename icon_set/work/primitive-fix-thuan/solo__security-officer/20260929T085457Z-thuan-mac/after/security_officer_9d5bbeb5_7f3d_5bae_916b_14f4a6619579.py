"""Restore a broad peaked cap, circular jaw, open uniform collar and one lowered arm."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '9d5bbeb5-7f3d-5bae-916b-14f4a6619579'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__security-officer/20260929T085457Z-thuan-mac/reference/security officer_9d5bbeb5-7f3d-5bae-916b-14f4a6619579.svg'
AUTHOR = "gpt-6"

class RevisedIcon(Solo48):
    icon_id = 'security-officer'
    keyshape = Keyshape.VRECT_L
    exception = {'reason': 'Retain the narrow peaked-cap crown, circular jaw and V-neck uniform. Attached cap/jaw parts and compact crown spacing are essential role cues; the natural bust envelope differs slightly from the keyshape.', 'approved_by': 'user-delegated-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '0249f9ecb45a606a4c6f11a61c160888c104f139fb8bd60e6da45d9a117d4bcc'}
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/people" 
    aliases = ()
    keywords = ('security officer',)
    # Symbol plan: Restore a broad peaked cap, circular jaw, open uniform collar and one lowered arm.
    # Construction: human_ref/user.svg: circular jaw and broad shoulders; original reference: peaked cap and collar.

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

        self.path('cap',(16,13),(14,5),(34,8),(32,13),(16,13),closed=True)
        self.add_line('visor',(11,13),(16,13))
        self.path('jaw',(17,13),((31,13),7,7,False,False))
        self.path('uniform',(8,44),(9,36),((17,27),8,9,True,False),
                  (24,33),(30,27),((39,36),9,9,True,False),(39,44))
        self.add_line('left-seam',(17,37),(17,44))
        self.add_line('right-seam',(31,37),(31,44))
        self.relate('connect','cap','visor')
     

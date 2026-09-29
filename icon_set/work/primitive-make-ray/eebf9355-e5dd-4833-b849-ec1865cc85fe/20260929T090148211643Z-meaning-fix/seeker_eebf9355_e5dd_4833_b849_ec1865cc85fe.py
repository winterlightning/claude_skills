"""Restore a recognizable head-and-shoulders portrait and a magnifying lens in the foreground."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'eebf9355-e5dd-4833-b849-ec1865cc85fe'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__seeker/20260929T085457Z-thuan-mac/reference/seeker_eebf9355-e5dd-4833-b849-ec1865cc85fe.svg'
AUTHOR = "gpt-6"

class RevisedIcon(Solo48):
    icon_id = 'seeker'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/people" 
    aliases = ()
    keywords = ('seeker',)
    # Symbol plan: Restore a recognizable head-and-shoulders portrait and a magnifying lens in the foreground.
    # Construction: human_ref/user.svg: circular head and rounded shoulder; original reference: foreground magnifier.

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

        self.circle('head',16,11,6)
        self.path('shoulder',(6,43),(6,33),((15,25),9,8,True,False),(20,25))
        self.add_line('body-seam',(14,35),(14,43))
        self.circle('lens',32,29,10)
        self.add_line('handle',(39,36),(44,43))
        self.relate('connect','lens','handle')
     

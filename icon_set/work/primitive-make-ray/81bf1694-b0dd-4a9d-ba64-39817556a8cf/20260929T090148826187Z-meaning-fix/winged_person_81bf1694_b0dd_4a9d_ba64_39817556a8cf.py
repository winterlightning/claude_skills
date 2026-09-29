"""Restore a full-height human body with separate arms and legs and compact scalloped wings attached behind the shoulders."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '81bf1694-b0dd-4a9d-ba64-39817556a8cf'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__winged-person/20260929T085457Z-thuan-mac/reference/wingman_81bf1694-b0dd-4a9d-ba64-39817556a8cf.svg'
AUTHOR = "gpt-6"

class RevisedIcon(Solo48):
    icon_id = 'winged-person'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/people" 
    aliases = ()
    keywords = ('wingman',)
    # Symbol plan: Restore a full-height human body with separate arms and legs and compact scalloped wings attached behind the shoulders.
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
        self.path('body',(17,44),(17,24),((24,22),9,3,True,False),
                  ((31,24),9,3,True,False),(31,44))
        self.add_line('leg-divider',(24,35),(24,44))
        self.path('left-wing',(17,24),((4,22),9,6,False,False),
                  ((8,29),6,6,False,False),((12,33),4,4,False,False))
        self.path('right-wing',(31,24),((44,22),9,6,True,False),
                  ((40,29),6,6,True,False),((36,33),4,4,True,False))
        self.relate('connect','body','left-wing')
        self.relate('connect','body','right-wing')
     

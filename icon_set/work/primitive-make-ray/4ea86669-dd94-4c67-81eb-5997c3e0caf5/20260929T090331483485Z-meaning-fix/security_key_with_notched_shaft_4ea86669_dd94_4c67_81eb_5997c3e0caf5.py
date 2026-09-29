"""Restore the round bow, enclosed keyhole, long shaft, pointed tip and two bottom notches."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '4ea86669-dd94-4c67-81eb-5997c3e0caf5'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__security-key-with-notched-shaft/20260929T085457Z-thuan-mac/reference/crypto encryption key_4ea86669-dd94-4c67-81eb-5997c3e0caf5.svg'
AUTHOR = "gpt-6"

class RevisedIcon(Solo48):
    icon_id = 'security-key-with-notched-shaft'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/people" 
    aliases = ()
    keywords = ('crypto encryption key',)
    # Symbol plan: Restore the round bow, enclosed keyhole, long shaft, pointed tip and two bottom notches.
    # Construction: lucide/original/key-round.svg and atomic-debug/key-round.svg: circular bow and integrated toothed contour.

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

        # Circular bow and integrated notched shaft; asymmetric by key function.
        self.path('outline',(26,18),(39,18),(44,24),(40,30),(36,30),(33,27),
                  (30,30),(26,30),((26,18),11,11,True,True),closed=True)
        self.circle('keyhole',15,24,3)
     

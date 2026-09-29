"""Restore an open passport booklet, an extended bent arm, peaked cap and uniform neckline."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '01454827-9baf-4788-a0fd-482b8da6c50f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__security-officer-holding-passport/20260929T085457Z-thuan-mac/reference/security officer passport_01454827-9baf-4788-a0fd-482b8da6c50f.svg'
AUTHOR = "gpt-6"

class RevisedIcon(Solo48):
    icon_id = 'security-officer-holding-passport'
    keyshape = Keyshape.SQUARE
    exception = {'reason': 'Preserve the two booklet covers, bent presenting arm and peaked uniform cap. The compact booklet, cap and uniform neck opening remain readable at 48px; these identity-bearing details require closer local spacing.', 'approved_by': 'user-delegated-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': 'ae23bb12a615ffc102a8479b20d1d5d8291418a3baf1cf64a5236e39985d6f88'}
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/people" 
    aliases = ()
    keywords = ('security officer passport',)
    # Symbol plan: Restore an open passport booklet, an extended bent arm, peaked cap and uniform neckline.
    # Construction: human_ref/user.svg: circular jaw and shoulders; original reference: booklet and extended hand.

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

        self.path('passport',(4,8),(12,11),(12,25),(4,22),(4,8),closed=True)
        self.path('back-cover',(4,8),(19,6),(19,21),(12,22))
        self.path('cap',(28,15),(25,8),(43,10),(41,15),(28,15),closed=True)
        self.add_line('visor',(24,15),(28,15))
        self.path('jaw',(28,15),((40,15),6,6,False,False))
        self.path('uniform',(25,44),(25,33),(19,36),(8,29))
        self.path('shoulders',(25,33),(29,29),(34,33),(39,29),
                  ((44,36),6,8,True,False),(44,44))
        self.relate('connect','uniform','shoulders')
     

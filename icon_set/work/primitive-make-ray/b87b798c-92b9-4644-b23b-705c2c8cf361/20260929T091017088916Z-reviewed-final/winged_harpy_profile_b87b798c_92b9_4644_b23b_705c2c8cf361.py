"""Restore a profile head with flowing hair, feathered spread wings, tapered bird body and clawed feet."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'b87b798c-92b9-4644-b23b-705c2c8cf361'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__winged-harpy-profile/20260929T085457Z-thuan-mac/reference/harpy_b87b798c-92b9-4644-b23b-705c2c8cf361.svg'
AUTHOR = "gpt-6"

class RevisedIcon(Solo48):
    icon_id = 'winged-harpy-profile'
    keyshape = Keyshape.SQUARE
    exception = {'reason': 'Preserve a continuous human profile and long hair, feather-shaped spread wings, tapered bird body and talons. Narrow hair/wing openings and close anatomical joins preserve the harpy identity at 48px.', 'approved_by': 'user-delegated-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '2edb407239d88c5008455c205af47487675fc1181d5c3922d7ddee66e00e98b5'}
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/people" 
    aliases = ()
    keywords = ('harpy',)
    # Symbol plan: Restore a profile head with flowing hair, feathered spread wings, tapered bird body and clawed feet.
    # Construction: human_ref/user.svg: rounded human face; original reference controls continuous neck, hair and avian anatomy.

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

        self.path('hair',(17,21),(18,9),((27,4),7,6,True,False),
                  ((29,10),5,6,True,False),((23,12),7,5,True,False),(23,18))
        self.path('face-body',(29,10),(30,16),(27,18),(27,21),
                  ((25,33),8,10,True,False),(16,39),(20,30))
        self.path('left-wing',(18,21),((5,14),24,15,True,False),(6,24),
                  (10,27),(8,29),((18,31),11,5,False,False))
        self.path('right-wing',(28,22),((43,14),25,14,False,False),(42,24),
                  (38,27),(40,29),((29,32),11,5,True,False))
        self.path('left-claw',(22,36),(23,43),(19,44))
        self.path('right-claw',(28,35),(32,42),(36,44))
     

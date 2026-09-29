"""Rebuilt the snake’s narrow head, S-shaped neck, body draped over the hand, and descending tail.
Before: The rejected snake looks like a bird head above a hand and omits the coiled body and draped tail.
Construction: Lucide hand-heart/hand-grab for coherent thumb, knuckles and palm;
supplied reference controls the specific grasp and subject arrangement.
Shared human full_body_ref.png inspected; isolated hands have no detached head.
Keyshape VRECT_L; complete drawing remains on 48x48 with 4px strokes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'cc4af31b-ad07-4519-9e2a-a3b2ee7e8834'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-holding-snake/20260928T182143Z-thuan-mac/reference/herping_cc4af31b-ad07-4519-9e2a-a3b2ee7e8834.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hand-holding-snake'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/hands'
    aliases = ()
    keywords = ('hand', 'herping')

    def path(self, name, start, *steps, closed=False):
        members=[]
        point=start
        for i, step in enumerate(steps):
            ident=f"{name}-{i}"
            end=tuple(step[:2])
            if len(step)==2:
                self.add_line(ident, point, end)
            else:
                self.add_arc(ident, point, end, radius_x=step[2], radius_y=step[3], sweep=step[4])
            members.append(ident)
            point=end
        self.add_contour(name, *members, closed=closed)

    def circle(self, name, cx, cy, r):
        self.path(name,(cx-r,cy),(cx+r,cy,r,r,True),(cx-r,cy,r,r,True),closed=True)

    def build(self):

        # Snake owns a smooth S neck and hanging tail; palm supports its coiled body.
        self.path('snake',(35,10),(31,6,5,5,False),(23,6),(20,13,6,6,False),(26,20),(29,25,6,6,True),(24,30),(17,27),(11,28,5,5,False),(14,37),(11,44))
        self.path('snake-back',(35,10),(32,16),(34,22,9,9,True),(30,32),(24,34),(18,32),(17,36),(16,42),(11,44))
        self.add_line('tongue',(35,10),(40,11))
        self.path('palm',(6,34),(11,34))
        self.path('fingers',(18,35),(25,37),(37,32),(42,35,3,3,True),(29,42),(20,42))
        self.add_line('wrist',(6,42),(11,42))
        self.relate('connect','snake','tongue')


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

        # Smooth S-shaped snake neck, a loop on the left, and a clearly draped tail.
        self.path('snake',(34,10),(29,6,5,5,False),(25,6),(21,10,4,4,False),(21,13),(27,19),(30,25,8,8,True),(27,30),(20,28),(16,24,6,6,False),(10,25,5,5,False),(9,30),(13,38),(11,44))
        self.path('snake-back',(34,10),(31,15),(35,21,9,9,True),(32,30),(27,34),(19,33),(17,30),(16,29),(15,30),(18,39),(15,43),(11,44))
        self.add_line('tongue',(34,10),(40,11))
        self.add_line('wrist-top',(6,34),(10,34))
        self.path('hand',(20,37),(27,39),(38,34),(42,37,3,3,True),(29,44),(21,44))
        self.add_line('wrist-bottom',(6,43),(11,43))
        self.relate('connect','snake','tongue')


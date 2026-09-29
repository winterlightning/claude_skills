"""Separated the rounded heart from the hand and restored the long thumb and rising supporting fingers.
Before: The rejected heart sits on the thumb with no breathing room, and the angular hand loses the reference’s extended palm.
Construction: Lucide hand-heart/hand-grab for coherent thumb, knuckles and palm;
supplied reference controls the specific grasp and subject arrangement.
Shared human full_body_ref.png inspected; isolated hands have no detached head.
Keyshape SQUARE; complete drawing remains on 48x48 with 4px strokes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '045520ca-f23a-531a-b54e-ce7bc4cbf52e'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-holding-heart/20260928T182143Z-thuan-mac/reference/love heart hold_045520ca-f23a-531a-b54e-ce7bc4cbf52e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hand-holding-heart'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/hands'
    aliases = ()
    keywords = ('hand', 'love heart hold')

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

        # Symmetric heart floating above a deliberately asymmetric supporting hand.
        self.path('heart',(25,10),(15,10,5,5,False),(17,16,8,8,False),(25,23),(33,16),(35,10,8,8,False),(25,10,5,5,False),closed=True)

        self.path('thumb',(6,34),(13,30),(24,30),(24,36,3,3,True),(18,36))
        self.path('palm',(6,42),(14,40),(25,42),(31,40,10,10,False),(41,32),(37,28,3,3,False),(27,35))


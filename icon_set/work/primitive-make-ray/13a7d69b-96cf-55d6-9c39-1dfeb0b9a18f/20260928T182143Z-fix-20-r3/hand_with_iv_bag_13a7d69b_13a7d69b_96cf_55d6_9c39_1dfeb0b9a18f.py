"""Restored an elongated hanging IV bag, open hanger loop and curved tubing entering the receiving hand.
Before: The rejected IV bag is squat like a bottle and the stem looks like a stand rather than a tube into the hand.
Construction: Lucide hand-heart/hand-grab for coherent thumb, knuckles and palm;
supplied reference controls the specific grasp and subject arrangement.
Shared human full_body_ref.png inspected; isolated hands have no detached head.
Keyshape VRECT_L; complete drawing remains on 48x48 with 4px strokes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '13a7d69b-96cf-55d6-9c39-1dfeb0b9a18f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-with-iv-bag-13a7d69b/20260928T182143Z-thuan-mac/reference/transfusion hand_13a7d69b-96cf-55d6-9c39-1dfeb0b9a18f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hand-with-iv-bag-13a7d69b'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/hands'
    aliases = ()
    keywords = ('hand', 'transfusion hand')

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

        # Tall hanging bag above a receiving hand; unobstructed tubing carries the action.
        self.path('bag',(19,10),(29,10),(32,13,3,3,True),(32,25),(29,28,3,3,True),(19,28),(16,25,3,3,True),(16,13),(19,10,3,3,True),closed=True)
        self.path('hanger',(20,10),(20,4),(28,4),(28,10))
        self.path('tube',(24,28),(24,31),(20,35,4,4,True))
        self.path('thumb',(8,36),(15,33),(20,33),(23,36,3,3,True),(20,39),(16,39))
        self.path('palm',(8,44),(15,43),(26,44),(32,41),(39,35),(35,31,3,3,False),(25,38))
        self.relate('connect','bag','hanger')
        self.relate('connect','bag','tube')


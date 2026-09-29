"""Restored two pairs of radio waves, a phone screen with bottom bezel, and a wrapping hand with thumb and wrist.
Before: The rejected wireless phone has a diagonal slash for a hand and only one pair of radio arcs.
Construction: Lucide hand-heart/hand-grab for coherent thumb, knuckles and palm;
supplied reference controls the specific grasp and subject arrangement.
Shared human full_body_ref.png inspected; isolated hands have no detached head.
Keyshape VRECT_L; complete drawing remains on 48x48 with 4px strokes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '67fe58cc-4429-4121-a342-5bd274251e19'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-holding-wireless-phone/20260928T182143Z-thuan-mac/reference/wifi transfer hand_67fe58cc-4429-4121-a342-5bd274251e19.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hand-holding-wireless-phone'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/hands'
    aliases = ()
    keywords = ('hand', 'wifi transfer hand')

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

        # Two true concentric radio corners; phone and enclosing hand beneath.
        self.path('phone',(25,44),(14,44),(11,41,3,3,True),(11,21),(14,18,3,3,True),(27,18),(30,21,3,3,True),(30,29))
        self.add_line('bezel',(11,36),(22,36))
        self.path('thumb',(34,36),(28,30),(23,34,3,3,False),(28,40),(30,44))
        self.path('back',(30,26),(39,35,9,9,True),(39,39),(42,44))
        for side in (-1,1):
            x=lambda v:24+side*v
            self.path(f'wave-outer-{side}',(x(20),14),(x(10),4,10,10,side==-1))
            self.path(f'wave-inner-{side}',(x(14),14),(x(10),10,4,4,side==-1))
        self.relate('connect','phone','bezel')


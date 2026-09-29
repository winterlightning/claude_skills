"""Restored a circular toothed gear with central hole and an enclosing pinch hand with continuous wrist.
Before: The rejected hand is reduced to a hook with two unrelated tails, and the gear center is a dot.
Construction: Lucide hand-heart/hand-grab for coherent thumb, knuckles and palm;
supplied reference controls the specific grasp and subject arrangement.
Shared human full_body_ref.png inspected; isolated hands have no detached head.
Keyshape SQUARE; complete drawing remains on 48x48 with 4px strokes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '9375035c-5b0d-47b1-8a06-a6cd84310dca'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-holding-gear/20260928T182143Z-thuan-mac/reference/workflow teamwork cog hand_9375035c-5b0d-47b1-8a06-a6cd84310dca.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hand-holding-gear'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/hands'
    aliases = ()
    keywords = ('hand', 'workflow teamwork cog hand')

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

        # Gear owns repeated teeth around its centre; the hand wraps the right half.
        self.path('gear',(15,6),(20,6),(21,11),(25,13),(29,12),(32,17),(28,21),(28,25),(23,29),(19,26),(15,27),(13,31),(8,29),(9,24),(6,20),(9,16),(8,12),(13,11),(15,6),closed=True)
        self.circle('hub',18,19,3)
        self.path('hand-back',(30,6),(35,7),(42,19,13,13,True),(42,42))
        self.path('finger',(30,6),(29,14,4,4,False),(34,19,6,6,True),(32,27,8,8,True),(28,30),(23,27),(18,31,4,4,False),(29,42))
        self.relate('connect','hand-back','finger')


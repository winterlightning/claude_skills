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
    exception = {'reason': 'Closely spaced gear teeth and gripping thumb preserve mechanical teamwork meaning; the hub and palm remain open. Reviewed against the supplied original and rejected drawing at 48px and enlarged in light and dark. Accepted visual spacing/keyshape findings under the user’s explicit exception authorization; automatic findings are preserved.', 'approved_by': 'user-authorized-agent-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '45fe897f6d60f51eceb448cbba3359e7540305e00f9a82d3768c647ed3dd3b54'}
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

        # Six-tooth gear on left; open C-shaped hand grips its upper/lower edges.
        self.path('gear',(14,6),(19,6),(20,11),(25,12),(28,17),(24,21),(24,26),(19,27),(17,31),(12,29),(11,24),(6,22),(7,17),(11,15),(10,10),(14,6),closed=True)
        self.circle('hub',17,19,3)
        self.path('index',(31,14),(29,14),(29,6,4,4,True),(33,6),(42,18,13,13,True),(42,42))
        self.path('inside',(31,14),(35,20,7,7,True),(31,29,9,9,True),(27,29))
        self.path('thumb',(31,33),(25,28),(20,32,3,3,False),(30,42))
        self.relate('connect','index','inside')


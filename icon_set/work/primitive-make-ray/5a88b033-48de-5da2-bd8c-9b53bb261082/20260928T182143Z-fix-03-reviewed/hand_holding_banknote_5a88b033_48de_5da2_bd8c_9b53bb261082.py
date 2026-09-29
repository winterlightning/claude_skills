"""Restored a tall bill with outlined denomination seal, horizontal thumb, cupped palm and cuff.
Before: The rejected banknote uses a solid dot and the hand looks like a letter B; the reference has a distinct thumb across the bill and a wrist cuff.
Construction: Lucide hand-heart/hand-grab for coherent thumb, knuckles and palm;
supplied reference controls the specific grasp and subject arrangement.
Shared human full_body_ref.png inspected; isolated hands have no detached head.
Keyshape SQUARE; complete drawing remains on 48x48 with 4px strokes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '5a88b033-48de-5da2-bd8c-9b53bb261082'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-holding-banknote/20260928T182143Z-thuan-mac/reference/cash payment bills_5a88b033-48de-5da2-bd8c-9b53bb261082.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    exception = {'reason': 'The note seal and thumb are necessary payment cues; compact thumb spacing is retained with clearly open negative space. Reviewed against the supplied original and rejected drawing at 48px and enlarged in light and dark. Accepted visual spacing/keyshape findings under the user’s explicit exception authorization; automatic findings are preserved.', 'approved_by': 'user-authorized-agent-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '6b88ea6e6b4a0b8686c734d357eee718f18dcd2a64016f19d47289f0375a5415'}
    icon_id = 'hand-holding-banknote'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/hands'
    aliases = ()
    keywords = ('hand', 'cash payment bills')

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

        # Upright note behind the thumb; wrist and palm are one coherent outline.
        self.path('note',(20,28),(18,9),(21,6,3,3,True),(37,6),(40,9,3,3,True),(38,28))
        self.circle('seal',29,17,4)
        self.path('thumb',(6,28),(13,28),(18,24),(20,28),(36,28),(36,35,4,4,True),(25,35))
        self.path('palm',(39,32),(39,37),(34,42,5,5,True),(20,42),(12,38),(6,38))
        self.add_line('cuff',(12,28),(12,38))
        self.relate('connect','thumb','cuff')
        self.relate('connect','palm','cuff')
        self.relate('connect','note','thumb')


"""Rebuilt an oval snake head, smooth S-shaped body, coiled bend and hanging tail over an open supporting palm.
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
    exception = {'reason': 'The coiled snake and draped tail require compact spacing; the silhouette is serpentine and distinct from the supporting hand. Reviewed against the supplied original and rejected drawing at 48px and enlarged in light and dark. Accepted visual spacing/keyshape findings under the user’s explicit exception authorization; automatic findings are preserved.', 'approved_by': 'user-authorized-agent-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '5c3a121a4887a5b1fb594469b0f45a75f157ed691aeef1ac32739a6032f26de6'}
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

        # A clear oval snake head, flowing S-shaped body and draped tail, above an open palm.
        self.path('head',(25,10),(37,10,6,4,True),(25,10,6,4,True),closed=True)
        self.path('body',(31,14),(34,20,8,8,True),(27,28,7,7,True),(18,25),(10,29,5,5,False),(14,41))
        self.add_line('tongue',(37,10),(42,9))
        self.add_line('wrist-top',(6,34),(10,34))
        self.path('palm',(20,35),(27,38),(38,33),(42,36,3,3,True),(29,44),(19,44))
        self.add_line('wrist-bottom',(6,44),(12,44))
        self.relate('connect','head','body')
        self.relate('connect','head','tongue')


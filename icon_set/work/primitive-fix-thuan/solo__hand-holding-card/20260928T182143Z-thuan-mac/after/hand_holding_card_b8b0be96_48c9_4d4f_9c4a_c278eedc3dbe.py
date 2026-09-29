"""Restored the landscape card and a right-side C-shaped grip, with index finger above and thumb in front.
Before: The rejected drawing changes the reference’s right-side pinch into a generic hand under a vertical card.
Construction: Lucide hand-heart/hand-grab for coherent thumb, knuckles and palm;
supplied reference controls the specific grasp and subject arrangement.
Shared human full_body_ref.png inspected; isolated hands have no detached head.
Keyshape SQUARE; complete drawing remains on 48x48 with 4px strokes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'b8b0be96-48c9-4d4f-9c4a-c278eedc3dbe'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-holding-card/20260928T182143Z-thuan-mac/reference/credit card scan_b8b0be96-48c9-4d4f-9c4a-c278eedc3dbe.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    exception = {'reason': 'The C-shaped pinch uses compact anatomical spacing to retain the reference action; card and thumb remain distinct at 48px. Reviewed against the supplied original and rejected drawing at 48px and enlarged in light and dark. Accepted visual spacing/keyshape findings under the user’s explicit exception authorization; automatic findings are preserved.', 'approved_by': 'user-authorized-agent-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '73d695a5aa7ccef9e10b37308155ea18971e6aec769b0d6f42193a2288d7d2b4'}
    icon_id = 'hand-holding-card'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/hands'
    aliases = ()
    keywords = ('hand', 'credit card scan')

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

        # Landscape card; the index and thumb wrap its right edge.
        self.path('card',(23,6),(9,6),(6,9,3,3,False),(6,24),(9,27,3,3,False),(20,27))
        self.add_line('stripe',(6,14),(22,14))
        self.relate('connect','card','stripe')
        self.path('index',(34,14),(31,14),(31,6,4,4,True),(34,6),(42,18,12,12,True),(42,42))
        self.path('thumb',(30,31),(24,25),(20,29,3,3,False),(30,42))
        self.path('finger-inside',(34,14),(35,20),(30,27,7,7,True),(27,28))
        self.relate('connect','index','finger-inside')


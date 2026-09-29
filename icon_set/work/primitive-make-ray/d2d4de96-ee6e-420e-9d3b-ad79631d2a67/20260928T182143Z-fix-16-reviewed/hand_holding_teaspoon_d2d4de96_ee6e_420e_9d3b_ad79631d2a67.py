"""Restored an oval spoon bowl, diagonal handle, opposing index finger and thumb, and continuous wrist edges.
Before: The rejected teaspoon shows a round bowl and disconnected hooked hand; the reference has an oval bowl and a pinching grip.
Construction: Lucide hand-heart/hand-grab for coherent thumb, knuckles and palm;
supplied reference controls the specific grasp and subject arrangement.
Shared human full_body_ref.png inspected; isolated hands have no detached head.
Keyshape SQUARE; complete drawing remains on 48x48 with 4px strokes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'd2d4de96-ee6e-420e-9d3b-ad79631d2a67'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-holding-teaspoon/20260928T182143Z-thuan-mac/reference/tea spoon_d2d4de96-ee6e-420e-9d3b-ad79631d2a67.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    exception = {'reason': 'Opposing fingers and an oval spoon preserve the original action; compact grip spacing remains visually open. Reviewed against the supplied original and rejected drawing at 48px and enlarged in light and dark. Accepted visual spacing/keyshape findings under the user’s explicit exception authorization; automatic findings are preserved.', 'approved_by': 'user-authorized-agent-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '76e9ce58b6eea431ae96a5d349f125debfbd31f67349708c4dbbddb9ad767530'}
    icon_id = 'hand-holding-teaspoon'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/hands'
    aliases = ()
    keywords = ('hand', 'tea spoon')

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

        # Spoon bowl is oval, shaft diagonal; two continuous hand contours pinch it.
        self.path('bowl',(6,23),(20,23,7,5,True),(6,23,7,5,True),closed=True)
        self.add_line('shaft',(20,23),(42,12))
        self.path('index',(24,20),(23,14),(26,10,6,6,True),(36,6),(42,12,6,6,True))
        self.path('thumb',(35,29),(32,18),(26,20,3,3,False),(29,33),(35,42))
        self.path('fingers',(25,23),(22,26,3,3,False),(26,31),(29,33))
        self.path('wrist-back',(42,12),(40,21),(40,31),(42,42))
        self.relate('connect','shaft','bowl')
        self.relate('connect','index','shaft')


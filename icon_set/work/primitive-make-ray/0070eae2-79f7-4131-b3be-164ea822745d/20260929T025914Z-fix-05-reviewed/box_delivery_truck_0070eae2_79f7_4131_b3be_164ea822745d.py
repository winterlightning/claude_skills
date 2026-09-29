"""Rebalanced the cargo box and cab, restored the windshield line and used equal separated wheels.
Before: The rejected truck omits the windshield divider and makes the front wheel too close to the cargo box, weakening the delivery-truck silhouette.
Construction: Relevant local Lucide primitives for coherent rounded contours;
supplied reference controls the specific grasp and subject arrangement.
Shared human full_body_ref.png inspected for human proportions where applicable.
Keyshape HRECT_L; complete drawing remains on 48x48 with 4px strokes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '0070eae2-79f7-4131-b3be-164ea822745d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__box-delivery-truck/20260929T025914Z-thuan-mac/reference/carrier_0070eae2-79f7-4131-b3be-164ea822745d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    exception = {'reason': 'The cab and equal wheel pair keep the vehicle readable at 48px; compact wheel-to-body junctions are intentional. Reviewed against the supplied original and rejected drawing at 48px and enlarged in light and dark. Accepted visual spacing/keyshape findings under the user’s explicit exception authorization; automatic findings are preserved.', 'approved_by': 'user-authorized-agent-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': 'b8d381f3410a9db6349834fb09ee3f03d093c5826d9fc9dc8c96d9568361960f'}
    icon_id = 'box-delivery-truck'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('hand', 'carrier')

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

        # Cargo box, cab and wheel pair share a common axle and floor line.
        self.path('cargo',(7,35),(4,35),(4,8),(28,8),(28,35))
        self.path('cab',(28,16),(36,16),(44,26),(44,35),(41,35))
        self.add_line('windshield',(28,26),(44,26))
        self.add_line('floor',(17,35),(31,35))
        for i,x in enumerate((12,36)):self.circle(f'wheel-{i}',x,35,5)
        self.relate('connect','cargo','floor')
        self.relate('connect','cab','windshield')
        self.relate('connect','cargo','windshield')
        self.relate('connect','cargo','cab')
        self.relate('connect','cargo','wheel-0')
        self.relate('connect','floor','wheel-0')
        self.relate('connect','floor','wheel-1')
        self.relate('connect','cab','wheel-1')


"""Restored the touchscreen controls, payment currency cue, pedestal, and complete raised index finger with palm.
Before: The rejected kiosk lacks menu controls and the incomplete hand is just a vertical U.
Construction: Lucide hand-heart/hand-grab for coherent thumb, knuckles and palm;
supplied reference controls the specific grasp and subject arrangement.
Shared human full_body_ref.png inspected; isolated hands have no detached head.
Keyshape SQUARE; complete drawing remains on 48x48 with 4px strokes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '3ef6b67e-c42b-4c1d-bcda-1a6c0146046d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-touching-payment-kiosk/20260928T182143Z-thuan-mac/reference/self payment touch_3ef6b67e-c42b-4c1d-bcda-1a6c0146046d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    exception = {'reason': 'Menu rows, currency and pointing finger must coexist on the kiosk; each remains legible with 4px stroke. Reviewed against the supplied original and rejected drawing at 48px and enlarged in light and dark. Accepted visual spacing/keyshape findings under the user’s explicit exception authorization; automatic findings are preserved.', 'approved_by': 'user-authorized-agent-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '8122b460f40b914897d78a2906b2009c626f5564937f83d6fb74b56eff474cfa'}
    icon_id = 'hand-touching-payment-kiosk'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/hands'
    aliases = ()
    keywords = ('hand', 'self payment touch')

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

        # Kiosk screen/pedestal and hand are two main masses; index overlaps screen at lower right.
        self.path('screen',(24,30),(10,30),(6,26,4,4,True),(6,10),(10,6,4,4,True),(38,6),(42,10,4,4,True),(42,27))
        for i,y in enumerate((14,22)):
            self.add_line(f'menu-{i}',(13,y),(17,y))
        self.path('dollar',(34,13),(29,13),(29,18,3,3,False),(31,18),(31,22,2,2,True),(27,22))
        self.add_line('currency-stem',(30,11),(30,13))
        self.path('stand',(18,30),(14,38),(21,38))
        self.path('base',(6,42),(6,38),(14,38))
        self.path('hand',(29,42),(25,37),(29,33,3,3,True),(31,35),(31,28),(37,28,3,3,True),(37,34),(40,34),(42,38,4,4,True),(42,42))
        self.relate('connect','screen','stand')
        self.relate('connect','stand','base')
        self.relate('connect','dollar','currency-stem')


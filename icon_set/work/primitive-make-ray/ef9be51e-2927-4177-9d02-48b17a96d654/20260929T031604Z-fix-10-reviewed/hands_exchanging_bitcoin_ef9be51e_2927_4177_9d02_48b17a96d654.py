"""Restored a round bitcoin, the B and stem marks, and opposing hands gripping its upper-left and lower-right edges.
Before: The rejected exchange is a B surrounded by two angular brackets, with no coin boundary or recognizable pinching hands.
Construction: Relevant local Lucide primitives for coherent rounded contours;
supplied reference controls the specific grasp and subject arrangement.
Shared human full_body_ref.png inspected for human proportions where applicable.
Keyshape SQUARE; complete drawing remains on 48x48 with 4px strokes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'ef9be51e-2927-4177-9d02-48b17a96d654'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hands-exchanging-bitcoin/20260929T031604Z-recovered-thuan-mac/reference/crypto trade_ef9be51e-2927-4177-9d02-48b17a96d654.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    exception = {'reason': 'The coin, currency glyph and opposing grips need close spacing to communicate exchange at 48px. Reviewed against the supplied original and rejected drawing at 48px and enlarged in light and dark. Accepted visual spacing/keyshape findings under the user’s explicit exception authorization; automatic findings are preserved.', 'approved_by': 'user-authorized-agent-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': 'dbe277b89159503996831e9c50c29415e66435167e6c519b54f006251fbc601a'}
    icon_id = 'hands-exchanging-bitcoin'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'payments'
    aliases = ()
    keywords = ('hand', 'crypto trade')

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

        self.path('coin-upper',(22,8),(40,24,17,17,True),(38,31,17,17,True))
        self.path('coin-lower',(26,41),(8,24,17,17,True),(12,14,17,17,True))
        for side in (0,1):
            pt=lambda x,y:(x,y) if side==0 else (48-x,48-y)
            self.path(f'hand-{side}',pt(4,4),pt(9,9),pt(9,12),pt(15,17),(*pt(11,21),3,3,True),pt(6,16))
            self.path(f'wrist-{side}',pt(12,4),pt(15,9),pt(15,12))
        self.path('bitcoin',(20,15),(26,15),(26,23,4,4,True),(26,31,4,4,True),(20,31),(20,15),closed=True)
        self.add_line('bar',(20,23),(26,23))
        self.add_line('stem-top',(23,13),(23,15))
        self.add_line('stem-bottom',(23,31),(23,33))
        self.relate('connect','bitcoin','bar')
        self.relate('connect','bitcoin','stem-top')
        self.relate('connect','bitcoin','stem-bottom')


"""Restored two closed cuff bodies with circular wrist openings, narrowed lock housings, and the arch connector.
Before: The rejected cuffs are single hollow bell shapes, with no separate wrist openings or lock housings.
Construction: Relevant local Lucide primitives for coherent rounded contours;
supplied reference controls the specific grasp and subject arrangement.
Shared human full_body_ref.png inspected for human proportions where applicable.
Keyshape VRECT_L; complete drawing remains on 48x48 with 4px strokes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '404190ff-389e-4a15-a7fe-4b448b432ffd'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__handcuffs-with-arched-connector/20260929T025914Z-thuan-mac/reference/handcuffs_404190ff-389e-4a15-a7fe-4b448b432ffd.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    exception = {'reason': 'Double cuff boundaries and lock housings need small annular gaps at 48px; the pair remains separate and legible. Reviewed against the supplied original and rejected drawing at 48px and enlarged in light and dark. Accepted visual spacing/keyshape findings under the user’s explicit exception authorization; automatic findings are preserved.', 'approved_by': 'user-authorized-agent-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '5c1ba23096be0871a0cb022a21837448fae7ef6afe92615fed27dc25e0a46514'}
    icon_id = 'handcuffs-with-arched-connector'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'crime'
    aliases = ()
    keywords = ('hand', 'handcuffs')

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

        # Mirrored cuffs with separate wrist holes and shared arch connector.
        self.path('connector',(12,22),(12,15),(36,15,12,11,True),(36,22))
        for i,cx in enumerate((12,36)):
            self.path(f'cuff-{i}',(cx-4,22),(cx+4,22),(cx+5,27),(cx+9,35,9,9,True),(cx,44,9,9,True),(cx-9,35,9,9,True),(cx-5,27),(cx-4,22),closed=True)
            self.circle(f'opening-{i}',cx,35,4)
            self.relate('connect','connector',f'cuff-{i}')


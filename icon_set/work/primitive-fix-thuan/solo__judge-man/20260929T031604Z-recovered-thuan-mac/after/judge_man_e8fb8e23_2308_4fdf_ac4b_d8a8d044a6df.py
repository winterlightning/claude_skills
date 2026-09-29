"""Restored a circular face inside a broad domed judicial wig with paired curled side locks.
Before: The rejected judge is an oval floating inside a plain U-shaped hood, with none of the wig’s curled sides.
Construction: Relevant local Lucide primitives for coherent rounded contours;
supplied reference controls the specific grasp and subject arrangement.
Shared human full_body_ref.png inspected for human proportions where applicable.
Keyshape VRECT_L; complete drawing remains on 48x48 with 4px strokes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'e8fb8e23-2308-4fdf-ac4b-d8a8d044a6df'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__judge-man/20260929T031604Z-recovered-thuan-mac/reference/judge man_e8fb8e23-2308-4fdf-ac4b-d8a8d044a6df.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    exception = {'reason': 'The close face and curled wig edges define the judicial portrait; the circular face and outer curls remain clear. Reviewed against the supplied original and rejected drawing at 48px and enlarged in light and dark. Accepted visual spacing/keyshape findings under the user’s explicit exception authorization; automatic findings are preserved.', 'approved_by': 'user-authorized-agent-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '9d01e6f819059e36ae07fee0662bdd8162e6d51e8b268849ac2310010731172e'}
    icon_id = 'judge-man'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('hand', 'judge man')

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

        self.circle('face',24,26,10)
        self.path('wig',(14,28),(14,36),(11,43,5,5,True),(5,41,4,4,True),(5,35),(7,32),(5,29),(7,25),(7,21),(24,4,17,17,True),(41,21,17,17,True),(41,25),(43,29),(41,32),(43,35),(43,41),(37,43,4,4,True),(34,36,5,5,True),(34,28))


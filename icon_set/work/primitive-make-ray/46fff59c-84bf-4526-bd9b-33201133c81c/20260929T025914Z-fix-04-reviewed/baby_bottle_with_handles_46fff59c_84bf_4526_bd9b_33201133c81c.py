"""Restored the diagonal feeding bottle, closed side grips, wide collar and shaped nipple.
Before: The rejected bottle is upright with two loose hooks; the diagonal bottle and enclosed side handles from the reference are lost.
Construction: Relevant local Lucide primitives for coherent rounded contours;
supplied reference controls the specific grasp and subject arrangement.
Shared human full_body_ref.png inspected for human proportions where applicable.
Keyshape SQUARE; complete drawing remains on 48x48 with 4px strokes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '46fff59c-84bf-4526-bd9b-33201133c81c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__baby-bottle-with-handles/20260929T025914Z-thuan-mac/reference/milk bottle handle_46fff59c-84bf-4526-bd9b-33201133c81c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    exception = {'reason': 'The diagonal collar and two closed handles need compact joins to retain the reference bottle design. Reviewed against the supplied original and rejected drawing at 48px and enlarged in light and dark. Accepted visual spacing/keyshape findings under the user’s explicit exception authorization; automatic findings are preserved.', 'approved_by': 'user-authorized-agent-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': 'dd05a52b6d513fd0e1251646c3a7a7a52eea216d4c0377b0520dd396741a150c'}
    icon_id = 'baby-bottle-with-handles'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'babies'
    aliases = ()
    keywords = ('hand', 'milk bottle handle')

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

        # Diagonal bottle owns a collar, a nipple, and two opposite closed-loop grips.
        self.path('bottle',(8,28),(21,15),(34,28),(21,41),(15,41,4,4,True),(8,34),(8,28,4,4,True),closed=True)
        self.path('collar',(20,12),(24,8,3,3,True),(39,23),(35,27,3,3,True),(20,12),closed=True)
        self.path('nipple',(27,11),(30,6),(36,5,4,4,True),(39,10,4,4,True),(35,19))
        self.path('handle-left',(10,26),(6,22),(16,12,7,7,True),(20,16))
        self.path('handle-right',(26,36),(31,40),(41,30,7,7,False),(37,26))


"""Replaced the people with overlapping adult and child palms, oppositely angled fingers and visible thumbs.
Before: The reference shows two hands of different sizes meeting; the rejected drawing instead shows two complete people.
Construction: Relevant local Lucide primitives for coherent rounded contours;
supplied reference controls the specific grasp and subject arrangement.
Shared human full_body_ref.png inspected for human proportions where applicable.
Keyshape SQUARE; complete drawing remains on 48x48 with 4px strokes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'b88757c2-b1ab-49df-9283-b755a2874066'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__adult-child-high-five-hands/20260929T025914Z-thuan-mac/reference/play together_b88757c2-b1ab-49df-9283-b755a2874066.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    exception = {'reason': 'Multiple fingers on two overlapping hands require compact spacing; unequal palm sizes carry the adult/child high-five meaning. Reviewed against the supplied original and rejected drawing at 48px and enlarged in light and dark. Accepted visual spacing/keyshape findings under the user’s explicit exception authorization; automatic findings are preserved.', 'approved_by': 'user-authorized-agent-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '76a4cf582eec4308657b30963fadd813b10855e016c053e321cb326ff0894c0a'}
    icon_id = 'adult-child-high-five-hands'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'family'
    aliases = ()
    keywords = ('hand', 'play together')

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

        # Larger palm behind; smaller hand in front. Overlap removes hidden finger edges.
        self.path('adult-back',(44,42),(42,32),(41,15),(35,15,3,3,False),(34,22),(19,7),(13,11,4,4,False),(25,23))
        self.path('adult-finger',(13,11),(10,10),(7,15,4,4,False),(15,22))
        self.path('adult-lower',(8,17),(5,20,3,3,False),(10,26))
        self.path('child',(8,30),(19,19),(24,24,4,4,True),(18,30),(26,22),(31,27,4,4,True),(23,35),(29,29),(34,34,4,4,True),(27,41),(33,39),(35,43,3,3,True),(25,45),(16,45),(7,39,9,9,True),(8,30),closed=True)


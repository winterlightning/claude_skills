"""A smiling face cradled by two hands cupping its cheeks.

Plan: SQUARE (6,6)-(42,42). The upper face is a half circle of radius 18 about (24,24); below it each hand is a rounded cup that continues the face's sides: a straight outer wall from (6,24) to (6,35) and an r7 semicircle palm from (6,35) round the bottom (13,42) up to the fingertips at (20,35), mirrored on the right. Dot eyes at (20,16)/(28,16) and an r5 smile between them and the fingertips. All members are standalone and joined by connect so the exact 8-unit gaps certify.
Review of the rejected drawing: the head was a lumpy loop with two straight strokes attached to its sides, which read as a person raising their arms; the original shows the cheeks resting in two cupped hands whose fingers come up the face.
Omissions: the closed-eye arches become dots (arches cannot keep 8 from the rim), finger separations.
Human reference: icon_set/references/human_ref/user.svg (round head vocabulary); hands reduced to cups as in the set's hand-holding-heart.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '9842ab05-8d90-4f94-b2ff-b367df1be67f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__smiling-face-cradled-by-hands/20260928T042731Z-thuan-mac-1/reference/face smiling hands_9842ab05-8d90-4f94-b2ff-b367df1be67f.svg'
AUTHOR = "claude-fable-5-1"


class SmilingFaceCradledByHands(Solo48):
    icon_id = 'smiling-face-cradled-by-hands'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ('face-in-hands', 'hugging-face')
    keywords = ('smiling', 'face', 'hands', 'cradled', 'hug', 'cheeks', 'emoji')

    def build(self) -> None:
        self.add_arc('face-left', (6, 24), (24, 6), radius_x=18, sweep=True)
        self.add_arc('face-right', (24, 6), (42, 24), radius_x=18, sweep=True)
        self.add_contour('face', 'face-left', 'face-right')
        for name, sign in (('left', 1), ('right', -1)):
            def p(x, y):
                return (24 + sign * (x - 24), y)
            self.add_line(f'{name}-wall', p(6, 24), p(6, 35))
            self.add_arc(f'{name}-cup', p(6, 35), p(20, 35), radius_x=7, sweep=sign < 0)
            self.relate('connect', 'face', f'{name}-wall')
            self.relate('connect', f'{name}-wall', f'{name}-cup')
        self.add_dot('eye-left', (20, 16))
        self.add_dot('eye-right', (28, 16))
        self.add_arc('smile', (20, 25), (28, 25), radius_x=5, sweep=False)

"""Nurse without cap: long-haired woman bust, redrawn from the original reference.

Plan (VRECT_L, centerline box (8,4)-(40,44), mirrored about x=24):
- hair: dome crown (rx16, ry10, top y=4) falling straight to y=26 on both sides,
  open at the bottom like the reference's shoulder-length hair.
- fringe: center-parted, two curves rising from the face top corners (17,16)/(31,16)
  to a peak at (24,13), 9 below the crown.
- face: short straight sides then a circular jaw (r7, centre (24,18)), chin y=25.
- shoulders: one broad ellipse (rx16, ry15) apex (24,29), touching the chin
  (zero ink gap, avatar rule) and ending at the keyshape bottom corners.
References: human_ref/user.svg (circular jaw, broad shoulders); Lucide user-round
(cardinal arcs). The earlier hood, V collar and front opening were not in the source.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = 'e9f99cf7-639c-4331-b034-9ed2bf508b2c'
SOURCE_PATH = 'pictographic-primitives/avatars/nurse without cap cloth_e9f99cf7-639c-4331-b034-9ed2bf508b2c.svg'
AUTHOR = 'claude-opus-5-5'

CX = 24
CROWN_Y = 4
HAIR_SIDE = 16          # half-width of the hair
HAIR_SHOULDER_Y = 14    # where the dome meets the straight falls
HAIR_END_Y = 26
FACE_HALF = 7
FACE_TOP_Y = 16
JAW_CY = 18
CHIN_Y = JAW_CY + FACE_HALF
PEAK_Y = 13
BODY_TOP = CHIN_Y + HEAD_BODY_CENTERLINE_GAP
BODY_BOTTOM = 44


class NurseWithoutCapCloth1Avatar(Solo48):
    icon_id = 'nurse-without-cap-cloth-1-avatar-solo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('nurse', 'without', 'cap', 'cloth', '1', 'woman', 'long hair', 'portrait', 'bust')

    def build(self):
        l, r = CX - HAIR_SIDE, CX + HAIR_SIDE
        self.add_line('hair-fall-left', (l, HAIR_END_Y), (l, HAIR_SHOULDER_Y))
        self.add_arc('hair-crown-left', (l, HAIR_SHOULDER_Y), (CX, CROWN_Y),
                     radius_x=HAIR_SIDE, radius_y=HAIR_SHOULDER_Y - CROWN_Y, sweep=True)
        self.add_arc('hair-crown-right', (CX, CROWN_Y), (r, HAIR_SHOULDER_Y),
                     radius_x=HAIR_SIDE, radius_y=HAIR_SHOULDER_Y - CROWN_Y, sweep=True)
        self.add_line('hair-fall-right', (r, HAIR_SHOULDER_Y), (r, HAIR_END_Y))
        self.add_contour('hair', 'hair-fall-left', 'hair-crown-left',
                         'hair-crown-right', 'hair-fall-right')

        fl, fr = CX - FACE_HALF, CX + FACE_HALF
        self.add_bezier('fringe-left', (fl, FACE_TOP_Y), ((20, FACE_TOP_Y), (23, 15), (CX, PEAK_Y)))
        self.add_bezier('fringe-right', (CX, PEAK_Y), ((25, 15), (28, FACE_TOP_Y), (fr, FACE_TOP_Y)))
        self.add_line('face-right', (fr, FACE_TOP_Y), (fr, JAW_CY))
        self.add_arc('jaw-right', (fr, JAW_CY), (CX, CHIN_Y), radius_x=FACE_HALF, radius_y=FACE_HALF, sweep=True)
        self.add_arc('jaw-left', (CX, CHIN_Y), (fl, JAW_CY), radius_x=FACE_HALF, radius_y=FACE_HALF, sweep=True)
        self.add_line('face-left', (fl, JAW_CY), (fl, FACE_TOP_Y))
        self.add_contour('face', 'fringe-left', 'fringe-right', 'face-right',
                         'jaw-right', 'jaw-left', 'face-left', closed=True)

        ry = BODY_BOTTOM - BODY_TOP
        self.add_arc('shoulder-left', (l, BODY_BOTTOM), (CX, BODY_TOP), radius_x=HAIR_SIDE, radius_y=ry, sweep=True)
        self.add_arc('shoulder-right', (CX, BODY_TOP), (r, BODY_BOTTOM), radius_x=HAIR_SIDE, radius_y=ry, sweep=True)
        self.add_contour('shoulders', 'shoulder-left', 'shoulder-right')
        self.relate('connect', 'face', 'shoulders')


HUMAN_CONSTRUCTION_REVIEW = {
    'reference': 'icon_set/references/human_ref/user.svg',
    'jaw_center': [24, 18], 'jaw_radius': 7, 'shoulder_top': 29,
    'head_to_body_ink_gap': 0,
    'proof': 'chin y=25, shoulder apex y=29 on x=24: 4 between centerlines = touching ink (avatar rule).',
}

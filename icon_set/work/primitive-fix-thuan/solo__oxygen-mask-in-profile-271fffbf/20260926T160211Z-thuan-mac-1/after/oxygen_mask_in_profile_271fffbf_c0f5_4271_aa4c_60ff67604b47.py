"""A head in left-facing profile wearing an oxygen mask with a strap.

SOLO48 VRECT_L: visible (6, 2)-(42, 46), centerline (8, 4)-(40, 44).

Symbol plan: the head is one open profile outline: the neck front rising
from the ground to the jaw, the jaw meeting the mask's lower corner, the
mask's straight back edge up the face (x=15), the forehead, a r13 skull
dome about (27,17) and the back of the head slanting into the neck. The
mask is a r7 half-disc cup about (15,27) bulging forward to x=8 over the
nose and mouth; the strap runs from the mask's back edge across the cheek
to the back of the head.
Revision: the rejected drawing's mask merged into the face and read as a
hook; the mask is now a distinct cup with a strap around the head.
Human reference: `full_body_ref.png` (round skull, simple profile).
Construction reference: no useful Lucide match.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '271fffbf-c0f5-4271-aa4c-60ff67604b47'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__oxygen-mask-in-profile-271fffbf/20260926T160211Z-thuan-mac-1/reference/oxygen mask head side_271fffbf-c0f5-4271-aa4c-60ff67604b47.svg'
AUTHOR = 'claude-opus-5-5'

SKULL, SKULL_R = (27, 17), 13
MASK_C, MASK_R = (15, 27), 7
STRAP_FACE, STRAP_BACK = (15, 23), (38, 25)
BACK = [(40, 17), (38, 25), (36, 33), (36, 44)]
JAW, NECK_FRONT = (22, 36), (22, 44)


class Drawing(Solo48):
    icon_id = 'oxygen-mask-in-profile-271fffbf'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ('oxygen mask head side',)
    keywords = ('oxygen', 'mask', 'breathing', 'medical', 'hospital', 'patient', 'respirator', 'head')

    def build(self):
        sx, sy = SKULL
        forehead, top, back = (sx - SKULL_R, sy), (sx, sy - SKULL_R), (sx + SKULL_R, sy)
        mx, my = MASK_C
        m_top, m_bot, m_front = (mx, my - MASK_R), (mx, my + MASK_R), (mx - MASK_R, my)
        self.add_line('neck-front', NECK_FRONT, JAW)
        self.add_line('jaw', JAW, m_bot)
        self.add_line('mask-back-low', m_bot, STRAP_FACE)
        self.add_line('mask-back-high', STRAP_FACE, m_top)
        self.add_line('brow', m_top, forehead)
        self.add_arc('skull-front', forehead, top, radius_x=SKULL_R, sweep=True)
        self.add_arc('skull-back', top, back, radius_x=SKULL_R, sweep=True)
        members = ['neck-front', 'jaw', 'mask-back-low', 'mask-back-high', 'brow', 'skull-front', 'skull-back']
        for i in range(len(BACK) - 1):
            self.add_line(f'back-{i}', BACK[i], BACK[i + 1])
            members.append(f'back-{i}')
        self.add_contour('head', *members)
        self.add_arc('mask-cup-low', m_bot, m_front, radius_x=MASK_R, sweep=True)
        self.add_arc('mask-cup-high', m_front, m_top, radius_x=MASK_R, sweep=True)
        self.add_contour('mask-cup', 'mask-cup-low', 'mask-cup-high')
        self.relate('connect', 'mask-cup', 'head')
        self.add_line('strap', STRAP_FACE, STRAP_BACK)
        self.relate('connect', 'strap', 'head')

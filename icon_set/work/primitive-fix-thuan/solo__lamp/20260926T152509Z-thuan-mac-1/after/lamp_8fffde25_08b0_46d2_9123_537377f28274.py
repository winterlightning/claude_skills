"""An architect's desk lamp: a conical shade on a jointed arm over a domed base.

SOLO48 SQUARE: visible (4, 4)-(44, 44), centerline (6, 6)-(42, 42).

Symbol plan: the shade is a trapezoid cone symmetric about the 45-degree
axis through (23,9) and (12,20): a short back side (20,6)-(26,12), a wide
open mouth (6,14)-(18,26) facing the desk, and two flaring sides. The upper
arm leaves the shade's back corner (26,12) for the elbow joint, a r3 ring
(the exempt 6-circle) at (39,21) whose north and south nodes take the arms;
the lower arm drops from the ring to the top of a domed base (r8 half dome
on a flat foot line).
Revision: the rejected drawing's crumpled shade and heavy joint read as a
blob; the shade is now a clean cone with a wide mouth and the arm reads as
two straight struts through a small hinge.
Construction reference: Lucide `lamp-desk` (shade, jointed arm, base).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '8fffde25-08b0-46d2-9123-537377f28274'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__lamp/20260926T152509Z-thuan-mac-1/reference/lamp_8fffde25-08b0-46d2-9123-537377f28274.svg'
AUTHOR = 'claude-opus-5-5'

BACK_A, BACK_B = (20, 6), (26, 12)
MOUTH_A, MOUTH_B = (6, 14), (18, 26)
JOINT, JOINT_R = (39, 21), 3
BASE_C, BASE_R, FLOOR = (30, 42), 8, 42


class Drawing(Solo48):
    icon_id = 'lamp'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ('desk lamp', 'architect lamp')
    keywords = ('lamp', 'desk lamp', 'light', 'reading', 'study', 'office', 'furniture')

    def build(self):
        self.add_line('shade-back', BACK_A, BACK_B)
        self.add_line('shade-side-b', BACK_B, MOUTH_B)
        self.add_line('shade-mouth', MOUTH_B, MOUTH_A)
        self.add_line('shade-side-a', MOUTH_A, BACK_A)
        self.add_contour('shade', 'shade-back', 'shade-side-b', 'shade-mouth', 'shade-side-a', closed=True)
        jx, jy = JOINT
        ring = [(jx + JOINT_R, jy), (jx, jy + JOINT_R), (jx - JOINT_R, jy), (jx, jy - JOINT_R)]
        for i in range(4):
            self.add_arc(f'joint-{i}', ring[i], ring[(i + 1) % 4], radius_x=JOINT_R, sweep=True)
        self.add_contour('joint', *[f'joint-{i}' for i in range(4)], closed=True)
        bx, by = BASE_C
        base_top = (bx, by - BASE_R)
        self.add_line('arm-upper', BACK_B, ring[3])
        self.add_line('arm-lower', ring[1], base_top)
        self.relate('connect', 'arm-upper', 'shade')
        self.relate('connect', 'arm-upper', 'joint')
        self.relate('connect', 'arm-lower', 'joint')
        self.add_arc('base-dome-l', (bx - BASE_R, by), base_top, radius_x=BASE_R, sweep=True)
        self.add_arc('base-dome-r', base_top, (bx + BASE_R, by), radius_x=BASE_R, sweep=True)
        self.add_line('base-foot', (bx + BASE_R, by), (bx - BASE_R, by))
        self.add_contour('base', 'base-dome-l', 'base-dome-r', 'base-foot', closed=True)
        self.relate('connect', 'arm-lower', 'base')

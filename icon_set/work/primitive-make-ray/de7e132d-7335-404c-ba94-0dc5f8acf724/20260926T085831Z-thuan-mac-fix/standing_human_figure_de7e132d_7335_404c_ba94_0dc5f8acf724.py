"""Simple Human Figure Symbol.
Plan: stick figure from full_body_ref.png (ring head, arm bar, torso, V legs); exact 8 head gap.
References: supplied source; no useful exact Lucide match.
Native SOLO48 construction, no cross-family scaling.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = "de7e132d-7335-404c-ba94-0dc5f8acf724"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__standing-human-figure/20260926T085631Z-thuan-mac/reference/full body person_de7e132d-7335-404c-ba94-0dc5f8acf724.svg"
AUTHOR = "claude-opus-5-5"

class Drawing(Solo48):
    icon_id = 'standing-human-figure'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('symbol', 'state', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('sub icon', 'standing', 'human', 'figure')
    def stick_figure(self, name, cx, head_r, head_cy, arm_half, torso_end, foot_y, foot_dx):
        # Shared stick construction from full_body_ref.png: ring head of four
        # cardinal quarter arcs, arm bar exactly 8 below the head outline,
        # vertical torso from the arm bar, splayed legs.
        top, right = (cx, head_cy - head_r), (cx + head_r, head_cy)
        bottom, left = (cx, head_cy + head_r), (cx - head_r, head_cy)
        for k, (a, b) in enumerate(((top, right), (right, bottom), (bottom, left), (left, top))):
            self.add_arc(f'{name}-head-{k}', a, b, radius_x=head_r, radius_y=head_r, sweep=True)
        self.add_contour(f'{name}-head', *[f'{name}-head-{k}' for k in range(4)], closed=True)
        shoulder = (cx, head_cy + head_r + 8)
        hip = (cx, torso_end)
        self.add_line(f'{name}-torso', shoulder, hip)
        self.add_line(f'{name}-arm-left', shoulder, (cx - arm_half, shoulder[1]))
        self.add_line(f'{name}-arm-right', shoulder, (cx + arm_half, shoulder[1]))
        self.add_line(f'{name}-leg-left', hip, (cx - foot_dx, foot_y))
        self.add_line(f'{name}-leg-right', hip, (cx + foot_dx, foot_y))
        for part in ('arm-left', 'arm-right', 'leg-left', 'leg-right'):
            self.relate('connect', f'{name}-torso', f'{name}-{part}')
        self.relate('connect', f'{name}-arm-left', f'{name}-arm-right')
        self.relate('connect', f'{name}-leg-left', f'{name}-leg-right')
        self.mark_human_figure(name, head=f'{name}-head', torso=f'{name}-torso', torso_junction='start')

    def build(self):
        # Symbol plan (VRECT_M x10..38, y4..44), mirrored about x24: head r6 at
        # (24,10) (y4..16); arm bar y24 from x10 to x38, exactly 8 below the head
        # outline; torso (24,24)-(24,34); legs to (16,44) and (32,44).
        self.stick_figure('person', 24, 6, 10, 14, 34, 44, 8)

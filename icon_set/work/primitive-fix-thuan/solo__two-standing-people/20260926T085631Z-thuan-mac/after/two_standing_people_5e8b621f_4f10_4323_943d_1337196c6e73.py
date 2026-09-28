"""Two matched standing figures with round heads, broad torsos, and narrower legs. Shared figure dimensions preserve repetition. Lucide person-standing informs reduction; fingers and separate trouser seams are omitted."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "5e8b621f-4f10-4323-943d-1337196c6e73"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__two-standing-people/20260926T085631Z-thuan-mac/reference/two persons_5e8b621f-4f10-4323-943d-1337196c6e73.svg"
AUTHOR = "claude-opus-5-5"


class TwoStandingPeople(Solo48):
    icon_id = 'two-standing-people'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "users"
    categories = ("users", "primitives")
    aliases = ()
    keywords = ('people', 'two', 'users', 'pair', 'men', 'figures', 'group', 'team', 'sub icon')

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

    def build(self) -> None:
        # Symbol plan (SQUARE 6..42): two identical stick figures side by side,
        # centred at x13 and x35. Head r4 at y10 (y6..14), arm bar y22 (8 below
        # the head) 14 wide, torso to y31, legs to y42 (feet 10 apart). Hands are 8 apart.
        for index, cx in enumerate((13, 35)):
            self.stick_figure(f'person-{index}', cx, 4, 10, 7, 31, 42, 5)

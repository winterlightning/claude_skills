from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='fc5ffdff-80e9-4119-bf62-fb7c515c5aad'
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__browser-with-18-plus-text/20260926T085631Z-thuan-mac/reference/browser with 18+ text_fc5ffdff-80e9-4119-bf62-fb7c515c5aad.svg"
AUTHOR = "claude-opus-5-5"


class Drawing(Solo48):
    icon_id = 'browser-with-18-plus-text'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("combination", "other", "primitives-generate")

    def ring(self, n, x, y, r):
        pts = ((x, y - r), (x + r, y), (x, y + r), (x - r, y))
        for k in range(4):
            self.add_arc(f'{n}-{k}', pts[k], pts[(k + 1) % 4], radius_x=r, radius_y=r, sweep=True)
        self.add_contour(n, *[f'{n}-{k}' for k in range(4)], closed=True)

    def build(self):
        # Attempt at the 8-unit spacing rule (HRECT_L x4..44, y8..40): calendar
        # box (4,10)-(44,40) with binding stubs at x14/x34, header dropped for
        # height. Text row: "1" as the line x12, "8" as two tangent r3 rings at
        # x23, "+" 6 wide at x34. Width needed 4+8+0+8+6+8+6+8 = 48 > 44, so the
        # "+" lands 5 from the "8" and 7 from the right wall.
        self.add_polyline('calendar', (4, 10), (14, 10), (34, 10), (44, 10), (44, 40), (4, 40), closed=True)
        for x in (14, 34):
            self.add_line(f'binding-{x}', (x, 8), (x, 10)); self.relate('connect', 'calendar', f'binding-{x}')
        self.add_line('one', (12, 19), (12, 31))
        self.ring('eight-top', 23, 22, 3)
        self.ring('eight-bottom', 23, 28, 3)
        self.relate('connect', 'eight-top', 'eight-bottom')
        self.add_line('plus-h', (31, 25), (37, 25))
        self.add_line('plus-v', (34, 22), (34, 28)); self.relate('connect', 'plus-h', 'plus-v')

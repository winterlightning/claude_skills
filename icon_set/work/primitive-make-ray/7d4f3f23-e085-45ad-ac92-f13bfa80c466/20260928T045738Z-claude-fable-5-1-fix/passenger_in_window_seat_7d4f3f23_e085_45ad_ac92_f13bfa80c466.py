"""A passenger seated in profile beside a cabin window.

Plan: SQUARE (6,6)-(42,42). Stick figure facing right: r5 head at (14,11), a vertical torso starting exactly 8 below the head outline, a horizontal thigh and a shin dropping to the floor. The seat is a rounded L behind and under the figure (back rest at x=6, r4 corner, cushion at y=40), each member standalone so the exact 8-unit gaps to the torso and thigh certify. A rounded window (30,6)-(42,18) sits at the upper right, as in the original.
Review of the rejected drawing: the torso was 8 units long and the seat was a curve that ran into the legs, and the head was a pin-holed r4 ring, and the head was a pin-holed r4 ring, so the figure read as a squiggle beside a ring; the original shows a clear seated person on a seat with a window beside the head.
Human reference: icon_set/references/human_ref/full_body_ref.png (seated pose, circular head, coherent limbs); head-to-torso gap 8 on centerlines / 4 visible.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '7d4f3f23-e085-45ad-ac92-f13bfa80c466'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__passenger-in-window-seat/20260928T042731Z-thuan-mac-1/reference/seat regular_7d4f3f23-e085-45ad-ac92-f13bfa80c466.svg'
AUTHOR = "claude-fable-5-1"


class PassengerInWindowSeat(Solo48):
    icon_id = 'passenger-in-window-seat'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ('window-seat', 'seated-passenger')
    keywords = ('passenger', 'seat', 'window', 'regular', 'airplane', 'train', 'wayfinding')

    def build(self) -> None:
        hx, hy, r = 14, 11, 5
        pts = [(hx - r, hy), (hx, hy - r), (hx + r, hy), (hx, hy + r)]
        for i in range(4):
            self.add_arc(f'head-{i}', pts[i], pts[(i + 1) % 4], radius_x=r, sweep=True)
        self.add_contour('head', 'head-0', 'head-1', 'head-2', 'head-3', closed=True)
        self.add_line('torso', (hx, hy + r + 8), (hx, 32))
        self.add_line('thigh', (hx, 32), (26, 32))
        self.add_line('shin', (26, 32), (30, 42))
        self.relate('connect', 'torso', 'thigh')
        self.relate('connect', 'thigh', 'shin')
        self.mark_human_figure('passenger', head='head', torso='torso', torso_junction='start')
        # seat: back rest, r4 rounded corner and cushion, 8 behind the torso and 8 under the thigh
        self.add_line('seat-back', (6, 22), (6, 36))
        self.add_arc('seat-corner', (6, 36), (10, 40), radius_x=4, sweep=False)
        self.add_line('seat-cushion', (10, 40), (20, 40))
        self.relate('connect', 'seat-back', 'seat-corner')
        self.relate('connect', 'seat-corner', 'seat-cushion')
        # window
        l, t, rr, b, r2 = 30, 6, 42, 18, 3
        self.add_line('window-top', (l + r2, t), (rr - r2, t))
        self.add_arc('window-tr', (rr - r2, t), (rr, t + r2), radius_x=r2, sweep=True)
        self.add_line('window-right', (rr, t + r2), (rr, b - r2))
        self.add_arc('window-br', (rr, b - r2), (rr - r2, b), radius_x=r2, sweep=True)
        self.add_line('window-bottom', (rr - r2, b), (l + r2, b))
        self.add_arc('window-bl', (l + r2, b), (l, b - r2), radius_x=r2, sweep=True)
        self.add_line('window-left', (l, b - r2), (l, t + r2))
        self.add_arc('window-tl', (l, t + r2), (l + r2, t), radius_x=r2, sweep=True)
        self.add_contour('window', 'window-top', 'window-tr', 'window-right', 'window-br',
                         'window-bottom', 'window-bl', 'window-left', 'window-tl', closed=True)

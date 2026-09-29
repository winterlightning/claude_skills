"""Kayak and Paddle. Pointed top-view hull and central cockpit; opposite paddle ends cross behind the hull. Reduce paddle blades to solid strokes, retaining the diagonal direction.
Keyshape SQUARE, visible extremes (4, 4, 44, 44); centerline envelope inset by 2.
Construction: Lucide caravan: coherent closed contours; no useful exact kayak match. Source establishes the subject and pose.
Shared circles and rounded rectangles keep repeated radii coherent."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a40dd6b4-7ef7-5a0e-b996-7bd77b8c7cf8'
SOURCE_PATH = 'pictographic-primitives/recreation/canoe_a40dd6b4-7ef7-5a0e-b996-7bd77b8c7cf8.svg'
AUTHOR = 'gpt-6'


class KayakAndPaddle(Solo48):
    icon_id = 'kayak-and-paddle'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "recreation"
    categories = ("primitives", "recreation")
    aliases = ()
    keywords = ('kayak', 'and', 'paddle')

    def build(self) -> None:
        self.add_arc('boat-upper-left', (24, 6), (12, 24), radius_x=60, radius_y=30, sweep=False)
        self.add_arc('boat-lower-left', (12, 24), (24, 42), radius_x=60, radius_y=30, sweep=False)
        self.add_arc('boat-lower-right', (24, 42), (36, 24), radius_x=60, radius_y=30, sweep=False)
        self.add_arc('boat-upper-right', (36, 24), (24, 6), radius_x=60, radius_y=30, sweep=False)
        self.add_contour('boat', 'boat-upper-left', 'boat-lower-left', 'boat-lower-right', 'boat-upper-right', closed=True)
        self.add_arc('cockpit-top', (21, 24), (27, 24), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('cockpit-bottom', (27, 24), (21, 24), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('cockpit', 'cockpit-top', 'cockpit-bottom', closed=True)
        self.add_line('paddle-left-1', (12, 24), (6, 36))
        self.add_line('paddle-left-2', (6, 36), (6, 42))
        self.add_contour('paddle-left', 'paddle-left-1', 'paddle-left-2', closed=False)
        self.add_line('paddle-right-1', (36, 24), (42, 12))
        self.add_line('paddle-right-2', (42, 12), (42, 6))
        self.add_contour('paddle-right', 'paddle-right-1', 'paddle-right-2', closed=False)
        self.relate("connect", 'boat', 'paddle-left')
        self.relate("connect", 'boat', 'paddle-right')

"""Replace the kayak’s four offset arcs with smooth matched hull curves; keep the widest point at the paddle attachments and give the cockpit an oval opening.
Independent centerline revision; original snapshot preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a40dd6b4-7ef7-5a0e-b996-7bd77b8c7cf8'
SOURCE_PATH = 'pictographic-primitives/recreation/canoe_a40dd6b4-7ef7-5a0e-b996-7bd77b8c7cf8.svg'
AUTHOR = 'gpt-6'

class KayakAndPaddle(Solo48):
    icon_id = 'kayak-and-paddle-centerline-v2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/recreation'
    aliases = ()
    keywords = ('kayak', 'and', 'paddle')

    def build(self) -> None:
        self.add_bezier('boat-upper-left', (24, 6), ((18, 10), (12, 17), (12, 24)))
        self.add_bezier('boat-lower-left', (12, 24), ((12, 31), (18, 38), (24, 42)))
        self.add_bezier('boat-lower-right', (24, 42), ((30, 38), (36, 31), (36, 24)))
        self.add_bezier('boat-upper-right', (36, 24), ((36, 17), (30, 10), (24, 6)))
        self.add_contour('boat', 'boat-upper-left', 'boat-lower-left', 'boat-lower-right', 'boat-upper-right', closed=True)
        self.add_arc('cockpit-top', (21, 24), (27, 24), radius_x=3, radius_y=5, sweep=True)
        self.add_arc('cockpit-bottom', (27, 24), (21, 24), radius_x=3, radius_y=5, sweep=True)
        self.add_contour('cockpit', 'cockpit-top', 'cockpit-bottom', closed=True)
        self.add_line('paddle-left-1', (12, 24), (6, 36))
        self.add_line('paddle-left-2', (6, 36), (6, 42))
        self.add_contour('paddle-left', 'paddle-left-1', 'paddle-left-2', closed=False)
        self.add_line('paddle-right-1', (36, 24), (42, 12))
        self.add_line('paddle-right-2', (42, 12), (42, 6))
        self.add_contour('paddle-right', 'paddle-right-1', 'paddle-right-2', closed=False)
        self.relate('connect', 'boat', 'paddle-left')
        self.relate('connect', 'boat', 'paddle-right')
    variant_of = 'kayak-and-paddle'
    variant_label = 'Batch 01 centerline repair'

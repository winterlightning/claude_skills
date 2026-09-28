"""Revision from the inspected source: The rejected arm and thigh were long flat bars; the source shows a compact seated forearm and extended bent leg.

Changes: Shortened the forearm and rebalanced the thigh while keeping the exact family envelope.
Full-body or bust construction follows icon_set/references/human_ref.
"""
"""A seated person facing right with one extended arm. VRECT_L extremes (8,4)-(40,44). Lucide accessibility informs the bent seated leg and separated head. Preserve the chair-free source pose, slanted back and forward lower leg."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '4c8005a6-de74-49df-bc2e-e2c42b099091'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-sitting/20260927T083143Z-thuan-mac-1/reference/person sitting_4c8005a6-de74-49df-bc2e-e2c42b099091.svg'
AUTHOR = 'gpt-6'


class PersonSitting(Solo48):
    icon_id = 'person-sitting'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    categories = ("symbol",)
    aliases = ()
    keywords = ('sitting', 'person', 'seat', 'rest', 'posture', 'figure', 'accessible', 'chair')

    def build(self) -> None:
        cx, cy, radius = 20, 10, 6
        self.add_arc('head-top', (cx-radius, cy), (cx+radius, cy), radius_x=radius)
        self.add_arc('head-bottom', (cx+radius, cy), (cx-radius, cy), radius_x=radius)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_polyline('body-legs',(16,26),(8,34),(30,34),(40,44))
        self.add_line('arm',(16,26),(32,26))
        self.relate('connect','body-legs','arm')

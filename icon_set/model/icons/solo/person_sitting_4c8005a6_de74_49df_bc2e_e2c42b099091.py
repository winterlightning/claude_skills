"""A seated person facing right with one extended arm. VRECT_L extremes (8,4)-(40,44). Lucide accessibility informs the bent seated leg and separated head. Preserve the chair-free source pose, slanted back and forward lower leg."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4c8005a6-de74-49df-bc2e-e2c42b099091'
SOURCE_PATH = 'pictographic-primitives/symbol/person sitting_4c8005a6-de74-49df-bc2e-e2c42b099091.svg'
AUTHOR = 'gpt-6'


class PersonSitting(Solo48):
    icon_id = 'person-sitting'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    aliases = ()
    keywords = ('sitting', 'person', 'seat', 'rest', 'posture', 'figure', 'accessible', 'chair')

    def build(self) -> None:
        cx, cy, radius = 20, 10, 6
        self.add_arc('head-top', (cx-radius, cy), (cx+radius, cy), radius_x=radius)
        self.add_arc('head-bottom', (cx+radius, cy), (cx-radius, cy), radius_x=radius)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_polyline('body-legs',(16,26),(8,34),(28,34),(40,44))
        self.add_line('arm',(16,26),(36,26))
        self.relate('connect','body-legs','arm')

"""Straighten the kiwi’s long beak and lift the lower belly to open the gap above its feet; keep the compact bird body and short legs.
Independent centerline revision; original snapshot preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e7f198e2-850a-485d-8d8d-49ce1c496222'
SOURCE_PATH = 'pictographic-primitives/animals/wild bird_e7f198e2-850a-485d-8d8d-49ce1c496222.svg'
AUTHOR = 'gpt-6'

class KiwiBird(Solo48):
    icon_id = 'kiwi-bird-centerline-v2'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/animals'
    aliases = ()
    keywords = ('kiwi', 'bird', 'beak', 'new zealand', 'flightless', 'round', 'long beak', 'wildlife')

    def build(self) -> None:
        self.add_bezier('back', (4, 25), ((4, 16), (10, 12), (18, 12)), ((22, 12), (24, 8), (24, 8)))
        self.add_bezier('head', (24, 8), ((30, 8), (33, 12), (31, 17)))
        self.add_bezier('neck', (31, 17), ((25, 20), (27, 27), (22, 31)), ((21, 32), (21, 32), (20, 32)), ((18, 32), (15, 33), (12, 32)), ((7, 32), (4, 28), (4, 25)))
        self.add_contour('bird', 'back', 'head', 'neck', closed=True)
        self.add_line('beak', (31, 17), (44, 30))
        self.relate('connect', 'beak', 'bird')
        self.add_polyline('leg-left', (12, 32), (8, 40), (4, 40))
        self.add_polyline('leg-right', (20, 32), (22, 40), (27, 40))
        self.relate('connect', 'leg-left', 'bird')
        self.relate('connect', 'leg-right', 'bird')
        self.add_dot('eye', (18, 22))
    variant_of = 'kiwi-bird'
    variant_label = 'Batch 01 centerline repair'

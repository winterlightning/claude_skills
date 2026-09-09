# Variant of diaper-change; parent file remains unchanged.
'Simpler changing pose. Independent feedback revision; preserve source subject.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ca21559b-4869-40c1-bb54-eb0998bb59fb'
SOURCE_PATH = 'pictographic-primitives/babies/family baby change diaper_ca21559b-4869-40c1-bb54-eb0998bb59fb.svg'
AUTHOR = 'gpt-6'

class DiaperChangeVariant2(Solo48):
    icon_id = 'diaper-change-v2'
    variant_of = 'diaper-change'
    variant_label = 'Simpler changing pose'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'people/babies'
    aliases = ()
    keywords = ('diaper', 'change', 'infant', 'nursery')

    def build(self) -> None:
        self.add_arc('adult-head-top', (21, 7), (31, 7), radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_arc('adult-head-bottom', (31, 7), (21, 7), radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_contour('adult-head', 'adult-head-top', 'adult-head-bottom', closed=True)
        self.add_polyline('adult-back', (17, 16), (2, 34), (2, 46))
        self.add_polyline('adult-arm', (17, 16), (23, 32))
        self.relate('connect', 'adult-back', 'adult-arm')
        self.add_arc('baby-head-top', (40, 33), (46, 33), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_arc('baby-head-bottom', (46, 33), (40, 33), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_contour('baby-head', 'baby-head-top', 'baby-head-bottom', closed=True)
        self.add_polyline('baby-body', (23, 32), (27, 38), (33, 38), (33, 31))
        self.relate('connect', 'adult-arm', 'baby-body')
        self.add_line('surface', (22, 46), (46, 46))

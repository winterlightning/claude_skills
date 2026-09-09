# Variant of shanty-village-row; parent file remains unchanged.
"""Staggered rear homes over level rectangular foreground buildings. SQUARE centerline bounds (2,2)-(46,46). Lucide house informs aligned wall runs and a symmetric gable; rear staggering is intentional."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e5d1bebc-56b3-4fda-9bbf-e7de604c4fb4'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-06/shanty house village_e5d1bebc-56b3-4fda-9bbf-e7de604c4fb4.svg'
AUTHOR = 'gpt-6'

class ShantyVillageRowVariant2(Solo48):
    icon_id = 'shanty-village-row-v2'
    variant_of = 'shanty-village-row'
    variant_label = 'Level geometric foreground buildings'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'places/landmarks'
    aliases = ()
    keywords = ('shanty', 'slum', 'village', 'houses', 'informal', 'settlement', 'shelter', 'housing')

    def build(self) -> None:
        self.add_polyline('rear-left', (2, 26), (2, 13), (12, 7), (22, 13), (22, 21))
        self.add_polyline('rear-right', (22, 13), (22, 8), (34, 2), (46, 8), (46, 23))
        self.relate('connect', 'rear-left', 'rear-right')
        self.add_polyline('shed', (18, 46), (18, 34), (32, 27), (46, 34), (46, 46), (18, 46), (2, 46), (2, 34), (18, 34))

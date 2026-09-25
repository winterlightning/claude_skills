"""Independent 32px profile of crystal-prism.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '50bf8547-15ad-48f8-a95c-4aded7b6887f'
SOURCE_PATH = 'pictographic-primitives/symbol/crystal_50bf8547-15ad-48f8-a95c-4aded7b6887f.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('50bf8547-15ad-48f8-a95c-4aded7b6887f', 'pictographic-primitives/symbol/crystal_50bf8547-15ad-48f8-a95c-4aded7b6887f.svg'),)
PROFILE_SOURCE_KEYS = ('solo/crystal-prism',)
SOLO_SOURCE_ICON_IDS = ('crystal-prism',)
REFERENCE_EXPORT_SHA256 = '08dc4de9ea75b9d80f0980293b0eda1ffeaf8383a9701e91ac7c4df19ac91c44'

class DrawingVariant3(Sub32):
    icon_id = 'crystal-prism-sub32-v3'
    related_origin_icon_id = 'crystal-prism-sub32-v2'
    variant_label = 'Redraw proportions and source features'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_polyline('outline', (16, 2), (24, 9), (24, 23), (16, 30), (8, 23), (8, 9), closed=True)
        self.add_polyline('upper-facets', (8, 9), (16, 14), (24, 9))
        self.add_polyline('lower-facets', (8, 23), (16, 18), (24, 23))
        self.add_line('spine', (16, 14), (16, 18))
        for x in ['upper-facets-1', 'upper-facets-2']:
            for y in ['spine']:
                self.relate('connect', x, y)
        for x in ['lower-facets-1', 'lower-facets-2']:
            self.relate('connect', x, 'spine')
        for a, b in [('outline-1', 'upper-facets-2'), ('outline-2', 'upper-facets-2'), ('outline-3', 'lower-facets-2'), ('outline-2', 'lower-facets-2'), ('outline-4', 'lower-facets-1'), ('outline-5', 'lower-facets-1'), ('outline-5', 'upper-facets-1'), ('outline-6', 'upper-facets-1')]:
            self.relate('connect', a, b)

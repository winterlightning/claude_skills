"""Independent 32px profile of police-badge.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '822a5769-bcbb-4ef4-8ce4-ccd72a880353'
SOURCE_PATH = 'pictographic-primitives/symbol/police badge_822a5769-bcbb-4ef4-8ce4-ccd72a880353.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('822a5769-bcbb-4ef4-8ce4-ccd72a880353', 'pictographic-primitives/symbol/police badge_822a5769-bcbb-4ef4-8ce4-ccd72a880353.svg'),)
PROFILE_SOURCE_KEYS = ('solo/police-badge',)
SOLO_SOURCE_ICON_IDS = ('police-badge',)
REFERENCE_EXPORT_SHA256 = '79a309493ff448944ee8402a5e6957126fbc8e8caedb861cebb1e880550d95b4'

class DrawingVariant3(Sub32):
    icon_id = 'police-badge-sub32-v3'
    related_origin_icon_id = 'police-badge-sub32-v2'
    variant_label = 'Redraw proportions and source features'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('top-left', (6, 5), ((10, 8), (13, 4), (16, 2)))
        self.add_bezier('top-right', (16, 2), ((19, 4), (22, 8), (26, 5)))
        self.add_bezier('right-in', (26, 5), ((22, 12), (26, 14), (26, 19)))
        self.add_bezier('right-base', (26, 19), ((26, 24), (21, 28), (16, 30)))
        self.add_bezier('left-base', (16, 30), ((11, 28), (6, 24), (6, 19)))
        self.add_bezier('left-in', (6, 19), ((6, 14), (10, 12), (6, 5)))
        self.add_contour('badge', 'top-left', 'top-right', 'right-in', 'right-base', 'left-base', 'left-in', closed=True)
        self.add_line('mark', (16, 14), (16, 19))

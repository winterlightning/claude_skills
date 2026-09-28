"""Independent 32px profile of octagon-up-arrow-content.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '1d212fbb-810b-4031-893b-526296e01048'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/1d212fbb-810b-4031-893b-526296e01048.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('1d212fbb-810b-4031-893b-526296e01048', 'icon_set/dist/gallery/combination-originals/1d212fbb-810b-4031-893b-526296e01048.svg'),)
PROFILE_SOURCE_KEYS = ('solo/octagon-up-arrow-content',)
SOLO_SOURCE_ICON_IDS = ('octagon-up-arrow-content',)
REFERENCE_EXPORT_SHA256 = '410829c823d717317547a5aaa7617e44d1cad625afd9f3790423649b53de8e39'

class DrawingVariant3(Sub32):
    icon_id = 'octagon-up-arrow-content-sub32-v3'
    related_origin_icon_id = 'octagon-up-arrow-content-sub32-v2'
    variant_label = 'Redraw proportions and source features'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_polyline('arrow', (11, 7), (16, 2), (21, 7))
        self.add_line('shaft', (16, 2), (16, 8))
        self.relate('connect', 'shaft', 'arrow-1')
        self.relate('connect', 'shaft', 'arrow-2')
        self.add_polyline('octagon', (12, 14), (20, 14), (24, 18), (24, 26), (20, 30), (12, 30), (8, 26), (8, 18), closed=True)

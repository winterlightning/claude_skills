"""Independent 32px profile of navigation-direction-left.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '22ff4baa-e14e-4622-9ea4-d56766efca09'
SOURCE_PATH = 'pictographic-primitives/interface-essential/navigation direction left_22ff4baa-e14e-4622-9ea4-d56766efca09.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('22ff4baa-e14e-4622-9ea4-d56766efca09', 'pictographic-primitives/interface-essential/navigation direction left_22ff4baa-e14e-4622-9ea4-d56766efca09.svg'),)
PROFILE_SOURCE_KEYS = ('solo/navigation-direction-left',)
SOLO_SOURCE_ICON_IDS = ('navigation-direction-left',)
REFERENCE_EXPORT_SHA256 = '066ffa0c7f5f0a89cac827cb4335ba9f77b24e857a54b6bd676d912f57abe20c'

class Drawing(Sub32):
    icon_id = 'navigation-direction-left-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 13), (24, 13))
        self.add_arc('p1-r1-2', (24, 13), (30, 19), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (30, 19), (30, 27))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (10, 5), (2, 13))
        self.add_line('p2-r1-2', (2, 13), (10, 22))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-1', 'p2-r1-2')

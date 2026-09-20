# Independent container symbol; edit separately from linked side sub-icon.
"""Independent 32px profile of building-building.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '265ecf16-9a75-43f1-970c-76948410da91'
SOURCE_PATH = 'pictographic-primitives/building/building_265ecf16-9a75-43f1-970c-76948410da91.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('265ecf16-9a75-43f1-970c-76948410da91', 'pictographic-primitives/building/building_265ecf16-9a75-43f1-970c-76948410da91.svg'),)
PROFILE_SOURCE_KEYS = ('solo/building-building',)
SOLO_SOURCE_ICON_IDS = ('building-building',)
REFERENCE_EXPORT_SHA256 = '727f371c967195febc025ec2202984500804923863d15189abf368b43175643f'

class DrawingContainerSymbol(Sub32):
    icon_id = 'building-building-sub32-symbol'
    variant_of = 'building-building-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/building-building-sub32'
    counterpart_icon_id = 'building-building-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'building'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (5, 30), (5, 2))
        self.add_line('p1-r1-2', (5, 2), (22, 2))
        self.add_line('p1-r1-3', (22, 2), (22, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (22, 11), (30, 15))
        self.add_line('p2-r1-2', (30, 15), (30, 30))
        self.add_line('p2-r1-3', (30, 30), (2, 30))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_line('p3-r1-1', (12, 10), (15, 10))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)

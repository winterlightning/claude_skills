# Independent container symbol; edit separately from linked side sub-icon.
"""Independent 32px profile of loading-bar-interface-essential.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'af64a969-821b-4b51-b04b-4e271c5910d7'
SOURCE_PATH = 'pictographic-primitives/interface-essential/loading bar_af64a969-821b-4b51-b04b-4e271c5910d7.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('af64a969-821b-4b51-b04b-4e271c5910d7', 'pictographic-primitives/interface-essential/loading bar_af64a969-821b-4b51-b04b-4e271c5910d7.svg'),)
PROFILE_SOURCE_KEYS = ('solo/loading-bar-interface-essential',)
SOLO_SOURCE_ICON_IDS = ('loading-bar-interface-essential',)
REFERENCE_EXPORT_SHA256 = '8dc2090d8469d05f859adf93717c02503a8192b99946f46c21adbf358d600f1d'

class DrawingContainerSymbol(Sub32):
    icon_id = 'loading-bar-interface-essential-sub32-symbol'
    variant_of = 'loading-bar-interface-essential-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/loading-bar-interface-essential-sub32'
    counterpart_icon_id = 'loading-bar-interface-essential-sub32'
    keyshape = Keyshape.HRECT_S
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (6, 12), (20, 12))
        self.add_line('p1-r1-2', (20, 12), (26, 12))
        self.add_bezier('p1-r1-3', (26, 12), ((29, 12), (30, 13), (30, 16)))
        self.add_bezier('p1-r1-4', (30, 16), ((30, 19), (29, 20), (26, 20)))
        self.add_line('p1-r1-5', (26, 20), (12, 20))
        self.add_line('p1-r1-6', (12, 20), (6, 20))
        self.add_bezier('p1-r1-7', (6, 20), ((3, 20), (2, 19), (2, 16)))
        self.add_bezier('p1-r1-8', (2, 16), ((2, 13), (3, 12), (6, 12)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_line('p2-r1-1', (20, 12), (12, 20))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-5', 'p2-r1-1')
        self.relate('connect', 'p1-r1-6', 'p2-r1-1')

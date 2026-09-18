"""Independent 32px profile of battery-charging-vertical.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '4eb92da5-29c0-4d92-ae40-851bdeae1749'
SOURCE_PATH = 'pictographic-primitives/symbol/lightning rectangle_4eb92da5-29c0-4d92-ae40-851bdeae1749.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('4eb92da5-29c0-4d92-ae40-851bdeae1749', 'pictographic-primitives/symbol/lightning rectangle_4eb92da5-29c0-4d92-ae40-851bdeae1749.svg'),)
PROFILE_SOURCE_KEYS = ('solo/battery-charging-vertical',)
SOLO_SOURCE_ICON_IDS = ('battery-charging-vertical',)
REFERENCE_EXPORT_SHA256 = '0c8109e691174030648795152ecb7b76bf4a88561c03df1061f321f6c369f3c9'

class Drawing(Sub32):
    icon_id = 'battery-charging-vertical-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (8, 9), (10, 9))
        self.add_line('p1-r1-2', (10, 9), (22, 9))
        self.add_line('p1-r1-3', (22, 9), (24, 9))
        self.add_arc('p1-r1-4', (24, 9), (27, 12), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (27, 12), (27, 27))
        self.add_arc('p1-r1-6', (27, 27), (24, 30), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-7', (24, 30), (8, 30))
        self.add_arc('p1-r1-8', (8, 30), (5, 27), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-9', (5, 27), (5, 12))
        self.add_arc('p1-r1-10', (5, 12), (8, 9), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', closed=False)
        self.add_line('p2-r1-1', (10, 9), (10, 2))
        self.add_line('p2-r1-2', (10, 2), (22, 2))
        self.add_line('p2-r1-3', (22, 2), (22, 9))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_line('p3-r1-1', (16, 15), (11, 20))
        self.add_line('p3-r1-2', (11, 20), (21, 20))
        self.add_line('p3-r1-3', (21, 20), (16, 24))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-2', 'p2-r1-1')
        self.relate("connect", 'p1-r1-2', 'p2-r1-3')
        self.relate("connect", 'p1-r1-3', 'p2-r1-3')

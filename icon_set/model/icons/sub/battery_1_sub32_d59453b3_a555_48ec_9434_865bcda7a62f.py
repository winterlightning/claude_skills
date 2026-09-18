"""Independent 32px profile of battery-1.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'd59453b3-a555-48ec-9434-865bcda7a62f'
SOURCE_PATH = 'pictographic-primitives/state/battery 1_d59453b3-a555-48ec-9434-865bcda7a62f.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('d59453b3-a555-48ec-9434-865bcda7a62f', 'pictographic-primitives/state/battery 1_d59453b3-a555-48ec-9434-865bcda7a62f.svg'),)
PROFILE_SOURCE_KEYS = ('solo/battery-1',)
SOLO_SOURCE_ICON_IDS = ('battery-1',)
REFERENCE_EXPORT_SHA256 = '8c49772019cd8e86f290bd424f27d1e5902d44ffb25614032fdb4c8aca97db89'

class Drawing(Sub32):
    icon_id = 'battery-1-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'state'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (5, 5), (22, 5))
        self.add_arc('p1-r1-2', (22, 5), (24, 8), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (24, 8), (24, 10))
        self.add_line('p1-r1-4', (24, 10), (24, 22))
        self.add_line('p1-r1-5', (24, 22), (24, 24))
        self.add_arc('p1-r1-6', (24, 24), (22, 27), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-7', (22, 27), (5, 27))
        self.add_arc('p1-r1-8', (5, 27), (2, 24), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-9', (2, 24), (2, 8))
        self.add_arc('p1-r1-10', (2, 8), (5, 5), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', closed=False)
        self.add_line('p2-r1-1', (24, 10), (30, 10))
        self.add_line('p2-r1-2', (30, 10), (30, 22))
        self.add_line('p2-r1-3', (30, 22), (24, 22))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.relate("connect", 'p1-r1-3', 'p2-r1-1')
        self.relate("connect", 'p1-r1-4', 'p2-r1-1')
        self.relate("connect", 'p1-r1-4', 'p2-r1-3')
        self.relate("connect", 'p1-r1-5', 'p2-r1-3')

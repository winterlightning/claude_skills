"""Independent 32px profile of graduation-cap-symbol.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'e5ae7651-62d6-4c05-b34e-faf818f521bc'
SOURCE_PATH = 'pictographic-primitives/symbol/graduation cap_e5ae7651-62d6-4c05-b34e-faf818f521bc.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e5ae7651-62d6-4c05-b34e-faf818f521bc', 'pictographic-primitives/symbol/graduation cap_e5ae7651-62d6-4c05-b34e-faf818f521bc.svg'), ('ac0c8839-9020-4a65-9a30-af5a45d63503', 'pictographic-primitives/accessories/batch-07/cap_ac0c8839-9020-4a65-9a30-af5a45d63503.svg'), ('5f6ee542-cdce-408a-b798-b60860e5b325', 'pictographic-primitives/accessories/batch-06/cap_5f6ee542-cdce-408a-b798-b60860e5b325.svg'))
PROFILE_SOURCE_KEYS = ('solo/graduation-cap-symbol', 'solo/academic-graduation-cap', 'solo/graduation-mortarboard')
SOLO_SOURCE_ICON_IDS = ('graduation-cap-symbol', 'academic-graduation-cap', 'graduation-mortarboard')
REFERENCE_EXPORT_SHA256 = '3db2ce90f5f70f0792c27acb4fbe21a247b788f59a72a50715d7930ff3bccb1b'

class Drawing(Sub32):
    icon_id = 'graduation-cap-symbol-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (26, 14), (26, 22))
        self.add_arc('p1-r1-2', (26, 22), (22, 26), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (22, 26), (16, 27))
        self.add_arc('p1-r1-4', (16, 27), (12, 26), radius_x=13, radius_y=13, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (12, 26), (6, 24))
        self.add_line('p1-r1-6', (6, 24), (6, 14))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_line('p2-r1-1', (26, 14), (17, 18))
        self.add_arc('p2-r1-2', (17, 18), (15, 18), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_line('p2-r1-3', (15, 18), (6, 14))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_line('p3-r1-1', (26, 14), (30, 12))
        self.add_line('p3-r1-2', (30, 12), (16, 5))
        self.add_arc('p3-r1-3', (16, 5), (15, 5), radius_x=27, radius_y=27, large_arc=False, sweep=True)
        self.add_line('p3-r1-4', (15, 5), (2, 12))
        self.add_line('p3-r1-5', (2, 12), (6, 14))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-1', 'p3-r1-1')
        self.relate("connect", 'p1-r1-6', 'p2-r1-3')
        self.relate("connect", 'p1-r1-6', 'p3-r1-5')
        self.relate("connect", 'p2-r1-1', 'p3-r1-1')
        self.relate("connect", 'p2-r1-3', 'p3-r1-5')

"""Independent 32px profile of empty-battery-content.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '85092961-e906-49b8-a4e0-732ce5ffbef0'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/85092961-e906-49b8-a4e0-732ce5ffbef0.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('85092961-e906-49b8-a4e0-732ce5ffbef0', 'icon_set/dist/gallery/combination-originals/85092961-e906-49b8-a4e0-732ce5ffbef0.svg'),)
PROFILE_SOURCE_KEYS = ('solo/empty-battery-content',)
SOLO_SOURCE_ICON_IDS = ('empty-battery-content',)
REFERENCE_EXPORT_SHA256 = 'cc6e5704dab24af125ef21b2e1044c1165a3440b80e3b941ee634b96fbe50561'

class Drawing(Sub32):
    icon_id = 'empty-battery-content-sub32'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (5, 6), (21, 6))
        self.add_arc('p1-r1-2', (21, 6), (24, 9), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (24, 9), (24, 23))
        self.add_arc('p1-r1-4', (24, 23), (21, 26), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (21, 26), (5, 26))
        self.add_arc('p1-r1-6', (5, 26), (2, 23), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-7', (2, 23), (2, 9))
        self.add_arc('p1-r1-8', (2, 9), (5, 6), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_line('p2-r1-1', (30, 12), (30, 20))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)

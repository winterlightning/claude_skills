"""Independent 32px profile of pie-chart-growth-content.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'f82a9a59-0712-48ad-b67b-ef47e7c946ad'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/f82a9a59-0712-48ad-b67b-ef47e7c946ad.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('f82a9a59-0712-48ad-b67b-ef47e7c946ad', 'icon_set/dist/gallery/combination-originals/f82a9a59-0712-48ad-b67b-ef47e7c946ad.svg'),)
PROFILE_SOURCE_KEYS = ('solo/pie-chart-growth-content',)
SOLO_SOURCE_ICON_IDS = ('pie-chart-growth-content',)
REFERENCE_EXPORT_SHA256 = 'b9b242c01ac6d175da22d9339e6b4902bb87105f051bd89d5c894ab355ff0153'

class Drawing(Sub32):
    icon_id = 'pie-chart-growth-content-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (16, 2), (2, 16), radius_x=14, radius_y=14, large_arc=False, sweep=False)
        self.add_arc('p1-r1-2', (2, 16), (16, 30), radius_x=14, radius_y=14, large_arc=False, sweep=False)
        self.add_line('p1-r1-3', (16, 30), (16, 16))
        self.add_line('p1-r1-4', (16, 16), (16, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (23, 24), (30, 13))
        self.add_line('p2-r1-2', (30, 13), (30, 21))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (23, 13), (30, 13))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate("connect", 'p2-r1-1', 'p3-r1-1')
        self.relate("connect", 'p2-r1-2', 'p3-r1-1')

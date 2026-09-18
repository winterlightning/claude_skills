"""Independent 32px profile of arrow-right-2dabd652.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '2dabd652-d8dd-4866-92ea-d5ea5b02c1cf'
SOURCE_PATH = 'pictographic-primitives/arrows/arrow right_2dabd652-d8dd-4866-92ea-d5ea5b02c1cf.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('2dabd652-d8dd-4866-92ea-d5ea5b02c1cf', 'pictographic-primitives/arrows/arrow right_2dabd652-d8dd-4866-92ea-d5ea5b02c1cf.svg'),)
PROFILE_SOURCE_KEYS = ('solo/arrow-right-2dabd652',)
SOLO_SOURCE_ICON_IDS = ('arrow-right-2dabd652',)
REFERENCE_EXPORT_SHA256 = '53de866da986683483755fadb3454e505f6da859b0615f545467bbb9e2bdb4a9'

class Drawing(Sub32):
    icon_id = 'arrow-right-2dabd652-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'arrows'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (2, 27), (19, 10), radius_x=17, radius_y=17, large_arc=False, sweep=True)
        self.add_line('p1-r1-2', (19, 10), (30, 10))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (23, 5), (30, 10))
        self.add_line('p2-r1-2', (30, 10), (23, 16))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.relate("connect", 'p1-r1-2', 'p2-r1-1')
        self.relate("connect", 'p1-r1-2', 'p2-r1-2')

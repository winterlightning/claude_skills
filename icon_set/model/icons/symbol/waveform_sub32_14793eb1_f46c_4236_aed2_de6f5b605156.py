"""Independent 32px profile of waveform.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '14793eb1-f46c-4236-aed2-de6f5b605156'
SOURCE_PATH = 'pictographic-primitives/symbol/waveform_14793eb1-f46c-4236-aed2-de6f5b605156.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('14793eb1-f46c-4236-aed2-de6f5b605156', 'pictographic-primitives/symbol/waveform_14793eb1-f46c-4236-aed2-de6f5b605156.svg'),)
PROFILE_SOURCE_KEYS = ('solo/waveform',)
SOLO_SOURCE_ICON_IDS = ('waveform',)
REFERENCE_EXPORT_SHA256 = '02214d1822f4e001eec8e39408ac92c493b5a8ca96d7ea50b9f39ce7035d63ba'

class Drawing(Sub32):
    icon_id = 'waveform-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (30, 17), (26, 17))
        self.add_arc('p1-r1-2', (26, 17), (24, 13), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (24, 13), (20, 27))
        self.add_line('p1-r1-4', (20, 27), (16, 5))
        self.add_line('p1-r1-5', (16, 5), (11, 24))
        self.add_line('p1-r1-6', (11, 24), (8, 17))
        self.add_line('p1-r1-7', (8, 17), (2, 17))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)

"""Independent 32px profile of bowling-pins-row.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'd972c303-2754-4efe-82ae-c0b2f535370b'
SOURCE_PATH = 'pictographic-primitives/symbol/three bowlings_d972c303-2754-4efe-82ae-c0b2f535370b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('d972c303-2754-4efe-82ae-c0b2f535370b', 'pictographic-primitives/symbol/three bowlings_d972c303-2754-4efe-82ae-c0b2f535370b.svg'),)
PROFILE_SOURCE_KEYS = ('solo/bowling-pins-row',)
SOLO_SOURCE_ICON_IDS = ('bowling-pins-row',)
REFERENCE_EXPORT_SHA256 = '7e2266793a3782340fe034c864ad5074b7828bfad71d94754eeda6b08ae177c4'

class Drawing(Sub32):
    icon_id = 'bowling-pins-row-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Row of three slim bowling pins: a dot head over a stick body, pins 8 units apart.
        for k, x in enumerate((4, 16, 28)):
            self.add_arc(f'head-{k}-1', (x - 2, 6), (x + 2, 6), radius_x=2, radius_y=2, large_arc=False, sweep=True)
            self.add_arc(f'head-{k}-2', (x + 2, 6), (x - 2, 6), radius_x=2, radius_y=2, large_arc=False, sweep=True)
            self.add_contour(f'head-{k}', f'head-{k}-1', f'head-{k}-2', closed=True)
            self.add_line(f'body-{k}', (x, 16), (x, 28))

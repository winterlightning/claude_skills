"""Independent 32px profile of lightning-with-wrench.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '7a4d7838-471b-4d28-87da-ddd67295cbe7'
SOURCE_PATH = 'pictographic-primitives/symbol/lightning with wrench_7a4d7838-471b-4d28-87da-ddd67295cbe7.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('7a4d7838-471b-4d28-87da-ddd67295cbe7', 'pictographic-primitives/symbol/lightning with wrench_7a4d7838-471b-4d28-87da-ddd67295cbe7.svg'), ('8b71e7e7-15cf-4d31-8c76-295ef5576f53', 'icon_set/dist/gallery/combination-originals/8b71e7e7-15cf-4d31-8c76-295ef5576f53.svg'))
PROFILE_SOURCE_KEYS = ('solo/lightning-with-wrench',)
SOLO_SOURCE_ICON_IDS = ('lightning-with-wrench',)
REFERENCE_EXPORT_SHA256 = '8499894bda8f20061b025c07c165f4022d6519d76adb62f1d7dc04a39dbd3237'

class Drawing(Sub32):
    icon_id = 'lightning-with-wrench-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Open-jaw wrench (upright) beside a lightning bolt, 4 units apart.
        self.add_arc('jaw', (11, 5), (3, 5), radius_x=5, radius_y=5, large_arc=True, sweep=True)
        self.add_line('handle', (7, 14), (7, 30))
        self.add_polyline('bolt', (30, 2), (20, 16), (30, 16), (20, 30))
        self.relate('connect', 'jaw', 'handle')

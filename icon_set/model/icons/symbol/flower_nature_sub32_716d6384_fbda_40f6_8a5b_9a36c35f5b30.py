"""Independent 32px profile of flower-nature.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '716d6384-fbda-40f6-8a5b-9a36c35f5b30'
SOURCE_PATH = 'pictographic-primitives/nature/flower_716d6384-fbda-40f6-8a5b-9a36c35f5b30.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('716d6384-fbda-40f6-8a5b-9a36c35f5b30', 'pictographic-primitives/nature/flower_716d6384-fbda-40f6-8a5b-9a36c35f5b30.svg'),)
PROFILE_SOURCE_KEYS = ('solo/flower-nature',)
SOLO_SOURCE_ICON_IDS = ('flower-nature',)
REFERENCE_EXPORT_SHA256 = 'aae1a9ae3673dc034ab5f8a8008f8d3f26a090b59e23587a55a7f9ae6ff07f51'

class Drawing(Sub32):
    icon_id = 'flower-nature-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'nature'
    categories = ('nature', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Flower: four round petals (semicircles) around a centre dot.
        self.add_arc('petal-t', (9, 9), (23, 9), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_arc('petal-r', (23, 9), (23, 23), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_arc('petal-b', (23, 23), (9, 23), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_arc('petal-l', (9, 23), (9, 9), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_contour('petals', 'petal-t', 'petal-r', 'petal-b', 'petal-l', closed=True)
        self.add_line('centre', (16, 16), (16, 16))

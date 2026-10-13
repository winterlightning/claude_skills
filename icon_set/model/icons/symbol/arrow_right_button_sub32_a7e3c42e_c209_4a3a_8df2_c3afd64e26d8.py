"""Independent 32px profile of arrow-right-button.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'a7e3c42e-c209-4a3a-8df2-c3afd64e26d8'
SOURCE_PATH = 'pictographic-primitives/symbol/arrow right button_a7e3c42e-c209-4a3a-8df2-c3afd64e26d8.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('a7e3c42e-c209-4a3a-8df2-c3afd64e26d8', 'pictographic-primitives/symbol/arrow right button_a7e3c42e-c209-4a3a-8df2-c3afd64e26d8.svg'),)
PROFILE_SOURCE_KEYS = ('solo/arrow-right-button',)
SOLO_SOURCE_ICON_IDS = ('arrow-right-button',)
REFERENCE_EXPORT_SHA256 = 'c585ec72c3913257650a386a579b6923c44e0ec0958ba73c88ea1154fb0ded99'

class Drawing(Sub32):
    icon_id = 'arrow-right-button-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Adopted from the production stroke edit (Browser Edit by hina).
        self.add_line('p1-r1-1', (4, 2), (16, 2))
        self.add_line('p1-r1-2', (16, 2), (28, 16))
        self.add_line('p1-r1-3', (28, 16), (16, 30))
        self.add_line('p1-r1-4', (16, 30), (4, 30))
        self.add_line('p1-r1-5', (4, 30), (16, 16))
        self.add_line('p1-r1-6', (16, 16), (4, 2))
        self.add_line('p1-r1-7', (4, 2), (4, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)

"""Independent 32px profile of vortex.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '8e306dff-212c-4c03-9e9f-74e443e01b07'
SOURCE_PATH = 'pictographic-primitives/symbol/vortex_8e306dff-212c-4c03-9e9f-74e443e01b07.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('8e306dff-212c-4c03-9e9f-74e443e01b07', 'pictographic-primitives/symbol/vortex_8e306dff-212c-4c03-9e9f-74e443e01b07.svg'),)
PROFILE_SOURCE_KEYS = ('solo/vortex',)
SOLO_SOURCE_ICON_IDS = ('vortex',)
REFERENCE_EXPORT_SHA256 = '095dae8bfd966ff4a25d3d6649e3b5a28e3a4533bbe10cb33715339ea184af37'

class Drawing(Sub32):
    icon_id = 'vortex-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (5, 2), (14, 27))
        self.add_bezier('p1-r1-2', (14, 27), ((15, 29), (15, 30), (16, 30)))
        self.add_bezier('p1-r1-3', (16, 30), ((17, 30), (17, 29), (18, 27)))
        self.add_line('p1-r1-4', (18, 27), (27, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)

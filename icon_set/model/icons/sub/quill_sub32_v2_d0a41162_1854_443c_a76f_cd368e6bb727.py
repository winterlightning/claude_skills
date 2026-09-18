# Variant of quill-sub32; parent file remains unchanged.
"""Independent 32px profile of quill.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'd0a41162-1854-443c-a76f-cd368e6bb727'
SOURCE_PATH = 'pictographic-primitives/design/quill_d0a41162-1854-443c-a76f-cd368e6bb727.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('d0a41162-1854-443c-a76f-cd368e6bb727', 'pictographic-primitives/design/quill_d0a41162-1854-443c-a76f-cd368e6bb727.svg'),)
PROFILE_SOURCE_KEYS = ('solo/quill',)
SOLO_SOURCE_ICON_IDS = ('quill',)
REFERENCE_EXPORT_SHA256 = 'b3bc4f3461d4afd2a382f9581921ec27100785f14627c69b248bc4ed322aa721'

class DrawingVariant2(Sub32):
    icon_id = 'quill-sub32-v2'
    variant_of = 'quill-sub32'
    variant_label = 'Balanced feather and smooth root around the shaft'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'design'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('upper', (4,22), ((4,12),(17,4),(30,2)))
        self.add_bezier('lower', (30,2), ((28,15),(20,28),(10,28)))
        self.add_arc('root', (10,28), (4,22), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_contour('feather', 'upper','lower','root', closed=True)
        self.add_line('shaft', (2,30), (16,16))
        self.add_contour('vein', 'shaft', closed=False)
        self.relate('connect','feather','vein')

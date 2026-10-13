"""Independent 32px profile of pointed-paintbrush.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'e2452464-4988-4b2f-a220-0a5f8d32cc3e'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-01/brush_e2452464-4988-4b2f-a220-0a5f8d32cc3e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e2452464-4988-4b2f-a220-0a5f8d32cc3e', 'pictographic-primitives/decoration/batch-01/brush_e2452464-4988-4b2f-a220-0a5f8d32cc3e.svg'),)
PROFILE_SOURCE_KEYS = ('solo/pointed-paintbrush',)
SOLO_SOURCE_ICON_IDS = ('pointed-paintbrush',)
REFERENCE_EXPORT_SHA256 = 'c08360479dd7b1b10a838fb970123073510b81133fec70f30615988d16ed0729'

class Drawing(Sub32):
    icon_id = 'pointed-paintbrush-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'decoration'
    categories = ('primitives', 'decoration')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Paintbrush on the diagonal: straight handle, a clean ferrule edge and a pointed brush tip.
        self.add_polyline('handle', (15, 11), (24, 2), (30, 8), (21, 17), closed=True)
        self.add_bezier('tip-a', (15, 11), ((9, 17), (4, 22), (2, 30)))
        self.add_bezier('tip-b', (2, 30), ((10, 28), (15, 23), (21, 17)))
        self.add_contour('tip', 'tip-a', 'tip-b')
        self.relate('connect', 'handle', 'tip')

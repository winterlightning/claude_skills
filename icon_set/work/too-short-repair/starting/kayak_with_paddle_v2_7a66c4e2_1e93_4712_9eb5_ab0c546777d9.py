# Variant of kayak-with-paddle; parent file remains unchanged.
"""Kayak with Paddle, re-authored from its reference on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7a66c4e2-1e93-4712-9eb5-ab0c546777d9'
SOURCE_PATH = 'pictographic-primitives/transportation/kayak_7a66c4e2-1e93-4712-9eb5-ab0c546777d9.svg'
AUTHOR = 'gpt-6'

class KayakWithPaddleVariant2(Solo48):
    icon_id = 'kayak-with-paddle-v2'
    variant_of = 'kayak-with-paddle'
    variant_label = 'Height envelope and full spacing repair'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('kayak', 'paddle', 'canoe', 'boat', 'water sports', 'rowing', 'river', 'outdoor')

    def build(self) -> None:
        self.add_arc('hull-right-top', (24, 6), (30, 9), radius_x=30, radius_y=25)
        self.add_arc('hull-right-middle', (30, 9), (36, 24), radius_x=30, radius_y=25)
        self.add_arc('hull-right-bottom', (36, 24), (24, 42), radius_x=30, radius_y=25)
        self.add_arc('hull-left-bottom', (24, 42), (12, 24), radius_x=30, radius_y=25)
        self.add_arc('hull-left-top', (12, 24), (24, 6), radius_x=30, radius_y=25)
        self.add_contour('hull', 'hull-right-top', 'hull-right-middle', 'hull-right-bottom', 'hull-left-bottom', 'hull-left-top', closed=True)
        self.add_line('paddle-shaft', (12, 24), (30, 9))
        self.relate('connect', 'paddle-shaft', 'hull')
        self.add_polyline('blade-left', (12, 24), (8, 28), (8, 32))
        self.add_polyline('blade-right', (30, 9), (36, 6), (40, 6))
        self.relate('connect', 'paddle-shaft', 'blade-left')
        self.relate('connect', 'paddle-shaft', 'blade-right')
        self.relate('connect', 'hull', 'blade-left')
        self.relate('connect', 'hull', 'blade-right')

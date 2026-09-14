"""Kayak with Paddle, re-authored from its reference on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7a66c4e2-1e93-4712-9eb5-ab0c546777d9'
SOURCE_PATH = 'pictographic-primitives/transportation/kayak_7a66c4e2-1e93-4712-9eb5-ab0c546777d9.svg'
AUTHOR = 'gpt-6'

class KayakWithPaddle(Solo48):
    icon_id = 'kayak-with-paddle'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('kayak', 'paddle', 'canoe', 'boat', 'water sports', 'rowing', 'river', 'outdoor')

    def build(self) -> None:
        # Height repair: exact SOLO48 keyshape extremes; original subject and stroke retained.
        self.add_arc('hull-right-top', (24, 4), (30, 9), radius_x=30, radius_y=25)
        self.add_arc('hull-right-middle', (30, 9), (36, 24), radius_x=30, radius_y=25)
        self.add_arc('hull-right-bottom', (36, 24), (24, 44), radius_x=30, radius_y=25)
        self.add_arc('hull-left-bottom', (24, 44), (12, 24), radius_x=30, radius_y=25)
        self.add_arc('hull-left-top', (12, 24), (24, 4), radius_x=30, radius_y=25)
        self.add_contour('hull', 'hull-right-top', 'hull-right-middle', 'hull-right-bottom', 'hull-left-bottom', 'hull-left-top', closed=True)
        self.add_line('paddle-shaft', (12, 24), (30, 9))
        self.relate('connect', 'paddle-shaft', 'hull')
        self.add_polyline('blade-left', (12, 24), (8, 28), (8, 32))
        self.add_polyline('blade-right', (30, 9), (36, 4), (40, 4))
        self.relate('connect', 'paddle-shaft', 'blade-left')
        self.relate('connect', 'paddle-shaft', 'blade-right')
        self.relate('connect', 'hull', 'blade-left')
        self.relate('connect', 'hull', 'blade-right')

# Repair: Deepen the wrench jaw opening while retaining the hand at its original full-width grip.
"""A hand grips a wrench with a broad open jaw; crowded fingers are reduced to a thumb and lower fist contour."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '80b7765d-72c2-4b01-b0bf-6a084aa9bc97'
SOURCE_PATH = 'pictographic-primitives/tools/tools wrench hold_80b7765d-72c2-4b01-b0bf-6a084aa9bc97.svg'
AUTHOR = 'gpt-6'

class HandHoldingWrench(Solo48):
    icon_id = 'hand-holding-wrench'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/tools'
    aliases = ()
    keywords = ('wrench', 'hand', 'holding', 'grip', 'repair', 'mechanic', 'fix', 'tool')

    def build(self) -> None:
        self.add_polyline('wrench', (6, 6), (6, 16), (16, 24), (24, 24), (34, 16), (34, 6), (26, 10), (14, 10), (6, 6))
        self.add_polyline('thumb', (42, 30), (34, 30), (28, 24), (16, 24), (12, 28), (16, 32), (24, 32))
        self.add_polyline('hand', (16, 32), (12, 36), (18, 42), (32, 42), (36, 38), (42, 38))
        self.relate('connect', 'wrench', 'thumb')
        self.relate('connect', 'thumb', 'hand')

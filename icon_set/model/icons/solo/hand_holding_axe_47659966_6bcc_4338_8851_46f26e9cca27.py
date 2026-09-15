# Repair: Move the fist knuckle away from the axe blade, preserving the shaft grip.
"""A fist grips a diagonal axe; crowded finger creases and forearm waves omitted while retaining the thumb contour and protruding shaft."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '47659966-6bcc-4338-8851-46f26e9cca27'
SOURCE_PATH = 'pictographic-primitives/tools/tools axe hold_47659966-6bcc-4338-8851-46f26e9cca27.svg'
AUTHOR = 'gpt-6'

class HandHoldingAxe(Solo48):
    icon_id = 'hand-holding-axe'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/tools'
    aliases = ()
    keywords = ('axe', 'hand', 'holding', 'grip', 'chop', 'lumberjack', 'wood', 'tool')

    def build(self) -> None:
        self.add_polyline('axe', (24, 6), (18, 14), (30, 22), (42, 16), (36, 6), closed=True)
        self.add_line('shaft-upper', (30, 22), (24, 28))
        self.relate('connect', 'shaft-upper', 'axe')
        self.add_polyline('fist', (12, 22), (24, 28), (30, 30), (26, 38), (16, 38), (6, 28), (12, 22))
        self.relate('connect', 'shaft-upper', 'fist')
        self.add_line('shaft-lower', (16, 38), (12, 42))
        self.relate('connect', 'shaft-lower', 'fist')

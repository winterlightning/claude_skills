"""Upright plunger with capsule grip, shaft and domed rubber cup. No close Lucide subject match; geometric capsule and half-circle construction.

SOLO48 VRECT_L; geometry authored from its exact centerline extremes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b15b5df3-6dde-4ab7-88f6-b70887ad1a96'
SOURCE_PATH = 'pictographic-primitives/symbol/plunger_b15b5df3-6dde-4ab7-88f6-b70887ad1a96.svg'
AUTHOR = 'gpt-6'

class Plunger(Solo48):
    icon_id = 'plunger'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    categories = ('symbol', 'state')
    aliases = ()
    keywords = ('plunger', 'toilet', 'plumbing', 'unclog', 'drain', 'bathroom', 'cleaning', 'tool')

    def build(self) -> None:
        # Height repair: exact SOLO48 keyshape extremes; original subject and stroke retained.
        self.add_arc('grip-top', (20, 8), (28, 8), radius_x=4)
        self.add_line('grip-right', (28, 8), (28, 18))
        self.add_arc('grip-bottom-right', (28, 18), (24, 22), radius_x=4)
        self.add_arc('grip-bottom-left', (24, 22), (20, 18), radius_x=4)
        self.add_line('grip-left', (20, 18), (20, 8))
        self.add_contour('grip', 'grip-top', 'grip-right', 'grip-bottom-right', 'grip-bottom-left', 'grip-left', closed=True)
        self.add_line('shaft', (24, 22), (24, 28))
        self.add_arc('cup-right', (24, 28), (40, 44), radius_x=16)
        self.add_line('cup-base', (40, 44), (8, 44))
        self.add_arc('cup-left', (8, 44), (24, 28), radius_x=16)
        self.add_contour('cup', 'cup-right', 'cup-base', 'cup-left', closed=True)
        self.relate('connect', 'grip', 'shaft')
        self.relate('connect', 'cup', 'shaft')

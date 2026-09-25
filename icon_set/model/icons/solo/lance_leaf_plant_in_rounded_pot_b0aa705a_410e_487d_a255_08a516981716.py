"""Lowered the crown tip and raised the pot base; retained all three leaves.

Keyshape VRECT_L: visible bounds (6, 2, 42, 46).
Reference: No useful exact match.
"""
# Independent repair of lance-leaf-plant-in-rounded-pot; parent preserved.
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b0aa705a-410e-487d-a255-08a516981716'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-05/vase plant_b0aa705a-410e-487d-a255-08a516981716.svg'
AUTHOR = 'gpt-6'

class LanceLeafPlantInRoundedPot(Solo48):
    icon_id = 'lance-leaf-plant-in-rounded-pot'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'decoration'
    categories = ('primitives', 'decoration')
    aliases = ()
    keywords = ('lance', 'leaf', 'plant', 'in', 'rounded', 'pot')

    # Symbol plan: retain the subject and shared attachment stations;
    # fit the current keyshape by adjusting the owning cap, base or repeat.
    def build(self):
        self.add_arc('left-outer', (8, 8), (24, 32), radius_x=30, sweep=False)
        self.add_arc('left-inner', (24, 32), (18, 16), radius_x=30, sweep=False)
        self.add_line('left-tip', (18, 16), (8, 8))
        self.add_contour('left-leaf', 'left-outer', 'left-inner', 'left-tip', closed=True)
        self.add_line('right-tip', (40, 8), (30, 16))
        self.add_arc('right-inner', (30, 16), (24, 32), radius_x=30, sweep=False)
        self.add_arc('right-outer', (24, 32), (40, 8), radius_x=30, sweep=False)
        self.add_contour('right-leaf', 'right-tip', 'right-inner', 'right-outer', closed=True)
        self.relate('connect', 'left-leaf', 'right-leaf')
        self.add_arc('crown-left', (18, 16), (24, 4), radius_x=32)
        self.add_arc('crown-right', (24, 4), (30, 16), radius_x=32)
        self.add_contour('crown', 'crown-left', 'crown-right')
        self.add_line('rim-left', (12, 32), (24, 32))
        self.add_line('rim-right', (24, 32), (36, 32))
        self.add_line('pot-right', (36, 32), (36, 38))
        self.add_arc('pot-br', (36, 38), (30, 44), radius_x=6)
        self.add_line('pot-base', (30, 44), (18, 44))
        self.add_arc('pot-bl', (18, 44), (12, 38), radius_x=6)
        self.add_line('pot-left', (12, 38), (12, 32))
        self.add_contour('pot', 'rim-left', 'rim-right', 'pot-right', 'pot-br', 'pot-base', 'pot-bl', 'pot-left', closed=True)
        self.relate('connect', 'left-leaf', 'pot')
        self.relate('connect', 'right-leaf', 'pot')
        self.relate('connect', 'crown', 'left-leaf')
        self.relate('connect', 'crown', 'right-leaf')

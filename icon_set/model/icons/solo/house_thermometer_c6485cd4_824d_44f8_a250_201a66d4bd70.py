"""house thermometer: fresh SOLO48 repair.
Plan: Mirrored tube and rounded bulb; matched tube walls.
Keyshape: SQUARE. House surrounds a centered vertical thermometer.
Omissions: Mercury stroke omitted to leave a legible open tube.
Construction reference: house: joined roof and rounded base corners.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c6485cd4-824d-44f8-a250-201a66d4bd70'
SOURCE_PATH = 'pictographic-primitives/other/house thermometer_c6485cd4-824d-44f8-a250-201a66d4bd70.svg'
AUTHOR = 'gpt-6'
PARENT_SOURCE = 'icon_set/model/icons/solo/house_thermometer_c6485cd4_824d_44f8_a250_201a66d4bd70.py'

class Drawing(Solo48):
    icon_id = 'house-thermometer'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('house', 'thermometer')

    def house(self):
        self.add_line('roof-1', (6, 14), (24, 6))
        self.add_line('roof-2', (24, 6), (42, 14))
        self.add_line('wall-right', (42, 14), (42, 40))
        self.add_arc('corner-right', (42, 40), (40, 42), radius_x=2)
        self.add_line('floor', (40, 42), (8, 42))
        self.add_arc('corner-left', (8, 42), (6, 40), radius_x=2)
        self.add_line('wall-left', (6, 40), (6, 14))
        self.add_contour('house', 'roof-1', 'roof-2', 'wall-right', 'corner-right', 'floor', 'corner-left', 'wall-left', closed=True)

    def build(self):
        self.house()
        self.add_arc('cap', (20, 20), (28, 20), radius_x=4)
        self.add_line('tube-right', (28, 20), (28, 27))
        self.add_bezier('bulb-right', (28, 27), ((32, 30), (30, 33), (24, 33)))
        self.add_bezier('bulb-left', (24, 33), ((18, 33), (16, 30), (20, 27)))
        self.add_line('tube-left', (20, 27), (20, 20))
        self.add_contour('thermometer', 'cap', 'tube-right', 'bulb-right', 'bulb-left', 'tube-left', closed=True)

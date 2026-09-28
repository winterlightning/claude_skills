"""Revision of the claimed reference after comparing original and rejected drawing."""
"""house thermometer: fresh SOLO48 repair.
Plan: Mirrored tube and rounded bulb; matched tube walls.
Keyshape: SQUARE. House surrounds a centered vertical thermometer.
Omissions: Mercury stroke omitted to leave a legible open tube.
Construction reference: house: joined roof and rounded base corners.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'c6485cd4-824d-44f8-a250-201a66d4bd70'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__house-thermometer/20260927T142529Z-thuan-mac-1/reference/house thermometer_c6485cd4-824d-44f8-a250-201a66d4bd70.svg'
AUTHOR = 'gpt-6'
PARENT_SOURCE = 'icon_set/model/icons/solo/house_thermometer_c6485cd4_824d_44f8_a250_201a66d4bd70.py'

class Drawing(Solo48):
    icon_id = 'house-thermometer'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('other', 'primitives-generate')
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
        # A narrow stem enters a distinct circular bulb.
        self.house()
        self.add_line('tube',(24,17),(24,25))
        self.add_arc('bulb-a',(20,29),(24,25),radius_x=4)
        self.add_arc('bulb-b',(24,25),(28,29),radius_x=4)
        self.add_arc('bulb-c',(28,29),(20,29),radius_x=4)
        self.add_contour('bulb','bulb-a','bulb-b','bulb-c',closed=True)
        self.relate('connect','tube','bulb')

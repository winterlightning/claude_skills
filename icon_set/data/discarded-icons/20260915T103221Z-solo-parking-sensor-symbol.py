"""Parking sensor symbol; independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0e0c3c55-82f6-46b5-83b1-967b4389b677'
SOURCE_PATH = 'pictographic-primitives/transportation/parkig aid system_0e0c3c55-82f6-46b5-83b1-967b4389b677.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = [{'SOURCE_ICON_ID': '0e0c3c55-82f6-46b5-83b1-967b4389b677', 'SOURCE_PATH': 'pictographic-primitives/transportation/parkig aid system_0e0c3c55-82f6-46b5-83b1-967b4389b677.svg', 'AUTHOR': 'gpt-6'}]

class ParkingSensorSymbol(Solo48):
    icon_id = 'parking-sensor-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('parking', 'sensor', 'symbol')

    def build(self) -> None:
        # SQUARE (6,6)-(42,42). P transmitter, one signal arc and a triangular obstacle.
        self.add_line('p-stem',(6,26),(6,18))
        self.add_line('p-upright',(6,18),(6,6))
        self.add_line('p-top',(6,6),(12,6))
        self.add_arc('p-bowl',(12,6),(12,18),radius_x=6)
        self.add_line('p-base',(12,18),(6,18))
        self.add_contour('p-loop','p-upright','p-top','p-bowl','p-base',closed=True)
        self.relate('connect','p-loop','p-stem')
        self.add_arc('sonar',(28,8),(16,30),radius_x=25)
        self.add_polyline('obstacle',(26,42),(34,26),(42,42),(26,42))

"""A location pin above a ground line. VRECT_L extremes (8,6)-(40,42). Lucide map-pin informs the arched cap, tapered point and inner ring. Shorten the pin to retain a clear gap above its ground line."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '632bbd50-870e-4274-87d8-51bc5834f214'
SOURCE_PATH = 'pictographic-primitives/symbol/location dot_632bbd50-870e-4274-87d8-51bc5834f214.svg'
AUTHOR = 'gpt-6'

class LocationPinGround(Solo48):
    icon_id = 'location-pin-ground'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    categories = ('symbol',)
    aliases = ()
    keywords = ('location', 'pin', 'map', 'place', 'marker', 'gps', 'destination', 'address')

    def build(self) -> None:
        # Height repair: exact SOLO48 keyshape extremes; original subject and stroke retained.
        self.add_arc('cap', (8, 16), (40, 16), radius_x=16, radius_y=12)
        self.add_arc('right-turn', (40, 16), (36, 25), radius_x=20, radius_y=15)
        self.add_line('right-tip', (36, 25), (24, 34))
        self.add_line('left-tip', (24, 34), (12, 25))
        self.add_arc('left-turn', (12, 25), (8, 16), radius_x=20, radius_y=15)
        self.add_contour('pin', 'cap', 'right-turn', 'right-tip', 'left-tip', 'left-turn', closed=True)
        cx, cy, radius = (24, 16, 3)
        self.add_arc('ring-top', (cx - radius, cy), (cx + radius, cy), radius_x=radius)
        self.add_arc('ring-bottom', (cx + radius, cy), (cx - radius, cy), radius_x=radius)
        self.add_contour('ring', 'ring-top', 'ring-bottom', closed=True)
        self.add_line('ground', (16, 44), (32, 44))

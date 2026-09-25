from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7ac2fe90-9ec6-57d3-93e3-bdf2c5c77136'
SOURCE_PATH = 'pictographic-primitives/transportation/railway station_7ac2fe90-9ec6-57d3-93e3-bdf2c5c77136.svg'
AUTHOR = 'gpt-6'

class StationHouseClock(Solo48):
    icon_id = 'station-house-clock'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    categories = ('transportation', 'primitives')
    aliases = ()
    keywords = ('railway station', 'station', 'clock', 'building', 'train station', 'depot', 'terminal', 'platform')

    def build(self):
        """Remove the tiny crowded hour hand; the clear clock face and vertical hand retain the station clock."""
        self.add_polyline('walls', (20, 44), (8, 44), (8, 18), (24, 4), (40, 18), (40, 44), (28, 44))
        self.add_arc('door', (28, 44), (20, 44), radius_x=4, sweep=False)
        self.relate('connect', 'walls', 'door')
        self.add_arc('clock-left', (24, 17), (24, 31), radius_x=7, sweep=False)
        self.add_arc('clock-right', (24, 31), (24, 17), radius_x=7, sweep=False)
        self.add_contour('clock', 'clock-left', 'clock-right', closed=True)
        self.add_polyline('hands', (24, 17), (24, 24))
        self.relate('connect', 'clock', 'hands')

'A stopwatch with a top button and diagonal hand.\nConstruction: Vertical centerlines (8,6)-(40,42) fit the top button over a near-circular dial. One short diagonal hand; omit the tiny stem and tick marks.\nLucide: timer: circle with a detached top button and short diagonal hand.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '952d9622-3556-4093-94f3-d074e7fb8919'
SOURCE_PATH = 'pictographic-primitives/sports/timer_952d9622-3556-4093-94f3-d074e7fb8919.svg'
AUTHOR = 'gpt-6'

class SportsStopwatch(Solo48):
    icon_id = 'sports-stopwatch'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/sports"
    aliases = ()
    keywords = ('sports', 'stopwatch', 'sport')

    def build(self):
        self.add_arc('dial-top', (8, 29), (40, 29), radius_x=16, radius_y=15, sweep=True)
        self.add_arc('dial-bottom', (40, 29), (8, 29), radius_x=16, radius_y=15, sweep=True)
        self.add_contour('dial', 'dial-top', 'dial-bottom', closed=True)
        self.add_line('button', (20, 6), (28, 6))
        self.add_line('hand', (24, 29), (28, 25))

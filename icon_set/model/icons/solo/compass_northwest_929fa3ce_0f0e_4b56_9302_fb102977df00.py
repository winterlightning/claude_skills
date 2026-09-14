"""A circular compass dial encloses an arrowhead-shaped needle aimed toward the upper left. Four short tick marks project inward at the cardinal positions around the rim.

Cardinal ticks omitted to protect the needle clearance; directional asymmetry is essential.
Construction reference: Lucide compass: clean circle and central diagonal pointer.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '929fa3ce-0f0e-4b56-9302-fb102977df00'
SOURCE_PATH = 'pictographic-primitives/weather/north west nnw_929fa3ce-0f0e-4b56-9302-fb102977df00.svg'
AUTHOR = 'gpt-6'

class CompassNorthwest(Solo48):
    icon_id = 'compass-northwest'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/weather"
    aliases = ()
    keywords = ('compass', 'northwest', 'direction', 'navigation', 'bearing', 'dial')

    def build(self) -> None:
        # Live CIRCLE visible bounds: (2, 2, 46, 46).
        self.add_arc('dial-top', (4, 24), (44, 24), radius_x=20, radius_y=20, sweep=True, large_arc=False)
        self.add_arc('dial-bottom', (44, 24), (4, 24), radius_x=20, radius_y=20, sweep=True, large_arc=False)
        self.add_contour('dial', 'dial-top', 'dial-bottom', closed=True)
        self.add_polyline('needle', (16, 16), (33, 24), (25, 26), (24, 33), closed=True)

"""A circular compass dial surrounds a triangular pointer aimed toward the upper left. Four short cardinal ticks project inward from the rim around the otherwise empty dial.

Cardinal ticks omitted to protect the needle clearance; directional asymmetry is essential.
Construction reference: Lucide compass: clean circle and central diagonal pointer.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c63f16f0-ecad-43f9-b75e-7718b21369f5'
SOURCE_PATH = 'pictographic-primitives/weather/north west_c63f16f0-ecad-43f9-b75e-7718b21369f5.svg'
AUTHOR = 'gpt-6'

class CompassNorthwestTriangle(Solo48):
    icon_id = 'compass-northwest-triangle'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/weather"
    aliases = ()
    keywords = ('compass', 'northwest', 'direction', 'navigation', 'bearing', 'dial')

    def build(self) -> None:
        # Live CIRCLE visible bounds: (2, 2, 46, 46).
        self.add_arc('dial-top', (6, 24), (42, 24), radius_x=20, radius_y=20, sweep=True, large_arc=False)
        self.add_arc('dial-bottom', (42, 24), (6, 24), radius_x=20, radius_y=20, sweep=True, large_arc=False)
        self.add_contour('dial', 'dial-top', 'dial-bottom', closed=True)
        self.add_polyline('needle', (16, 16), (33, 24), (24, 33), closed=True)

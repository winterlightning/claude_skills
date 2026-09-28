"""A round compass dial has four inward cardinal ticks. A long diamond-shaped needle crosses the center from lower left to upper right, divided across its middle into two pointed halves.

Cardinal ticks omitted to protect the needle clearance; directional asymmetry is essential.
Construction reference: Lucide compass: clean circle and central diagonal pointer.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '563debf3-e47a-45f3-a251-5724e7b03a45'
SOURCE_PATH = 'pictographic-primitives/weather/north east nne_563debf3-e47a-45f3-a251-5724e7b03a45.svg'
AUTHOR = 'gpt-6'

class CompassNortheast(Solo48):
    icon_id = 'compass-northeast'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "weather"
    categories = ("weather", "primitives")
    aliases = ()
    keywords = ('compass', 'northeast', 'direction', 'navigation', 'bearing', 'dial')

    def build(self) -> None:
        # Live CIRCLE visible bounds: (2, 2, 46, 46).
        self.add_arc('dial-top', (4, 24), (44, 24), radius_x=20, radius_y=20, sweep=True, large_arc=False)
        self.add_arc('dial-bottom', (44, 24), (4, 24), radius_x=20, radius_y=20, sweep=True, large_arc=False)
        self.add_contour('dial', 'dial-top', 'dial-bottom', closed=True)
        self.add_polyline('needle', (17, 31), (20, 20), (31, 17), (28, 28), closed=True)

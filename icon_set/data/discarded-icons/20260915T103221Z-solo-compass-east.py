"""A circular compass dial has four inward tick marks and an arrow-shaped needle pointing toward the upper right. A capital E sits directly beneath the dial.

Opened the lower dial and simplified the pointer to an open arrow so the E legend can retain three clearly separated bars; cardinal ticks omitted.
Construction reference: Lucide compass: circle with geometric pointer.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ad12d3ce-dd3a-4c8e-9db3-83b54c4a1c0b'
SOURCE_PATH = 'pictographic-primitives/weather/east_ad12d3ce-dd3a-4c8e-9db3-83b54c4a1c0b.svg'
AUTHOR = 'gpt-6'

class CompassEast(Solo48):
    icon_id = 'compass-east'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/weather'
    aliases = ()
    keywords = ('compass', 'east', 'direction', 'navigation', 'bearing', 'dial')

    def build(self) -> None:
        # Height repair: exact SOLO48 keyshape extremes; original subject and stroke retained.
        self.add_line('dial-left', (8, 32), (8, 20))
        self.add_arc('dial-top', (8, 20), (40, 20), radius_x=16, radius_y=16, sweep=True, large_arc=False)
        self.add_contour('dial', 'dial-left', 'dial-top', closed=False)
        self.add_polyline('needle', (18, 18), (28, 14), (24, 23), closed=False)
        self.add_polyline('legend', (38, 44), (32, 44), (32, 28), (38, 28), closed=False)
        self.add_line('legend-middle', (32, 36), (38, 36))
        self.relate('connect', 'legend', 'legend-middle')

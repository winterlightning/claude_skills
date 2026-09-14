# Variant of car-skidding; parent file remains unchanged.
"""Car Skidding. Retains two clearly curved skid tracks; omits short wheel stubs to allocate a nine-unit gap below the car body.

VRECT_L visible extremes (6, 2, 42, 46); centerlines (8, 4, 40, 44).
Lucide car-front: trapezoidal cabin and plain rounded body; supplied source determines the paired skid tracks.
Repeated features share dimensions; deliberate asymmetry preserves the
letter order, handles and chart heights. Authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9ba9924a-41d3-4ed9-93c5-d475f8bd2fd2'
SOURCE_PATH = 'pictographic-primitives/symbol/car with wave lines_9ba9924a-41d3-4ed9-93c5-d475f8bd2fd2.svg'
AUTHOR = 'gpt-6'

class CarSkiddingVariant2(Solo48):
    icon_id = 'car-skidding-v2'
    variant_of = 'car-skidding'
    variant_label = 'Height envelope and full spacing repair'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbols/standalone'
    aliases = ()
    keywords = ('car', 'skid', 'slippery', 'road', 'traction', 'warning', 'driving', 'vehicle')

    def build(self) -> None:
        self.add_line('body-top-1', (11, 14), (14, 14))
        self.add_line('body-top-2', (14, 14), (34, 14))
        self.add_line('body-top-3', (34, 14), (37, 14))
        self.add_arc('body-ne', (37, 14), (40, 17), radius_x=3, radius_y=3, sweep=True)
        self.add_line('body-right', (40, 17), (40, 20))
        self.add_arc('body-se', (40, 20), (37, 23), radius_x=3, radius_y=3, sweep=True)
        self.add_line('body-bottom-1', (37, 23), (11, 23))
        self.add_arc('body-sw', (11, 23), (8, 20), radius_x=3, radius_y=3, sweep=True)
        self.add_line('body-left', (8, 20), (8, 17))
        self.add_arc('body-nw', (8, 17), (11, 14), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('body', 'body-top-1', 'body-top-2', 'body-top-3', 'body-ne', 'body-right', 'body-se', 'body-bottom-1', 'body-sw', 'body-left', 'body-nw', closed=True)
        self.add_polyline('cabin', (14, 14), (18, 6), (30, 6), (34, 14))
        self.relate('connect', 'body', 'cabin')
        self.add_arc('left-track-a', (16, 32), (16, 38), radius_x=4, radius_y=3, sweep=False)
        self.add_arc('left-track-b', (16, 38), (16, 42), radius_x=4, radius_y=3, sweep=True)
        self.add_contour('left-track', 'left-track-a', 'left-track-b')
        self.add_arc('right-track-a', (32, 32), (32, 38), radius_x=4, radius_y=3, sweep=False)
        self.add_arc('right-track-b', (32, 38), (32, 42), radius_x=4, radius_y=3, sweep=True)
        self.add_contour('right-track', 'right-track-a', 'right-track-b')

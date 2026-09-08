"""Three-arm candelabra on a table. VRECT_XL (5,2)-(43,46). Repeated circular arm bends follow Lucide-style tangent construction; no exact match. Flames become short strokes and ornate foot becomes a simple base."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1fd0448b-e249-5adc-9797-e731d5823281'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-04/table candelabra_1fd0448b-e249-5adc-9797-e731d5823281.svg'
AUTHOR = 'gpt-6'


class TabletopThreeArmCandelabra(Solo48):
    icon_id = 'tabletop-three-arm-candelabra'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/decoration"
    aliases = ()
    keywords = ('candelabra', 'candles', 'flames', 'table', 'holder', 'decor', 'lighting')

    def build(self) -> None:
        self.add_line('left-flame', (10, 7), (10, 10))
        self.add_line('left-candle', (10, 17), (10, 24))
        self.add_line('centre-flame', (24, 2), (24, 5))
        self.add_line('centre-candle', (24, 12), (24, 38))
        self.add_line('right-flame', (38, 7), (38, 10))
        self.add_line('right-candle', (38, 17), (38, 24))
        self.add_arc('arm-left', (10, 24), (24, 24), radius_x=7, radius_y=7, sweep=False, large_arc=False)
        self.add_arc('arm-right', (24, 24), (38, 24), radius_x=7, radius_y=7, sweep=False, large_arc=False)
        self.add_contour('arms', 'arm-left', 'arm-right', closed=False)
        self.relate('connect', 'arms', 'left-candle')
        self.relate('connect', 'arms', 'centre-candle')
        self.relate('connect', 'arms', 'right-candle')
        self.add_line('foot', (17, 38), (31, 38))
        self.relate('connect', 'foot', 'centre-candle')
        self.add_line('table', (5, 38), (43, 38))
        self.relate('connect', 'foot', 'table')
        self.relate('connect', 'centre-candle', 'table')
        self.add_line('leg-left', (8, 38), (8, 46))
        self.add_line('leg-right', (40, 38), (40, 46))
        self.relate('connect', 'table', 'leg-left')
        self.relate('connect', 'table', 'leg-right')

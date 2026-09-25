"""Beer Mug. Retains the identifying silhouette and visible features.

SQUARE visible extremes (4, 4, 44, 44); centerlines (6, 6, 42, 42).
Lucide beer: foam cap, rounded mug bottom and attached loop handle; no added internal fluting.
Repeated features share dimensions; deliberate asymmetry preserves the
letter order, handles and chart heights. Authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5429b76f-075c-4738-87f2-f8390c36df79'
SOURCE_PATH = 'pictographic-primitives/symbol/beer_5429b76f-075c-4738-87f2-f8390c36df79.svg'
AUTHOR = 'gpt-6'


class BeerMug(Solo48):
    icon_id = 'beer-mug'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    aliases = ()
    keywords = ('beer', 'mug', 'drink', 'pub', 'alcohol', 'foam', 'bar', 'beverage')

    def build(self) -> None:
        self.add_arc('foam-left', (8, 18), (6, 16), radius_x=2, radius_y=2, sweep=True)
        self.add_arc('foam-lobe-left', (6, 16), (14, 8), radius_x=8, radius_y=8, sweep=True)
        self.add_arc('foam-top', (14, 8), (24, 8), radius_x=5, radius_y=2, sweep=True)
        self.add_arc('foam-right', (24, 8), (30, 14), radius_x=6, radius_y=6, sweep=True)
        self.add_line('foam-edge', (30, 14), (30, 18))
        self.add_line('right-wall-1', (30, 18), (30, 22))
        self.add_line('right-wall-2', (30, 22), (30, 34))
        self.add_line('right-wall-3', (30, 34), (30, 38))
        self.add_arc('bottom-right', (30, 38), (26, 42), radius_x=4, radius_y=4, sweep=True)
        self.add_line('bottom', (26, 42), (12, 42))
        self.add_arc('bottom-left', (12, 42), (8, 38), radius_x=4, radius_y=4, sweep=True)
        self.add_line('left-wall', (8, 38), (8, 18))
        self.add_contour('mug', 'foam-left', 'foam-lobe-left', 'foam-top', 'foam-right', 'foam-edge', 'right-wall-1', 'right-wall-2', 'right-wall-3', 'bottom-right', 'bottom', 'bottom-left', 'left-wall', closed=True)
        self.add_line('rim', (8, 18), (30, 18))
        self.relate("connect", 'mug', 'rim')
        self.add_line('handle-top', (30, 22), (38, 22))
        self.add_arc('handle-ne', (38, 22), (42, 26), radius_x=4, radius_y=4, sweep=True)
        self.add_line('handle-right', (42, 26), (42, 30))
        self.add_arc('handle-se', (42, 30), (38, 34), radius_x=4, radius_y=4, sweep=True)
        self.add_line('handle-bottom', (38, 34), (30, 34))
        self.add_contour('handle', 'handle-top', 'handle-ne', 'handle-right', 'handle-se', 'handle-bottom')
        self.relate("connect", 'mug', 'handle')

"""A caterpillar toy with a round head and two descending rounded body lobes. Three broad segments and open antenna tips replace crowded overlapping beads; deliberate directional asymmetry."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b5c1ac54-b49a-4df4-acfe-b33a9fa9b695'
SOURCE_PATH = 'pictographic-primitives/babies/toys caterpillar_b5c1ac54-b49a-4df4-acfe-b33a9fa9b695.svg'
AUTHOR = 'gpt-6'


class CaterpillarToy(Solo48):
    icon_id = 'caterpillar-toy'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "babies"
    categories = ("babies", "primitives")
    aliases = ()
    keywords = ('caterpillar', 'toy', 'infant', 'nursery')

    def build(self) -> None:
        # Envelope repair: shared boundary nodes and cardinal curve extrema;
        # retain the subject, grid, stroke, and declared physical joins.
        # Centerline extremes: (6,6)-(42,42).
        self.add_arc('head-top', (6, 16), (22, 16), radius_x=10, radius_y=10, sweep=True, large_arc=False)
        self.add_arc('head-bottom', (22, 16), (6, 16), radius_x=10, radius_y=10, sweep=True, large_arc=False)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_arc('body-upper', (22, 16), (34, 28), radius_x=12, radius_y=12, sweep=True, large_arc=False)
        self.add_arc('body-lower', (34, 28), (22, 40), radius_x=12, radius_y=12, sweep=True, large_arc=False)
        self.add_arc('body-front', (22, 40), (12, 26), radius_x=10, radius_y=14, sweep=True, large_arc=False)
        self.add_contour('body', 'body-upper', 'body-lower', 'body-front', closed=False)
        self.add_arc('tail-top', (34, 28), (42, 37), radius_x=8, radius_y=9, sweep=True, large_arc=False)
        self.add_arc('tail-tip', (42, 37), (37, 42), radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_arc('tail-bottom', (37, 42), (22, 40), radius_x=15, radius_y=2, sweep=True, large_arc=False)
        self.add_contour('tail', 'tail-top', 'tail-tip', 'tail-bottom', closed=False)
        self.add_polyline('antenna-left', (6, 8), (6, 6))
        self.add_polyline('antenna-right', (18, 8), (22, 6))
        self.relate("connect", 'head', 'antenna-left')
        self.relate("connect", 'head', 'antenna-right')
        self.relate("connect", 'head', 'body')
        self.relate("connect", 'body', 'tail')

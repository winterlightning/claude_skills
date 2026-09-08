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
    category = "people/babies"
    aliases = ()
    keywords = ('caterpillar', 'toy', 'infant', 'nursery')

    def build(self) -> None:
        # Centerline extremes: (2,2)-(46,46).
        self.add_arc('head-top', (2, 16), (22, 16), radius_x=10, radius_y=10, sweep=True, large_arc=False)
        self.add_arc('head-bottom', (22, 16), (2, 16), radius_x=10, radius_y=10, sweep=True, large_arc=False)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_arc('body-upper', (22, 16), (34, 28), radius_x=12, radius_y=12, sweep=True, large_arc=False)
        self.add_arc('body-lower', (34, 28), (22, 40), radius_x=12, radius_y=12, sweep=True, large_arc=False)
        self.add_arc('body-front', (22, 40), (12, 26), radius_x=10, radius_y=14, sweep=True, large_arc=False)
        self.add_contour('body', 'body-upper', 'body-lower', 'body-front', closed=False)
        self.add_arc('tail-top', (34, 28), (46, 37), radius_x=12, radius_y=9, sweep=True, large_arc=False)
        self.add_arc('tail-tip', (46, 37), (37, 46), radius_x=9, radius_y=9, sweep=True, large_arc=False)
        self.add_arc('tail-bottom', (37, 46), (22, 40), radius_x=15, radius_y=6, sweep=True, large_arc=False)
        self.add_contour('tail', 'tail-top', 'tail-tip', 'tail-bottom', closed=False)
        self.add_polyline('antenna-left', (6, 8), (3, 2))
        self.add_polyline('antenna-right', (18, 8), (22, 2))
        self.relate("connect", 'head', 'antenna-left')
        self.relate("connect", 'head', 'antenna-right')
        self.relate("connect", 'head', 'body')
        self.relate("connect", 'body', 'tail')

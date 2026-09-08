"""Flamingo with long neck and one supporting leg; extremes (8,2)-(40,46). Open neck and crescent body preserve clear space; tucked leg reduced to a bent stroke."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0eedad4e-672e-40c7-9399-bd5db48d8049'
SOURCE_PATH = 'pictographic-primitives/animals/wild bird flamingo_0eedad4e-672e-40c7-9399-bd5db48d8049.svg'
AUTHOR = 'gpt-6'


class Flamingo(Solo48):
    icon_id = 'flamingo'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('flamingo', 'standing', 'one leg', 'bird', 'pink', 'tropical', 'wading', 'beak')

    def build(self) -> None:
        self.add_arc('head', (26, 10), (34, 2), radius_x=8, radius_y=8, sweep=True)
        self.add_arc('head-front', (34, 2), (40, 10), radius_x=6, radius_y=8, sweep=True)
        self.add_line('beak', (40, 10), (33, 10))
        self.add_line('neck-front', (33, 10), (33, 23))
        self.add_arc('breast', (33, 23), (22, 34), radius_x=11, radius_y=11, sweep=True)
        self.add_arc('belly', (22, 34), (8, 30), radius_x=20, radius_y=10, sweep=True)
        self.add_arc('back', (8, 30), (26, 27), radius_x=12, radius_y=10, sweep=True)
        self.add_line('neck-back', (26, 27), (26, 10))
        self.add_contour('body', 'head', 'head-front', 'beak', 'neck-front', 'breast', 'belly', 'back', 'neck-back', closed=True)
        self.add_line('leg', (22, 34), (22, 46))
        self.relate("connect", 'leg', 'body')
        self.add_polyline('tucked-leg', (22, 34), (13, 41), (17, 41), closed=False)
        self.relate("connect", 'tucked-leg', 'body')

"""Seated person facing right with heat and low bench. Square extremes 6,6–42,42. Lucide user-round circular head; intentional profile asymmetry; one heat wisp, one leg and simplified arm."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '69ae7a1c-75de-43c9-b54f-3baeb9173095'
SOURCE_PATH = 'pictographic-primitives/spas/sauna heat person_69ae7a1c-75de-43c9-b54f-3baeb9173095.svg'
AUTHOR = 'gpt-6'

class SeatedSaunaBather(Solo48):
    icon_id = 'seated-sauna-bather'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/wellness"
    aliases = ()
    keywords = ('spa', 'wellness', 'seated-sauna-bather')

    def build(self):
        self.add_arc('head-top', (9,11), (19,11), radius_x=5, radius_y=5)
        self.add_arc('head-bottom', (19,11), (9,11), radius_x=5, radius_y=5)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_polyline('person', (14,25), (14,31), (30,31), (36,42))
        self.add_line('arm', (14,25), (25,23))
        self.add_polyline('bench', (6,42), (6,39), (23,39), (23,42))
        self.add_arc('heat-top', (40,6), (40,14), radius_x=2, radius_y=4)
        self.add_arc('heat-bottom', (40,14), (40,22), radius_x=2, radius_y=4, sweep=False)
        self.add_contour('heat', 'heat-top', 'heat-bottom')
        self.relate('connect', 'person', 'arm')

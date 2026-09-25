"""Front-facing bather in steaming pool, a natural scene. Square extremes 6,6–42,42. Lucide user-round head and shoulders; shared bilateral layout; reduce four steam trails to two and use a single shoulder arch for the partially immersed torso."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b94cca4b-3af8-4e51-83cc-683432d67936'
SOURCE_PATH = 'pictographic-primitives/spas/sauna heat person_b94cca4b-3af8-4e51-83cc-683432d67936.svg'
AUTHOR = 'gpt-6'

class BatherInSteamingPool(Solo48):
    icon_id = 'bather-in-steaming-pool'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "spas"
    aliases = ()
    keywords = ('spa', 'wellness', 'bather-in-steaming-pool')

    def build(self):
        self.add_arc('head-top', (18,12), (30,12), radius_x=6, radius_y=6)
        self.add_arc('head-bottom', (30,12), (18,12), radius_x=6, radius_y=6)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_arc('shoulders', (17,32), (31,32), radius_x=7, radius_y=5)
        self.add_arc('pool', (6,31), (42,31), radius_x=18, radius_y=11, sweep=False)
        for x in (8,40):
            self.add_arc(f'heat-{x}-top', (x,6), (x,14), radius_x=2, radius_y=4)
            self.add_arc(f'heat-{x}-bottom', (x,14), (x,22), radius_x=2, radius_y=4, sweep=False)
            self.add_contour(f'heat-{x}', f'heat-{x}-top', f'heat-{x}-bottom')

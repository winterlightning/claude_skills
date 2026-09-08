"""Kiwi with a round wingless body, long bill and two feet. Lucide bird: coherent round body and sparse marks."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e7f198e2-850a-485d-8d8d-49ce1c496222'
SOURCE_PATH = 'pictographic-primitives/animals/wild bird_e7f198e2-850a-485d-8d8d-49ce1c496222.svg'
AUTHOR = 'gpt-6'


class KiwiBird(Solo48):
    icon_id = 'kiwi-bird'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/animals"
    aliases = ()
    keywords = ('kiwi', 'bird', 'beak', 'new zealand', 'flightless', 'round', 'long beak', 'wildlife')

    def build(self) -> None:
        self.add_arc('back', (2, 25), (15, 12), radius_x=13, radius_y=13, sweep=True)
        self.add_arc('shoulder', (15, 12), (23, 8), radius_x=10, radius_y=10, sweep=False)
        self.add_arc('head', (23, 8), (32, 17), radius_x=9, radius_y=9, sweep=True)
        self.add_arc('throat', (32, 17), (26, 26), radius_x=9, radius_y=9, sweep=False)
        self.add_arc('belly-front', (26, 26), (20, 34), radius_x=8, radius_y=8, sweep=True)
        self.add_line('belly', (20, 34), (11, 34))
        self.add_arc('rump', (11, 34), (2, 25), radius_x=9, radius_y=9, sweep=True)
        self.add_contour('outline', 'back', 'shoulder', 'head', 'throat', 'belly-front', 'belly', 'rump', closed=True)
        self.add_arc('beak', (32, 17), (46, 29), radius_x=24, radius_y=24, sweep=True)
        self.relate("connect", 'outline', 'beak')
        self.add_line('left-leg-1', (11, 34), (10, 40))
        self.add_line('left-leg-2', (10, 40), (6, 40))
        self.add_contour('left-leg', 'left-leg-1', 'left-leg-2', closed=False)
        self.add_line('right-leg-1', (20, 34), (24, 40))
        self.add_line('right-leg-2', (24, 40), (28, 40))
        self.add_contour('right-leg', 'right-leg-1', 'right-leg-2', closed=False)
        self.relate("connect", 'outline', 'left-leg')
        self.relate("connect", 'outline', 'right-leg')
        self.add_dot('eye', (21, 18))

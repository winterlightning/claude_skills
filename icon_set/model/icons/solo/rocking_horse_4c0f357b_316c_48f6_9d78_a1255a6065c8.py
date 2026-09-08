"""Left-facing rocking horse with broad arched belly. Lucide rocking-chair informs the single rocker; tiny ear and tail curl omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4c0f357b-316c-48f6-9d78-a1255a6065c8'
SOURCE_PATH = 'pictographic-primitives/babies/toys rocking horse_4c0f357b-316c-48f6-9d78-a1255a6065c8.svg'
AUTHOR = 'gpt-6'


class RockingHorse(Solo48):
    icon_id = 'rocking-horse'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/baby"
    aliases = ()
    keywords = ('rocking', 'horse', 'baby', 'nursery', 'toy')

    def build(self) -> None:
        # Centerline keyshape: HRECT_XL; Left-facing rocking horse with broad arched belly. Lucide rocking-chair informs the single rocker; tiny ear and tail curl omitted.
        self.add_polyline('head', (18, 5), (8, 10), (5, 17), (11, 21), (17, 17), (20, 27), (12, 43), closed=False)
        self.add_polyline('back', (18, 5), (24, 20), (35, 20), closed=False)
        self.relate("connect", 'head', 'back')
        self.add_arc('rump', (35, 20), (40, 25), radius_x=5, radius_y=5, sweep=True)
        self.add_line('rear-leg', (40, 25), (36, 43))
        self.add_contour('rear', 'rump', 'rear-leg', closed=False)
        self.relate("connect", 'back', 'rear')
        self.add_arc('belly', (12, 43), (36, 43), radius_x=13, radius_y=13, sweep=True)
        self.relate("connect", 'belly', 'head')
        self.relate("connect", 'belly', 'rear')
        self.add_arc('rocker-left', (2, 33), (12, 43), radius_x=10, radius_y=10, sweep=False)
        self.add_line('rocker-base', (12, 43), (36, 43))
        self.add_arc('rocker-right', (36, 43), (46, 33), radius_x=10, radius_y=10, sweep=False)
        self.add_contour('rocker', 'rocker-left', 'rocker-base', 'rocker-right', closed=False)
        self.relate("connect", 'rocker', 'head')
        self.relate("connect", 'rocker', 'rear')
        self.relate("connect", 'rocker', 'belly')

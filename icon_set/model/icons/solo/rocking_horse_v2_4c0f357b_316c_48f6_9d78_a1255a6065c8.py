# Independent revision; parent models preserved.
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4c0f357b-316c-48f6-9d78-a1255a6065c8'
SOURCE_PATH = 'pictographic-primitives/babies/toys rocking horse_4c0f357b-316c-48f6-9d78-a1255a6065c8.svg'
AUTHOR = 'gpt-6'

class RockingHorseVariant2(Solo48):
    icon_id = 'rocking-horse-v2'
    variant_of = 'rocking-horse'
    variant_label = 'Exact keyshape envelope and clear spacing'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/baby'
    aliases = ()
    keywords = ('rocking', 'horse', 'baby', 'nursery', 'toy')

    def build(self) -> None:
        self.add_polyline('head', (18, 6), (8, 10), (6, 17), (11, 21), (17, 17), (20, 27), (12, 42), closed=False)
        self.add_polyline('back', (18, 6), (24, 20), (35, 20), closed=False)
        self.relate('connect', 'head', 'back')
        self.add_arc('rump', (35, 20), (40, 25), radius_x=5, radius_y=5, sweep=True)
        self.add_line('rear-leg', (40, 25), (36, 42))
        self.add_contour('rear', 'rump', 'rear-leg', closed=False)
        self.relate('connect', 'back', 'rear')
        self.add_arc('belly', (12, 42), (36, 42), radius_x=13, radius_y=13, sweep=True)
        self.relate('connect', 'belly', 'head')
        self.relate('connect', 'belly', 'rear')
        self.add_arc('rocker-left', (6, 33), (12, 42), radius_x=10, radius_y=10, sweep=False)
        self.add_line('rocker-base', (12, 42), (36, 42))
        self.add_arc('rocker-right', (36, 42), (42, 33), radius_x=10, radius_y=10, sweep=False)
        self.add_contour('rocker', 'rocker-left', 'rocker-base', 'rocker-right', closed=False)
        self.relate('connect', 'rocker', 'head')
        self.relate('connect', 'rocker', 'rear')
        self.relate('connect', 'rocker', 'belly')

"""Dog Offering Paw.

Plan: Left-facing seated dog, pointed ear, projecting muzzle, raised forepaw and upward curling tail. Lower body owns broad haunch.
Centerline extremes: (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '520f29cc-1cbb-4177-b8b8-89624c81e125'
SOURCE_PATH = 'pictographic-primitives/pets/dog giving hand paw_520f29cc-1cbb-4177-b8b8-89624c81e125.svg'
AUTHOR = 'gpt-6'

class DogOfferingPawVariant2(Solo48):
    icon_id = 'dog-offering-paw-v2'
    variant_of = 'dog-offering-paw'
    variant_label = 'Hole and centerline reconstruction'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/pets'
    aliases = ()
    keywords = ('dog', 'paw', 'shake', 'trick', 'training', 'sitting', 'pet')

    def build(self):
        """Open the bent paw recess while retaining the raised paw gesture."""

        def line(n, a, b):
            self.add_line(n, a, b)

        def arc(n, a, b, rx, ry=None, sweep=True):
            self.add_arc(n, a, b, radius_x=rx, radius_y=ry or rx, sweep=sweep)

        def contour(n, *parts, closed=False):
            self.add_contour(n, *parts, closed=closed)
        self.add_polyline('head', (24, 20), (24, 6), (18, 14), (10, 18), (10, 24), (18, 24), (18, 34), (6, 28), (6, 34), (20, 40))
        arc('haunch', (20, 40), (38, 28), 18, 12, False)
        line('back', (38, 28), (24, 20))
        self.relate('connect', 'head', 'haunch')
        self.relate('connect', 'haunch', 'back')
        self.relate('connect', 'back', 'head')
        arc('tail', (38, 28), (42, 16), 4, 12, False)
        self.relate('connect', 'tail', 'haunch')
        self.relate('connect', 'tail', 'back')
        line('base', (20, 40), (20, 42))
        self.relate('connect', 'base', 'head')
        self.relate('connect', 'base', 'haunch')

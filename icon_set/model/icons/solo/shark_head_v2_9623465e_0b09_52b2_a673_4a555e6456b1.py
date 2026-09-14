"""Square envelope; opened the forehead and lower-jaw band around the solid eye and retained the wedge snout.

SQUARE: visible ink (4, 4, 44, 44). Square envelope preserves the subject’s near-equal overall width and height.
No useful exact local Lucide match; retained the inspected parent silhouette.
"""
# Independent revision; parent models preserved.
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9623465e-0b09-52b2-a673-4a555e6456b1'
SOURCE_PATH = 'pictographic-primitives/animals/tiger shark_9623465e-0b09-52b2-a673-4a555e6456b1.svg'
AUTHOR = 'gpt-6'

class SharkHeadVariant2(Solo48):
    icon_id = 'shark-head-v2'
    variant_of = 'shark-head'
    variant_label = 'Exact keyshape envelope and clear spacing'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/animals'
    aliases = ()
    keywords = ('shark', 'head', 'jaw', 'teeth', 'fish', 'sea', 'predator', 'bite')

    def build(self) -> None:
        self.add_line('rear-1', (6, 6), (14, 13))
        self.add_line('rear-2', (14, 13), (28, 10))
        self.add_arc('snout-top', (28, 10), (42, 25), radius_x=30)
        self.add_arc('snout-bottom', (42, 25), (40, 31), radius_x=10)
        self.add_line('mouth-top', (40, 31), (24, 30))
        self.add_line('jaw-1', (24, 30), (32, 40))
        self.add_line('jaw-2', (32, 40), (14, 40))
        self.add_line('jaw-3', (14, 40), (6, 42))
        self.add_contour('profile', 'rear-1', 'rear-2', 'snout-top', 'snout-bottom', 'mouth-top', 'jaw-1', 'jaw-2', 'jaw-3')
        self.add_line('gill', (10, 23), (10, 29))
        self.add_dot('eye', (28, 22))

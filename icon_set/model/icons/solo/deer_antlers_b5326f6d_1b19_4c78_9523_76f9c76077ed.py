"""Mirrored deer antlers with three outward tines on each curved beam. No useful local Lucide antler match; paired radii maintain balance."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b5326f6d-1b19-4c78-9523-76f9c76077ed'
SOURCE_PATH = 'pictographic-primitives/animals/deer antlers_b5326f6d-1b19-4c78-9523-76f9c76077ed.svg'
AUTHOR = 'gpt-6'


class DeerAntlers(Solo48):
    icon_id = 'deer-antlers'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ()
    keywords = ('antlers', 'deer', 'horns', 'stag', 'hunting', 'wildlife', 'rack', 'nature')

    def build(self) -> None:
        # Visible bounds: (0, 0, 48, 48); centerline inset 2.
        self.add_line('left-base', (20, 46), (20, 39))
        self.add_arc('left-beam-low', (20, 39), (12, 24), radius_x=18, radius_y=18, sweep=False)
        self.add_arc('left-beam-high', (12, 24), (7, 10), radius_x=22, radius_y=22, sweep=False)
        self.add_line('left-tip', (7, 10), (7, 2))
        self.add_contour('left-beam', 'left-base', 'left-beam-low', 'left-beam-high', 'left-tip', closed=False)
        self.add_arc('left-upper-tine', (7, 10), (2, 7), radius_x=5, radius_y=3, sweep=True)
        self.relate("connect", 'left-upper-tine', 'left-beam')
        self.add_arc('left-middle-tine', (12, 24), (2, 20), radius_x=10, radius_y=4, sweep=True)
        self.relate("connect", 'left-middle-tine', 'left-beam')
        self.add_line('left-lower-tine', (20, 39), (11, 34))
        self.relate("connect", 'left-lower-tine', 'left-beam')
        self.add_line('right-base', (28, 46), (28, 39))
        self.add_arc('right-beam-low', (28, 39), (36, 24), radius_x=18, radius_y=18, sweep=True)
        self.add_arc('right-beam-high', (36, 24), (41, 10), radius_x=22, radius_y=22, sweep=True)
        self.add_line('right-tip', (41, 10), (41, 2))
        self.add_contour('right-beam', 'right-base', 'right-beam-low', 'right-beam-high', 'right-tip', closed=False)
        self.add_arc('right-upper-tine', (41, 10), (46, 7), radius_x=5, radius_y=3, sweep=False)
        self.relate("connect", 'right-upper-tine', 'right-beam')
        self.add_arc('right-middle-tine', (36, 24), (46, 20), radius_x=10, radius_y=4, sweep=False)
        self.relate("connect", 'right-middle-tine', 'right-beam')
        self.add_line('right-lower-tine', (28, 39), (37, 34))
        self.relate("connect", 'right-lower-tine', 'right-beam')

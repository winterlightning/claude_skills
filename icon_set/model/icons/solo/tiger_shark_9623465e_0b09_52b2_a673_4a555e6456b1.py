"""A shark head in right-facing profile with a wedge snout and open jaw."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9623465e-0b09-52b2-a673-4a555e6456b1'
SOURCE_PATH = 'pictographic-primitives/animals/tiger shark_9623465e-0b09-52b2-a673-4a555e6456b1.svg'
AUTHOR = 'gpt-6'


class SharkHead(Solo48):
    icon_id = 'shark-head'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('shark', 'head', 'jaw', 'teeth', 'fish', 'sea', 'predator', 'bite')

    def build(self) -> None:
        # Visible keyshape extremes: (0, 3, 48, 45).
        self.add_line('rear-1', (2, 5), (14, 13))
        self.add_line('rear-2', (14, 13), (28, 15))
        self.add_arc("snout-top", (28,15), (46,25), radius_x=30)
        self.add_arc("snout-bottom", (46,25), (40,31), radius_x=10)
        self.add_line("mouth-top", (40,31), (24,28))
        self.add_line('jaw-1', (24, 28), (32, 36))
        self.add_line('jaw-2', (32, 36), (14, 39))
        self.add_line('jaw-3', (14, 39), (2, 43))
        self.add_contour("profile", "rear-1", "rear-2", "snout-top", "snout-bottom", "mouth-top", "jaw-1", "jaw-2", "jaw-3")
        self.add_line("gill", (10,23), (10,29))
        self.add_line("eye", (29,22), (31,22))

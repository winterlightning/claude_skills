# Review revision; previous candidates preserved.
"""Paw print with enlarged circular toes and rounded mirrored central pad. Lucide paw-print informs coherent round lobes."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3a1bcec0-4f4d-5256-8275-cc56ec3fa7d1'
SOURCE_PATH = 'pictographic-primitives/animals/animal print paw_3a1bcec0-4f4d-5256-8275-cc56ec3fa7d1.svg'
AUTHOR = 'gpt-6'

class PawPrint(Solo48):
    icon_id = 'paw-print'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/animals'
    aliases = ()
    keywords = ('paw', 'print', 'track', 'footprint', 'animal', 'pet', 'dog', 'cat', 'wildlife')

    def build(self) -> None:
        for name, cx, cy, radius in (('inner-left', 15, 10, 4), ('inner-right', 33, 10, 4), ('outer-left', 9, 24, 3), ('outer-right', 39, 24, 3)):
            self.add_arc(name + '-top', (cx - radius, cy), (cx + radius, cy), radius_x=radius)
            self.add_arc(name + '-bottom', (cx + radius, cy), (cx - radius, cy), radius_x=radius)
            self.add_contour(name, name + '-top', name + '-bottom', closed=True)
        self.add_arc('pad-crown', (16, 38), (32, 38), radius_x=8, radius_y=10)
        self.add_arc('pad-right', (32, 38), (28, 42), radius_x=4)
        self.add_arc('pad-notch-right', (28, 42), (24, 42), radius_x=6, sweep=False)
        self.add_arc('pad-notch-left', (24, 42), (20, 42), radius_x=6, sweep=False)
        self.add_arc('pad-left', (20, 42), (16, 38), radius_x=4)
        self.add_contour('pad', 'pad-crown', 'pad-right', 'pad-notch-right', 'pad-notch-left', 'pad-left', closed=True)

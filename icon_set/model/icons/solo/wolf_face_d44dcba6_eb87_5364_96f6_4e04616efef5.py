"""Raised the chin and nose together, retaining pointed ears and paired cheeks.

Keyshape SQUARE: visible bounds (4, 4, 44, 44).
Reference: No useful exact match.
"""
# Independent repair of wolf-face; parent preserved.
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd44dcba6-eb87-5364-96f6-4e04616efef5'
SOURCE_PATH = 'pictographic-primitives/animals/wolf_d44dcba6-eb87-5364-96f6-4e04616efef5.svg'
AUTHOR = 'gpt-6'

class WolfFace(Solo48):
    icon_id = 'wolf-face'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    categories = ('animals', 'primitives')
    aliases = ('wolf-head',)
    keywords = ('wolf', 'face', 'head', 'ears', 'front', 'muzzle', 'canine', 'wild')

    # Symbol plan: retain the subject and shared attachment stations;
    # fit the current keyshape by adjusting the owning cap, base or repeat.
    def build(self):
        points = [(6, 28), (7, 18), (6, 6), (16, 10), (32, 10), (42, 6), (41, 18), (42, 28), (30, 40)]
        for j, (a, b) in enumerate(zip(points, points[1:]), 1):
            self.add_line(f'upper-head-{j}', a, b)
        self.add_arc('chin', (30, 40), (18, 40), radius_x=10, radius_y=10, sweep=True)
        self.add_line('left-jaw', (18, 40), (6, 28))
        self.add_contour('head', *[f'upper-head-{i}' for i in range(1, 9)], 'chin', 'left-jaw', closed=True)
        self.add_dot('nose', (24,30))

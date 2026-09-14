"""A mirrored wolf face with pointed ears, flared cheeks and a rounded nose."""
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
    category = 'objects/animals'
    aliases = ('wolf-head',)
    keywords = ('wolf', 'face', 'head', 'ears', 'front', 'muzzle', 'canine', 'wild')

    def build(self):
        # SQUARE centerline extremes: (6,6)-(42,42). Mirror about x=24.
        points = [(6,28), (7,18), (6,6), (16,10), (32,10), (42,6), (41,18), (42,28), (30,42)]
        for j, (a,b) in enumerate(zip(points, points[1:]), 1):
            self.add_line(f'upper-head-{j}', a, b)
        self.add_arc('chin', (30,42), (18,42), radius_x=10, radius_y=10, sweep=True)
        self.add_line('left-jaw', (18,42), (6,28))
        self.add_contour('head', *[f'upper-head-{i}' for i in range(6,9)], 'chin', 'left-jaw', closed=True)
        self.add_arc('nose-top', (21,32), (27,32), radius_x=3, sweep=True)
        self.add_arc('nose-bottom', (27,32), (21,32), radius_x=3, sweep=True)
        self.add_contour('nose', 'nose-top', 'nose-bottom', closed=True)

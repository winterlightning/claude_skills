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
        # SQUARE centerline extremes: (2,2)-(46,46). Mirror about x=24.
        points = [(2,28), (7,18), (4,2), (16,10), (32,10), (44,2), (41,18), (46,28), (30,44)]
        for j, (a,b) in enumerate(zip(points, points[1:]), 1):
            self.add_line(f'upper-head-{j}', a, b)
        self.add_arc('chin', (30,44), (18,44), radius_x=10, radius_y=10, sweep=True)
        self.add_line('left-jaw', (18,44), (2,28))
        self.add_contour('head', *[f'upper-head-{i}' for i in range(1,9)], 'chin', 'left-jaw', closed=True)
        self.add_arc('nose-top', (21,32), (27,32), radius_x=3, sweep=True)
        self.add_arc('nose-bottom', (27,32), (21,32), radius_x=3, sweep=True)
        self.add_contour('nose', 'nose-top', 'nose-bottom', closed=True)

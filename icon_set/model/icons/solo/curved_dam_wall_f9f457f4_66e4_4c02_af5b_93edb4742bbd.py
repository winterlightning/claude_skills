"""A notched dam wall with flared sides, water edge and two flow streaks."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f9f457f4-66e4-4c02-af5b-93edb4742bbd'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-07/water dam_f9f457f4-66e4-4c02-af5b-93edb4742bbd.svg'
AUTHOR = 'gpt-6'

class CurvedDamWall(Solo48):
    icon_id = 'curved-dam-wall'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/landmarks'
    aliases = ()
    keywords = ('dam', 'wall', 'water', 'reservoir', 'barrier', 'spillway', 'infrastructure', 'river')

    def build(self) -> None:
        # HRECT_XL centerline extremes (2,5)-(46,43).
        wall = [(2, 40), (5, 15), (5, 5), (13, 5), (13, 13), (35, 13), (35, 5), (43, 5), (43, 15), (46, 40)]
        for j, (a, b) in enumerate(zip(wall, wall[1:]), 1):
            self.add_line(f'wall-{j}', a, b)
        self.add_arc('water-right', (46, 40), (24, 40), radius_x=11, radius_y=3, sweep=True)
        self.add_arc('water-left', (24, 40), (2, 40), radius_x=11, radius_y=3, sweep=True)
        self.add_contour('outline', *[f'wall-{i}' for i in range(1,10)], 'water-right', 'water-left', closed=True)
        self.add_line('flow-left', (19, 23), (17, 31))
        self.add_line('flow-right', (31, 23), (29, 31))

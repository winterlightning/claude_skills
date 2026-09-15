"""A notched dam wall with flared sides, water edge and two flow streaks."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f9f457f4-66e4-4c02-af5b-93edb4742bbd'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-07/water dam_f9f457f4-66e4-4c02-af5b-93edb4742bbd.svg'
AUTHOR = 'gpt-6'

class CurvedDamWall(Solo48):
    icon_id = 'curved-dam-wall'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/landmarks'
    aliases = ()
    keywords = ('dam', 'wall', 'water', 'reservoir', 'barrier', 'spillway', 'infrastructure', 'river')

    def build(self):
        # Shared 10-unit wall thickness and one elliptical lower water edge; paired flow marks. No useful Lucide dam match.
        self.add_line('wall-1', (4, 32), (4, 8))
        self.add_line('wall-2', (4, 8), (14, 8))
        self.add_line('wall-3', (14, 8), (14, 16))
        self.add_line('wall-4', (14, 16), (34, 16))
        self.add_line('wall-5', (34, 16), (34, 8))
        self.add_line('wall-6', (34, 8), (44, 8))
        self.add_line('wall-7', (44, 8), (44, 32))
        self.add_arc('water', (44, 32), (4, 32), radius_x=20, radius_y=8, sweep=True)
        self.add_contour('outline', 'wall-1', 'wall-2', 'wall-3', 'wall-4', 'wall-5', 'wall-6', 'wall-7', 'water', closed=True)
        self.add_line('flow-left', (18, 25), (16, 31))
        self.add_line('flow-right', (32, 25), (30, 31))

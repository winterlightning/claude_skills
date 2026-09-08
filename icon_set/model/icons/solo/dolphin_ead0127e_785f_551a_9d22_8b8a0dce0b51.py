"""jumping-dolphin: reconstructed at native SOLO48 size."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ead0127e-785f-551a-9d22-8b8a0dce0b51'
SOURCE_PATH = 'pictographic-primitives/animals/dolphin_ead0127e-785f-551a-9d22-8b8a0dce0b51.svg'
AUTHOR = 'gpt-6'


class JumpingDolphin(Solo48):
    icon_id = 'jumping-dolphin'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ()
    keywords = ('dolphin', 'jump', 'sea', 'ocean', 'marine', 'mammal', 'arc', 'swim')

    def build(self):
        self.add_line('silhouette-1', (2, 24), (6, 17))
        self.add_arc('silhouette-2', (6, 17), (22, 7), radius_x=19, radius_y=19, sweep=True)
        self.add_line('silhouette-3', (22, 7), (30, 5))
        self.add_line('silhouette-4', (30, 5), (28, 12))
        self.add_arc('silhouette-5', (28, 12), (40, 32), radius_x=24, radius_y=24, sweep=True)
        self.add_arc('silhouette-6', (40, 32), (46, 43), radius_x=6, radius_y=11, sweep=True)
        self.add_line('silhouette-7', (46, 43), (36, 39))
        self.add_line('silhouette-8', (36, 39), (27, 43))
        self.add_arc('silhouette-9', (27, 43), (31, 33), radius_x=12, radius_y=12, sweep=True)
        self.add_arc('silhouette-10', (31, 33), (18, 23), radius_x=15, radius_y=15, sweep=False)
        self.add_line('silhouette-11', (18, 23), (20, 32))
        self.add_arc('silhouette-12', (20, 32), (12, 27), radius_x=10, radius_y=10, sweep=True)
        self.add_line('silhouette-13', (12, 27), (2, 30))
        self.add_line('silhouette-14', (2, 30), (2, 24))
        self.add_contour('silhouette', 'silhouette-1', 'silhouette-2', 'silhouette-3', 'silhouette-4', 'silhouette-5', 'silhouette-6', 'silhouette-7', 'silhouette-8', 'silhouette-9', 'silhouette-10', 'silhouette-11', 'silhouette-12', 'silhouette-13', 'silhouette-14', closed=True)

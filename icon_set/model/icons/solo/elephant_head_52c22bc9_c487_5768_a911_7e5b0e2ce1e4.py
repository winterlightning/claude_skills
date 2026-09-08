"""Connected elephant head profile with a broad ear, visible eye, lower jaw and curled trunk."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '52c22bc9-c487-5768-a911-7e5b0e2ce1e4'
SOURCE_PATH = 'pictographic-primitives/animals/elephant head_52c22bc9-c487-5768-a911-7e5b0e2ce1e4.svg'
AUTHOR = 'gpt-6'


class MinimalElephantHead(Solo48):
    icon_id = 'minimal-elephant-head'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/animals"
    aliases = ()
    keywords = ('minimal', 'elephant', 'head')

    def build(self) -> None:
        # SQUARE ink bounds (0, 0, 48, 48), centerline extremes 2 and 46.
        self.add_arc('crown', (2, 16), (38, 16), radius_x=18, radius_y=14, sweep=True)
        self.add_line('forehead', (38, 16), (38, 32))
        self.add_arc('trunk-tip-inner', (38, 32), (46, 32), radius_x=4, sweep=False)
        self.add_line('trunk-tip', (46, 32), (46, 38))
        self.add_arc('trunk-outer', (46, 38), (30, 38), radius_x=8, sweep=True)
        self.add_line('trunk-inner', (30, 38), (30, 30))
        self.add_line('jaw', (30, 30), (12, 32))
        self.add_arc('ear-outline', (12, 32), (2, 16), radius_x=10, radius_y=16, sweep=True)
        self.add_contour('silhouette', 'crown', 'forehead', 'trunk-tip-inner', 'trunk-tip', 'trunk-outer', 'trunk-inner', 'jaw', 'ear-outline', closed=True)
        self.add_line('ear-fold', (18, 11), (18, 18))
        self.add_arc('ear-round', (18, 18), (12, 24), radius_x=6, sweep=True)
        self.add_contour('ear-detail', 'ear-fold', 'ear-round')
        self.add_dot('eye', (28, 17))

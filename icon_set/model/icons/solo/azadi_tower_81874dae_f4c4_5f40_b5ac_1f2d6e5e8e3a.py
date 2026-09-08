"""Azadi Tower: a flat crown, flaring legs and a pointed central arch. Secondary arch omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '81874dae-f4c4-5f40-b5ac-1f2d6e5e8e3a'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-02/azadi tower iran_81874dae-f4c4-5f40-b5ac-1f2d6e5e8e3a.svg'
AUTHOR = 'gpt-6'


class AzadiTower(Solo48):
    icon_id = 'azadi-tower'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "places/landmarks"
    aliases = ()
    keywords = ('azadi', 'tower', 'iran', 'tehran', 'monument', 'arch', 'landmark', 'gate', 'architecture')

    def build(self) -> None:
        # Centerline extremes: (2,8)-(46,40); mirrored around x=24.
        self.add_line('crown', (17,8), (31,8))
        self.add_arc('right-flare', (31,8), (46,40), radius_x=15, radius_y=32, sweep=False)
        self.add_line('right-foot', (46,40), (33,40))
        self.add_arc('right-opening', (33,40), (24,19), radius_x=27, radius_y=27, sweep=False)
        self.add_arc('left-opening', (24,19), (15,40), radius_x=27, radius_y=27, sweep=False)
        self.add_line('left-foot', (15,40), (2,40))
        self.add_arc('left-flare', (2,40), (17,8), radius_x=15, radius_y=32, sweep=False)
        self.add_contour('monument', 'crown', 'right-flare', 'right-foot', 'right-opening', 'left-opening', 'left-foot', 'left-flare', closed=True)

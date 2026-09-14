# Review candidate; original preserved.
"""Capped Berlin wall with right-facing painted head. Centerline extremes (6,6)-(42,42). Deliberate profile asymmetry; tiny mouth notch omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c05f1690-f04d-460c-a834-2bdbd5877990'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-04/east side gallery berlin wall_c05f1690-f04d-460c-a834-2bdbd5877990.svg'
AUTHOR = 'gpt-6'

class PaintedWallMuralPanel(Solo48):
    icon_id = 'painted-wall-mural-panel'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/landmarks'
    aliases = ()
    keywords = ('berlin wall', 'east side gallery', 'mural', 'graffiti', 'wall', 'art', 'landmark', 'panel', 'face')

    def build(self) -> None:
        """Opening repair: Replaced the thin hollow coping band with one solid cap stroke; retained the mural."""
        self.add_polyline('cap', (8, 4), (10, 4), (38, 4), (40, 4), closed=False)
        self.add_polyline('panel', (10, 4), (10, 44), (38, 44), (38, 4), closed=False)
        self.add_arc('head', (18, 26), (30, 22), radius_x=8, radius_y=7, sweep=True)
        self.add_polyline('face', (30, 22), (32, 28), (26, 31), (26, 38), (18, 38), (18, 26), closed=False)
        self.relate('connect', 'cap', 'panel')
        self.relate('connect', 'head', 'face')

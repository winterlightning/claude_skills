"""Capped Berlin wall with right-facing painted head. Centerline extremes (5,2)-(43,46). Deliberate profile asymmetry; tiny mouth notch omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c05f1690-f04d-460c-a834-2bdbd5877990'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-04/east side gallery berlin wall_c05f1690-f04d-460c-a834-2bdbd5877990.svg'
AUTHOR = 'gpt-6'

class PaintedWallMuralPanel(Solo48):
    icon_id = 'painted-wall-mural-panel'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/landmarks"
    aliases = ()
    keywords = ('berlin wall', 'east side gallery', 'mural', 'graffiti', 'wall', 'art', 'landmark', 'panel', 'face')

    def build(self) -> None:
        self.add_polyline('cap', (5, 2), (43, 2), (43, 9), (38, 9), (10, 9), (5, 9), closed=True)
        self.add_polyline('panel', (10, 9), (10, 46), (38, 46), (38, 9), closed=False)
        self.add_arc('head', (18, 26), (30, 22), radius_x=8, radius_y=7, sweep=True)
        self.add_polyline('face', (30, 22), (32, 28), (26, 31), (26, 38), (18, 38), (18, 26), closed=False)
        self.relate("connect", 'cap', 'panel')
        self.relate("connect", 'head', 'face')

# Variant of painted-wall-mural-panel; parent file remains unchanged.
"""Wider capped Berlin wall with a rectangular mural. Centerline extremes (2,2)-(46,46)."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c05f1690-f04d-460c-a834-2bdbd5877990'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-04/east side gallery berlin wall_c05f1690-f04d-460c-a834-2bdbd5877990.svg'
AUTHOR = 'gpt-6'

class PaintedWallMuralPanelVariant2(Solo48):
    icon_id = 'painted-wall-mural-panel-v2'
    variant_of = 'painted-wall-mural-panel'
    variant_label = 'Wider wall with rectangular mural'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/landmarks'
    aliases = ()
    keywords = ('berlin wall', 'east side gallery', 'mural', 'graffiti', 'wall', 'art', 'landmark', 'panel', 'face')

    def build(self) -> None:
        self.add_polyline('cap', (2, 2), (46, 2), (46, 9), (41, 9), (7, 9), (2, 9), closed=True)
        self.add_polyline('panel', (7, 9), (7, 46), (41, 46), (41, 9), closed=False)
        self.add_polyline('mural', (18, 20), (30, 20), (30, 38), (18, 38), closed=True)
        self.relate('connect', 'cap', 'panel')

# Review candidate; original preserved.
"""Wider capped Berlin wall with a rectangular mural. Centerline extremes (6,6)-(42,42)."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c05f1690-f04d-460c-a834-2bdbd5877990'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-04/east side gallery berlin wall_c05f1690-f04d-460c-a834-2bdbd5877990.svg'
AUTHOR = 'gpt-6'

class PaintedWallMuralPanelVariant5(Solo48):
    icon_id = 'painted-wall-mural-panel-v5'
    variant_of = 'painted-wall-mural-panel-v2'
    variant_label = 'Roomier openings — pending review'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/landmarks'
    aliases = ()
    keywords = ('berlin wall', 'east side gallery', 'mural', 'graffiti', 'wall', 'art', 'landmark', 'panel', 'face')

    def build(self) -> None:
        """Opening repair: Replaced the thin hollow coping band with one solid cap stroke; retained the mural."""
        self.add_polyline('cap', (6, 6), (7, 6), (41, 6), (42, 6), closed=False)
        self.add_polyline('panel', (7, 6), (7, 42), (41, 42), (41, 6), closed=False)
        self.add_polyline('mural', (18, 20), (30, 20), (30, 38), (18, 38), closed=True)
        self.relate('connect', 'cap', 'panel')

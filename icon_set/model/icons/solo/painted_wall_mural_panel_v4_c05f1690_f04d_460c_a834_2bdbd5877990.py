# Variant of painted-wall-mural-panel-v2; parent file remains unchanged.
'Painted wall mural panel v2: independent spacing revision.\n\nDeepen wall cap and raise mural off the bottom boundary.\nNative solo family, SQUARE keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: Original subject render; no exact Lucide match selected.\n'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c05f1690-f04d-460c-a834-2bdbd5877990'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-04/east side gallery berlin wall_c05f1690-f04d-460c-a834-2bdbd5877990.svg'
AUTHOR = 'gpt-6'

class PaintedWallMuralPanelVariant4(Solo48):
    icon_id = 'painted-wall-mural-panel-v4'
    variant_of = 'painted-wall-mural-panel-v2'
    variant_label = 'Roomier spacing — remaining review'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/landmarks'
    aliases = ()
    keywords = ('berlin wall', 'east side gallery', 'mural', 'graffiti', 'wall', 'art', 'landmark', 'panel', 'face')

    def build(self):
        self.add_polyline('cap',(6, 6),(42, 6),(42, 14),(6, 14),closed=True)
        self.add_polyline('panel',(6, 14),(6, 42),(42, 42),(42, 14),closed=False)
        self.relate('connect','cap','panel')
        self.add_polyline('mural',(16, 22),(32, 22),(32, 34),(16, 34),closed=True)

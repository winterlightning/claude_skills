# Variant of painted-wall-mural-panel; parent file remains unchanged.
'Painted wall mural panel: independent spacing revision.\n\nEight-unit wall cap and a simpler open profile with clear margins.\nNative solo family, VRECT_L keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: Original subject render; no exact Lucide match selected.\n'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c05f1690-f04d-460c-a834-2bdbd5877990'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-04/east side gallery berlin wall_c05f1690-f04d-460c-a834-2bdbd5877990.svg'
AUTHOR = 'gpt-6'

class PaintedWallMuralPanelVariant3(Solo48):
    icon_id = 'painted-wall-mural-panel-v3'
    variant_of = 'painted-wall-mural-panel'
    variant_label = 'Roomier spacing — remaining review'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/landmarks'
    aliases = ()
    keywords = ('berlin wall', 'east side gallery', 'mural', 'graffiti', 'wall', 'art', 'landmark', 'panel', 'face')

    def build(self):
        self.add_polyline('cap',(8, 4),(40, 4),(40, 12),(8, 12),closed=True)
        self.add_polyline('panel',(8, 12),(8, 44),(40, 44),(40, 12),closed=False)
        self.relate('connect','cap','panel')
        self.add_line('head-left',(18, 35),(18, 28))
        self.add_arc('crown',(18, 28),(30, 28),radius_x=6,radius_y=6,sweep=True)
        self.add_polyline('profile',(30, 28),(30, 30),(26, 32),(26, 35),closed=False)
        self.contours = [c for c in self.contours if c.contour_id != 'profile']
        self.add_contour('mural','head-left','crown','profile-1','profile-2','profile-3',closed=False)

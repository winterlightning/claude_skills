'Suspended succulent planter: independent spacing revision.\n\nOne broad succulent leaf replaces the crowded three-point crown; deeper hanging bowl.\nNative solo family, VRECT_L keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: sprout: broad leaf silhouettes around a central stem. Local Lucide originals and atomic-debug renders were inspected.\n'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5cbfa835-9e2f-4167-8646-e8f8c56bf395'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-02/hanging plant 2_5cbfa835-9e2f-4167-8646-e8f8c56bf395.svg'
AUTHOR = 'gpt-6'

class SuspendedSucculentPlanter(Solo48):
    icon_id = 'suspended-succulent-planter'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/decoration'
    aliases = ()
    keywords = ('planter', 'hanging', 'succulent', 'leaves', 'cord', 'bowl', 'plant')

    def build(self):
        self.add_polyline('suspension',(8, 32),(8, 24),(24, 4),(40, 24),(40, 32),closed=False)
        self.add_polyline('rim',(8, 32),(16, 32),(32, 32),(40, 32),closed=False)
        self.add_arc('bowl',(40, 32),(8, 32),radius_x=16,radius_y=12,sweep=True)
        self.contours = [c for c in self.contours if c.contour_id != 'rim']
        self.add_contour('pot','rim-1','rim-2','rim-3','bowl',closed=True)
        self.add_polyline('leaf',(16, 32),(16, 26),(24, 18),(32, 26),(32, 32),closed=False)
        self.relate('connect','suspension','pot')
        self.relate('connect','leaf','pot')

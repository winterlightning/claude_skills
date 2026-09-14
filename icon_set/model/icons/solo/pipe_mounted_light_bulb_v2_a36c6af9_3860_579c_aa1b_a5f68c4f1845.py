# Variant of pipe-mounted-light-bulb; parent file remains unchanged.
'Pipe mounted light bulb: independent spacing revision.\n\nRemove crowded filament and tiny lower bend; use one broad bent pipe and foot.\nNative solo family, VRECT_L keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: Original subject render; no exact Lucide match selected.\n'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a36c6af9-3860-579c-aa1b-a5f68c4f1845'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-04/steampunk decoration lamp_a36c6af9-3860-579c-aa1b-a5f68c4f1845.svg'
AUTHOR = 'gpt-6'

class PipeMountedLightBulbVariant2(Solo48):
    icon_id = 'pipe-mounted-light-bulb-v2'
    variant_of = 'pipe-mounted-light-bulb'
    variant_label = 'Roomier spacing — remaining review'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/decoration'
    aliases = ()
    keywords = ('lamp', 'bulb', 'pipe', 'light', 'filament', 'steampunk', 'fixture')

    def build(self):
        self.add_arc('dome',(16, 16),(40, 16),radius_x=12,radius_y=12,sweep=True)
        self.add_arc('shoulder-right',(40, 16),(34, 26),radius_x=15,radius_y=15,sweep=True)
        self.add_polyline('socket',(34, 26),(34, 32),(28, 32),(22, 32),(22, 26),closed=False)
        self.add_arc('shoulder-left',(22, 26),(16, 16),radius_x=15,radius_y=15,sweep=True)
        self.contours = [c for c in self.contours if c.contour_id != 'socket']
        self.add_contour('bulb','dome','shoulder-right','socket-1','socket-2','socket-3','socket-4','shoulder-left',closed=True)
        self.add_polyline('pipe',(28, 32),(28, 44),(8, 44),closed=False)
        self.relate('connect','bulb','pipe')

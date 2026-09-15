'Printer 3d cone: independent spacing revision.\n\nRaise nozzle and center printed cone with eight-unit frame clearance.\nNative solo family, SQUARE keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: Original subject render; no exact Lucide match selected.\n'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'dd8e0bad-9fc5-427b-bf73-b63a99a3bc98'
SOURCE_PATH = 'pictographic-primitives/technology/3 d print triangle_dd8e0bad-9fc5-427b-bf73-b63a99a3bc98.svg'
AUTHOR = 'gpt-6'

class Printer3DCone(Solo48):
    icon_id = 'printer-3d-cone'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/technology'
    aliases = ()
    keywords = ('3d-printing', 'printer', 'cone', 'nozzle', 'fabrication', 'maker', 'model')

    def build(self):
        self.add_polyline('frame',(6, 6),(16, 6),(42, 6),(42, 42),(34, 42),(14, 42),(6, 42),closed=True)
        self.add_polyline('feed',(16, 6),(16, 16),(24, 16),(24, 18),closed=False)
        self.add_polyline('print',(14, 42),(14, 36),(24, 28),(34, 36),(34, 42),closed=False)
        self.relate('connect','frame','feed')
        self.relate('connect','frame','print')

'Pentagon with star: independent spacing revision.\n\nRemove stripe and rebalance the five-point star inside the pentagon.\nNative solo family, SQUARE keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: Original subject render; no exact Lucide match selected.\n'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '901869c8-bdce-553a-afb2-859aca2f3363'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-04/pentagon usa_901869c8-bdce-553a-afb2-859aca2f3363.svg'
AUTHOR = 'gpt-6'

class PentagonWithStar(Solo48):
    icon_id = 'pentagon-with-star'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/landmarks'
    aliases = ()
    keywords = ('pentagon', 'usa', 'defence', 'military', 'star', 'badge', 'government', 'emblem')

    def build(self):
        self.add_polyline('badge',(24, 6),(42, 18),(38, 42),(10, 42),(6, 18),closed=True)
        self.add_polyline('star',(24, 18),(27, 24),(32, 24),(28, 28),(30, 34),(24, 30),(18, 34),(20, 28),(16, 24),(21, 24),closed=True)

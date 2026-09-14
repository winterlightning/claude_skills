'Hunting rifle front sight: independent spacing revision.\n\nRebalanced geometry for eight-unit straight spacing and clear curved openings.\nNative solo family, HRECT_XL keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: Original subject render; no exact Lucide match selected.\n'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '75455c5e-9e1f-50fc-8a01-0407f3b0bdc6'
SOURCE_PATH = 'pictographic-primitives/war/modern weapon rifle_75455c5e-9e1f-50fc-8a01-0407f3b0bdc6.svg'
AUTHOR = 'gpt-6'

class HuntingRifleFrontSight(Solo48):
    icon_id = 'hunting-rifle-front-sight'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/war'
    aliases = ()
    keywords = ('rifle', 'hunting', 'stock', 'barrel', 'sight', 'trigger')

    def build(self):
        self.add_polyline('stock',(4, 40),(4, 28),(12, 24),(18, 18),(28, 18),(28, 28),(22, 28),(16, 34),(4, 40),closed=False)
        self.add_line('barrel',(28, 18),(44, 13))
        self.add_line('sight',(44, 13),(44, 8))
        self.relate('connect','stock','barrel')
        self.relate('connect','barrel','sight')

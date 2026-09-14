# Variant of washing-hands; parent file remains unchanged.
'Washing hands: independent spacing revision.\n\nOpen the thumb return and simplify the finger outline while preserving the washing gesture.\nNative solo family, HRECT_L keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: hand: clear finger returns and rounded joins. Local Lucide originals and atomic-debug renders were inspected.\n'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b49d7989-5d86-40cf-8c72-632e8858db04'
SOURCE_PATH = 'pictographic-primitives/wayfinding/washing hand_b49d7989-5d86-40cf-8c72-632e8858db04.svg'
AUTHOR = 'gpt-6'

class WashingHandsVariant2(Solo48):
    icon_id = 'washing-hands-v2'
    variant_of = 'washing-hands'
    variant_label = 'Roomier spacing — remaining review'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/wayfinding'
    aliases = ()
    keywords = ('hands', 'washing', 'soap', 'hygiene', 'cleaning', 'palms')

    def build(self):
        self.add_polyline('lower',(4, 32),(4, 24),(16, 16),(24, 24),(16, 30),(38, 30),(44, 34),(44, 40),(16, 40),(4, 32),closed=False)
        self.add_polyline('upper',(20, 8),(28, 8),(44, 20),closed=False)
        self.add_dot('water',(8, 8))

# Variant of star-labelled-bottle; parent file remains unchanged.
'Star labelled bottle: independent spacing revision.\n\nBroaden star points and keep eight-unit separation from straight bottle walls.\nNative solo family, VRECT_L keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: Original subject render; no exact Lucide match selected.\n'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e0f7f6c1-f633-5b90-9f71-aac0f4ec1dce'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-01/decoration bottle_e0f7f6c1-f633-5b90-9f71-aac0f4ec1dce.svg'
AUTHOR = 'gpt-6'

class StarLabelledBottleVariant3(Solo48):
    icon_id = 'star-labelled-bottle-v3'
    variant_of = 'star-labelled-bottle'
    variant_label = 'Roomier spacing — remaining review'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/decoration'
    aliases = ()
    keywords = ('bottle', 'star', 'cap', 'container', 'label', 'decor', 'vessel')

    def build(self):
        self.add_polyline('bottle',(16, 12),(16, 4),(32, 4),(32, 12),(40, 20),(40, 44),(8, 44),(8, 20),closed=True)
        self.add_polyline('star',(24, 18),(27, 24),(32, 24),(28, 28),(30, 34),(24, 30),(18, 34),(20, 28),(16, 24),(21, 24),closed=True)

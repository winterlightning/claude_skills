# Variant of hammerhead-shark-v2; parent file remains unchanged.
'Hammerhead shark v2: independent spacing revision.\n\nDeepen hammer bar; simplify gill, fins and swept tail to remove narrow returns.\nNative solo family, SQUARE keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: Original subject render; no exact Lucide match selected.\n'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'bdd1577c-6f14-5bee-a41f-fac2b80017a7'
SOURCE_PATH = 'pictographic-primitives/animals/shark hammer_bdd1577c-6f14-5bee-a41f-fac2b80017a7.svg'
AUTHOR = 'gpt-6'

class HammerheadSharkVariant4(Solo48):
    icon_id = 'hammerhead-shark-v4'
    variant_of = 'hammerhead-shark-v2'
    variant_label = 'Roomier spacing — remaining review'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals/marine'
    aliases = ()
    keywords = ('hammerhead', 'shark', 'head', 'fins', 'sea', 'ocean', 'fish', 'predator')

    def build(self):
        self.add_polyline('body',(6, 6),(42, 6),(42, 14),(32, 14),(32, 24),(40, 30),(32, 30),(32, 34),(40, 42),(24, 38),(16, 42),(20, 30),(8, 30),(16, 24),(16, 14),(6, 14),closed=True)

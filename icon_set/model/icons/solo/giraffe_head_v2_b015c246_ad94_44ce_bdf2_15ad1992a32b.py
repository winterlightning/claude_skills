# Variant of giraffe-head; parent file remains unchanged.
'Giraffe head: independent spacing revision.\n\nOpen ear, eight-unit ossicone, deeper muzzle and wider neck.\nNative solo family, SQUARE keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: Original subject render; no exact Lucide match selected.\n'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b015c246-ad94-44ce-bdf2-15ad1992a32b'
SOURCE_PATH = 'pictographic-primitives/animals/giraffe_b015c246-ad94-44ce-bdf2-15ad1992a32b.svg'
AUTHOR = 'gpt-6'

class GiraffeHeadVariant2(Solo48):
    icon_id = 'giraffe-head-v2'
    variant_of = 'giraffe-head'
    variant_label = 'Roomier spacing — remaining review'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ()
    keywords = ('giraffe', 'head', 'neck', 'ossicone', 'ear', 'profile', 'animal', 'safari')

    def build(self):
        self.add_polyline('outline',(6, 42),(16, 20),(20, 12),(20, 6),(28, 6),(28, 14),(42, 28),(42, 38),(26, 30),(18, 42),closed=False)
        self.add_polyline('ear',(16, 20),(6, 10),(6, 6),closed=False)
        self.relate('connect','outline','ear')

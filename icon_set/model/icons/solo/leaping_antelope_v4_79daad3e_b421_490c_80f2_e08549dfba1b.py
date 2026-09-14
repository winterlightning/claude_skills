# Variant of leaping-antelope-v2; parent file remains unchanged.
'Leaping antelope v2: independent spacing revision.\n\nOpen horn and foreleg, retaining the diagonal leaping body and widening the rear leg.\nNative solo family, SQUARE keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: Original subject render; no exact Lucide match selected.\n'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '79daad3e-b421-490c-80f2-e08549dfba1b'
SOURCE_PATH = 'pictographic-primitives/animals/deer jump_79daad3e-b421-490c-80f2-e08549dfba1b.svg'
AUTHOR = 'gpt-6'

class LeapingAntelopeVariant4(Solo48):
    icon_id = 'leaping-antelope-v4'
    variant_of = 'leaping-antelope-v2'
    variant_label = 'Roomier spacing — remaining review'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/animals'
    aliases = ()
    keywords = ('antelope', 'deer', 'leap', 'jump', 'running', 'gazelle', 'wildlife', 'motion')

    def build(self):
        self.add_polyline('body',(6, 42),(6, 32),(14, 26),(14, 20),(28, 14),(30, 6),(38, 6),(42, 14),(34, 20),(34, 26),(18, 36),(6, 42),closed=False)
        self.add_line('horn',(30, 6),(22, 6))
        self.add_line('foreleg',(34, 26),(42, 34))
        self.relate('connect','body','horn')
        self.relate('connect','body','foreleg')

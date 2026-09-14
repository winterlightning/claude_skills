# Variant of memory-module-with-notch; parent file remains unchanged.
'Memory module with notch: independent spacing revision.\n\nHorizontal module with two eight-unit chips and a broad edge notch.\nNative solo family, HRECT_L keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: Original subject render; no exact Lucide match selected.\n'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6f237c30-c7db-4dfc-91c5-5d21fb166711'
SOURCE_PATH = 'pictographic-primitives/computers/batch-05/computer ram_6f237c30-c7db-4dfc-91c5-5d21fb166711.svg'
AUTHOR = 'gpt-6'

class MemoryModuleWithNotchVariant2(Solo48):
    icon_id = 'memory-module-with-notch-v2'
    variant_of = 'memory-module-with-notch'
    variant_label = 'Roomier spacing — remaining review'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/device'
    aliases = ()
    keywords = ('ram', 'memory', 'module', 'dimm', 'chip', 'hardware', 'computer', 'upgrade')

    def build(self):
        self.add_polyline('board',(4, 8),(44, 8),(44, 40),(28, 40),(28, 32),(20, 32),(20, 40),(4, 40),closed=True)
        self.add_polyline('chip-left',(12, 16),(20, 16),(20, 24),(12, 24),closed=True)
        self.add_polyline('chip-right',(28, 16),(36, 16),(36, 24),(28, 24),closed=True)

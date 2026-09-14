"""An underlined capital K. VRECT_L extremes (8,6)-(40,42). No useful exact Lucide match; preserve the two diagonal arms and separate underline with open spacing."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '142e8cbc-226e-43cc-ba88-44eae89e8efa'
SOURCE_PATH = 'pictographic-primitives/symbol/k (text u)_142e8cbc-226e-43cc-ba88-44eae89e8efa.svg'
AUTHOR = 'gpt-6'

class KLetterUnderlinedVariant2(Solo48):
    icon_id = 'k-letter-underlined-v2'
    variant_of = 'k-letter-underlined'
    variant_label = 'Height envelope and full spacing repair'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/symbols'
    aliases = ()
    keywords = ('k', 'letter', 'text', 'underline', 'typography', 'alphabet', 'language')

    def build(self) -> None:
        self.add_polyline('stem', (12, 4), (12, 18), (12, 32))
        self.add_polyline('arms', (34, 4), (12, 18), (36, 32))
        self.relate('connect', 'stem', 'arms')
        self.add_line('underline', (8, 44), (40, 44))

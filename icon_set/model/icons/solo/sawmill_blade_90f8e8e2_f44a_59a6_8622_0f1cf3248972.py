'Sawmill blade: independent spacing revision.\n\nRebalanced geometry for eight-unit straight spacing and clear curved openings.\nNative solo family, SQUARE keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: Original subject render; no exact Lucide match selected.\n'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '90f8e8e2-f44a-59a6-8622-0f1cf3248972'
SOURCE_PATH = 'pictographic-primitives/tools/sawmill_90f8e8e2-f44a-59a6-8622-0f1cf3248972.svg'
AUTHOR = 'gpt-6'

class SawmillBlade(Solo48):
    icon_id = 'sawmill-blade'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/tools'
    aliases = ()
    keywords = ('sawmill', 'saw', 'blade', 'circular saw', 'cutting', 'lumber', 'wood', 'teeth')

    def build(self) -> None:
        self.add_polyline('blade', (6, 18), (12, 18), (10, 8), (18, 12), (24, 6), (28, 12), (36, 8), (36, 18), (42, 18), (38, 30), (42, 38), (30, 38), (28, 42), (20, 38), (12, 40), (10, 30), closed=True)
        self.add_dot('hub', (24, 22))

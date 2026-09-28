'Shanty village row: independent spacing revision.\n\nLevel the lower shed top to retain eight units above its base.\nNative solo family, SQUARE keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: Original subject render; no exact Lucide match selected.\n'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e5d1bebc-56b3-4fda-9bbf-e7de604c4fb4'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-06/shanty house village_e5d1bebc-56b3-4fda-9bbf-e7de604c4fb4.svg'
AUTHOR = 'gpt-6'

class ShantyVillageRow(Solo48):
    icon_id = 'shanty-village-row'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'places/landmarks'
    aliases = ()
    keywords = ('shanty', 'slum', 'village', 'houses', 'informal', 'settlement', 'shelter', 'housing')

    def build(self) -> None:
        self.add_polyline('rear-left', (6, 26), (6, 13), (12, 7), (22, 13), (22, 21))
        self.add_polyline('rear-right', (22, 13), (22, 8), (34, 6), (42, 8), (42, 23))
        self.relate('connect', 'rear-left', 'rear-right')
        self.add_polyline('shed', (18, 42), (18, 33), (31, 27), (42, 33), (42, 42), (18, 42), (6, 42), (6, 34), (18, 34))

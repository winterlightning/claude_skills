"""Growing money plant.
Plan: Rectangular banknote leaves at staggered levels join a slender stem and tapered pot. Extrema (8,4)-(40,44).
Reference: Lucide sprout: leaf junctions meeting a central stem; supplied banknotes replace leaf outlines.
Reduction: Tiny oval note marks and lower ordinary leaf omitted to preserve clear banknote leaves and pot.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '811d385a-460c-4a4e-9d97-0cef15611e99'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/finance/saving money seedling_811d385a-460c-4a4e-9d97-0cef15611e99.svg'
AUTHOR = 'gpt-6'

class Batch30Icon(Solo48):
    icon_id = 'potted-banknote-leaf-plant'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/finance"
    aliases = ()
    keywords = ('growing', 'money', 'plant')

    def build(self):

        self.add_polyline('note-left',(8,4),(20,4),(20,16),(8,16),(8,4))
        self.add_polyline('note-right',(28,12),(40,12),(40,24),(28,24),(28,12))
        self.add_polyline('branch',(20,16),(20,24),(28,24))
        self.relate('connect','note-left','branch');self.relate('connect','note-right','branch')
        self.add_line('stem',(28,24),(28,32));self.relate('connect','stem','branch');self.relate('connect','stem','note-right')
        self.add_polyline('pot',(10,32),(28,32),(38,32),(32,44),(16,44),(10,32));self.relate('connect','pot','stem')

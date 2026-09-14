"""Arrow (war), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bd4b75eb-f784-5321-93ca-96df4f0c0e41'
SOURCE_PATH = 'icons-json/war/arrow_bd4b75eb-f784-5321-93ca-96df4f0c0e41.json'
AUTHOR = 'json_to_solo'

class ArrowWar(Solo48):
    icon_id = 'arrow-war'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'war'
    aliases = ()
    keywords = ('arrow', 'war')

    def build(self):
        self.add_line('sym-e0', (8, 19), (24, 4))
        self.add_line('sym-e1', (24, 4), (40, 19))
        self.add_line('sym-e2', (24, 19), (24, 44))
        self.add_line('sym-e3', (24, 19), (40, 34))
        self.add_line('sym-e4', (24, 19), (8, 34))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e2')
        self.add_contour('sym-c2', 'sym-e3')
        self.add_contour('sym-c3', 'sym-e4')
        self.relate('connect', 'sym-c1', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c2')

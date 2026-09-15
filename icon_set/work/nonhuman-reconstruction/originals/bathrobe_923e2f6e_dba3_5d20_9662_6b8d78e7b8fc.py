"""Front-facing belted wrap robe. Square extremes 6,6–42,42. Mirrored sleeves; directional lapel. Lucide shirt informs garment outline; omit duplicate belt tails and front hem seam."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '923e2f6e-dba3-5d20-9662-6b8d78e7b8fc'
SOURCE_PATH = 'pictographic-primitives/spas/bathroom robe_923e2f6e-dba3-5d20-9662-6b8d78e7b8fc.svg'
AUTHOR = 'gpt-6'

class Bathrobe(Solo48):
    icon_id = 'bathrobe'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/wellness"
    aliases = ()
    keywords = ('spa', 'wellness', 'bathrobe')

    def build(self):
        self.add_polyline('robe', (16,6), (7,7), (6,23), (10,26), (14,16), (14,28), (10,42), (38,42), (34,28), (34,16), (38,26), (42,23), (41,7), (32,6), (16,6))
        self.add_polyline('lapel', (32,6), (20,28), (14,28))
        self.add_line('collar', (16,6), (23,16))
        self.add_line('belt', (20,28), (34,28))
        self.add_line('tie', (24,28), (24,37))
        self.relate('connect', 'robe', 'lapel')
        self.relate('connect', 'robe', 'collar')
        self.relate('connect', 'robe', 'belt')
        self.relate('connect', 'lapel', 'belt')
        self.relate('connect', 'belt', 'tie')

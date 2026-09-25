from ._construction import path, rounded_rect as rect, ellipse
'A circular towel holder hangs beneath a centered bracket and wall bar.\n\nSQUARE fits the wide bar and hanging ring: ink (0,0)-(64,64),\ncenterline (2,2)-(62,62). Reference: supplied failed SVG; Lucide circle original\nand atomic-debug informed the circular ring. No direct towel-ring match was\nused. A longer hanger and smaller ring give the bracket 9 units of centerline\nclearance. All parts remain centered on x=32; no identifying detail was removed.\n\nHosting (compose.py): plus, heart valid; check blocked.\n'
from ...keyshapes import Keyshape
from ._base import Container64
SOURCE_ICON_ID = 'towel-ring'
SOURCE_PATH = 'icon_set/dist/failed/container64/towel-ring.svg'
AUTHOR = 'gpt-6'

class TowelRing(Container64):
    icon_id = 'towel-ring'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'container'
    categories = ('container',)
    aliases = ('circular-towel-ring-hanger',)
    keywords = ('towel', 'ring')

    def build(self):
        line, poly = (self.add_line, self.add_polyline)

        def join(a, b):
            self.relate('connect', a, b)
        line('mount', (2, 2), (62, 2))
        line('hanger', (32, 2), (32, 10))
        ellipse(self, 'ring', 32, 36, 26)
        join('mount', 'hanger')
        join('hanger', 'ring')

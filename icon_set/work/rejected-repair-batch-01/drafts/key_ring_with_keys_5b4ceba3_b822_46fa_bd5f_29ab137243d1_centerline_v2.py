"""Add a clear tooth to the left key and shorten its lower stem; distinguish the hanging keys instead of leaving one as a bare line.
Independent centerline revision; original snapshot preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5b4ceba3-b822-46fa-bd5f-29ab137243d1'
SOURCE_PATH = 'pictographic-primitives/tools/tools keys_5b4ceba3-b822-46fa-bd5f-29ab137243d1.svg'
AUTHOR = 'gpt-6'

class KeyRingWithKeys(Solo48):
    icon_id = 'key-ring-with-keys-centerline-v2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/tools'
    aliases = ()
    keywords = ('keys', 'key ring', 'keychain', 'lock', 'access', 'unlock', 'bunch', 'tools')

    def build(self) -> None:

        def circle(n, x, y, r):
            self.add_arc(n + '-a', (x - r, y), (x + r, y), radius_x=r)
            self.add_arc(n + '-b', (x + r, y), (x - r, y), radius_x=r)
            self.add_contour(n, n + '-a', n + '-b', closed=True)
        circle('ring', 18, 18, 12)
        self.add_polyline('right-key', (30, 18), (42, 18), (42, 26))
        self.add_polyline('down-key', (18, 30), (18, 42), (26, 42))
        self.add_polyline('left-key', (6, 18), (6, 30), (6, 38), (10, 38))
        self.relate('connect', 'right-key', 'ring')
        self.relate('connect', 'down-key', 'ring')
        self.relate('connect', 'left-key', 'ring')
    variant_of = 'key-ring-with-keys'
    variant_label = 'Batch 01 centerline repair'

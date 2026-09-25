"""Angular folded bird with one broad wing, a pointed beak, and a triangular tail. Shared crease endpoints preserve the folded-paper topology; enlarge the beak interior."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '69eacfe0-29e8-4724-9178-908556367bd2'
SOURCE_PATH = 'pictographic-primitives/logos/snapcraft logo_69eacfe0-29e8-4724-9178-908556367bd2.svg'
AUTHOR = 'gpt-6'

class SnapcraftLogo(Solo48):
    icon_id = 'snapcraft-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('snapcraft', 'ubuntu', 'packages', 'bird', 'logo', 'brand', 'linux')

    def build(self):
        # Plan: Angular folded bird with one broad wing, a pointed beak, and a triangular tail. Shared crease endpoints preserve the folded-paper topology; enlarge the beak interior.
        # Exact keyshape ink extremes are owned by Keyshape.SQUARE on SOLO48.

        self.add_polyline('body',(6,6),(26,12),(38,12),(42,24),(34,22),(26,32),(16,19),closed=True)
        self.add_polyline('tail',(16,19),(8,42),(26,32))
        self.add_line('crease',(26,12),(26,32))
        self.relate('connect','body','tail')
        self.relate('connect','body','crease')
        self.relate('connect','tail','crease')


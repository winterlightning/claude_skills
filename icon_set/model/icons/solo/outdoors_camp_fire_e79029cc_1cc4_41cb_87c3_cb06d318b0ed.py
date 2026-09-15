'Campfire: retain the curling asymmetric flame above two genuinely crossing logs, lifting the flame base for clearance.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e79029cc-1cc4-41cb-87c3-cb06d318b0ed'
SOURCE_PATH = 'pictographic-primitives/outdoors/outdoors camp fire_e79029cc-1cc4-41cb-87c3-cb06d318b0ed.svg'
AUTHOR = 'gpt-6'

class OutdoorsCampFire(Solo48):
    icon_id = 'outdoors-camp-fire'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    aliases = ()
    keywords = ('outdoors', 'camp', 'fire')

    def build(self) -> None:
        # Preserve the asymmetric flame; cross two equal logs below its raised base.
        self.add_bezier('flame',(26,4),((16,9),(12,17),(14,23)),((16,31),(29,34),(34,26)),((37,21),(33,14),(30,12)),((30,20),(23,16),(26,4)))
        self.add_polyline('log-a',(8,37),(24,40),(40,44))
        self.add_polyline('log-b',(8,44),(24,40),(40,37))
        self.relate('connect','log-a','log-b')

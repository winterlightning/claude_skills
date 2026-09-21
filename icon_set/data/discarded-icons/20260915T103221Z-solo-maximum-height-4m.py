from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '51d07cc0-5d3e-489d-b18a-12bf56b9cf6a'
SOURCE_PATH = 'pictographic-primitives/transportation/road sign 4m high_51d07cc0-5d3e-489d-b18a-12bf56b9cf6a.svg'
AUTHOR = 'gpt-6'

class MaximumHeight4M(Solo48):
    icon_id = 'maximum-height-4m'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('height', '4m', 'clearance', 'maximum height', 'road sign', 'dimension', 'vehicle', 'traffic')

    def build(self):
        self.add_polyline('four-cross',(16,16),(6,28),(16,28))
        self.add_polyline('four-stem',(16,16),(16,28),(16,32))
        self.relate('connect','four-cross','four-stem')
        self.add_polyline('m',(26,32),(26,16),(34,26),(42,16),(42,32))
        self.add_polyline('upper-chevron',(20,8),(24,6),(28,8))
        self.add_polyline('lower-chevron',(20,40),(24,42),(28,40))

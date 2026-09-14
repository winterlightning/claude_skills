"""A width limit reading 2.5 above M, with tiny inward chevrons beside the unit. SQUARE ink (6,6)-(42,42). Exact value retained; Lucide type informs monoline letter construction."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9a1c2aa2-6935-41f2-96ed-4f3ebc7f1fc0'
SOURCE_PATH = 'pictographic-primitives/transportation/2.5m wide_9a1c2aa2-6935-41f2-96ed-4f3ebc7f1fc0.svg'
AUTHOR = 'gpt-6'

class WidthLimit25M(Solo48):
    icon_id = 'width-limit-2-5m'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('width', 'limit', 'restriction', '2.5m', 'road sign', 'narrow', 'vehicle', 'traffic')

    def build(self) -> None:
        self.add_polyline('two',(6,6),(14,6),(14,14),(6,22),(14,22))
        self.add_dot('decimal',(22,22))
        self.add_polyline('five',(38,6),(30,6),(30,14),(38,14),(38,22),(30,22))
        self.add_polyline('metres',(16,42),(16,34),(24,40),(32,34),(32,42))
        self.add_polyline('left-chevron',(6,31),(8,34),(6,37))
        self.add_polyline('right-chevron',(42,31),(40,34),(42,37))

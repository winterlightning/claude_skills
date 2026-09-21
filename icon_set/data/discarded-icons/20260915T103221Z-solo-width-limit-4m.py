"""A 4M width limit with inward-facing chevrons and stacked lettering. SQUARE ink (6,6)-(42,42). Lucide type informs monoline letters."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f92f1287-4d1f-4f11-b3d2-cf575c8bb3ec'
SOURCE_PATH = 'pictographic-primitives/transportation/4m wide_f92f1287-4d1f-4f11-b3d2-cf575c8bb3ec.svg'
AUTHOR = 'gpt-6'

class WidthLimit4M(Solo48):
    icon_id = 'width-limit-4m'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('width', 'limit', 'restriction', '4m', 'road sign', 'narrow', 'vehicle', 'traffic')

    def build(self) -> None:
        self.add_polyline('left-chevron',(6,19),(10,24),(6,29))
        self.add_polyline('right-chevron',(42,19),(38,24),(42,29))
        self.add_polyline('four',(19,6),(19,16),(29,16),(29,6),(29,19))
        self.add_polyline('metres',(16,42),(16,30),(24,36),(32,30),(32,42))

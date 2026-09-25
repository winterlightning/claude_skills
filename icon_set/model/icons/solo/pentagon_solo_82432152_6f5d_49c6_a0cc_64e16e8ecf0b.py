"""A five-sided outline with one top point and flat base. SQUARE extremes (6,6)-(42,42). Lucide pentagon informs paired slopes and softened corners. Use the integer-grid approximation with mirrored sides and round joins."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '82432152-6f5d-49c6-a0cc-64e16e8ecf0b'
SOURCE_PATH = 'pictographic-primitives/symbol/pentagon_82432152-6f5d-49c6-a0cc-64e16e8ecf0b.svg'
AUTHOR = 'gpt-6'


class PentagonSolo(Solo48):
    icon_id = 'pentagon-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    categories = ("symbol",)
    aliases = ()
    keywords = ('pentagon', 'shape', 'polygon', 'geometry', 'five', 'sides', 'outline', 'form')

    def build(self) -> None:
        self.add_polyline('pentagon',(24,6),(42,20),(35,42),(13,42),(6,20),(24,6),closed=True)

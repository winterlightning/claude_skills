"""Two matching water waves; tangent-continuous elliptical lobes keep the astrological read."""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '6a7d7977-2fda-5703-aeaa-a73c4a23525e'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__aquarius-zodiac-symbol/20260926T073831Z-thuan-mac/reference/astrology aquarius_6a7d7977-2fda-5703-aeaa-a73c4a23525e.svg'
AUTHOR = 'claude-opus-5-5'


class AquariusZodiacSymbol(Solo48):
    icon_id = 'aquarius-zodiac-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "culture"
    categories = ("culture", "primitives")
    aliases = ()
    keywords = ('aquarius', 'zodiac', 'astrology', 'water', 'waves', 'horoscope', 'star sign', 'symbol')

    def build(self) -> None:
        # Revision per review: each wave is wider and the two troughs are shallower. Per line: a
        # half-trough (4..14, 3 deep), a wide crest (14..34, 20 wide, 5 high) and a half-trough
        # (34..44, 3 deep). Upper line on y 13 (crest top 8, troughs 16), lower line on y 37
        # (crest top 32, troughs 40); the lines stay 16 apart.
        for label, y in (("upper", 13), ("lower", 37)):
            self.add_arc(label+"-left", (4, y), (14, y), radius_x=5, radius_y=3, sweep=False)
            self.add_arc(label+"-crest", (14, y), (34, y), radius_x=10, radius_y=5)
            self.add_arc(label+"-right", (34, y), (44, y), radius_x=5, radius_y=3, sweep=False)
            self.add_contour(label, label+"-left", label+"-crest", label+"-right")

"""Two matching water waves; tangent-continuous elliptical lobes keep the astrological read."""

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6a7d7977-2fda-5703-aeaa-a73c4a23525e'
SOURCE_PATH = 'pictographic-primitives/culture/batch-01/astrology aquarius_6a7d7977-2fda-5703-aeaa-a73c4a23525e.svg'


class AquariusZodiacSymbol(Solo48):
    icon_id = 'aquarius-zodiac-symbol'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "culture"
    aliases = ()
    keywords = ('aquarius', 'zodiac', 'astrology', 'water', 'waves', 'horoscope', 'star sign', 'symbol')

    def build(self) -> None:
        # HRECT_M: visible extremes (0, 9, 48, 39); centerlines inset 2.
        # Matching smooth waves, reflected about x=24; extrema y=11 and 37.
        for label, y in (("upper", 16), ("lower", 32)):
            self.add_arc(label+"-left", (2,y), (16,y), radius_x=7, radius_y=5, sweep=False)
            self.add_arc(label+"-crest", (16,y), (32,y), radius_x=8, radius_y=5)
            self.add_arc(label+"-right", (32,y), (46,y), radius_x=7, radius_y=5, sweep=False)
            self.add_contour(label, label+"-left", label+"-crest", label+"-right")

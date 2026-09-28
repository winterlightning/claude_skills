"""Two matching water waves; tangent-continuous elliptical lobes keep the astrological read."""

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6a7d7977-2fda-5703-aeaa-a73c4a23525e'
SOURCE_PATH = 'pictographic-primitives/culture/batch-01/astrology aquarius_6a7d7977-2fda-5703-aeaa-a73c4a23525e.svg'
AUTHOR = 'gpt-6'


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
        # HRECT_L: visible extremes (2, 6, 46, 42); centerlines inset 2.
        # Matching smooth waves, reflected about x=24; extrema y=8 and 40.
        for label, y in (("upper", 13), ("lower", 35)):
            self.add_arc(label+"-left", (4,y), (16,y), radius_x=6, radius_y=5, sweep=False)
            self.add_arc(label+"-crest", (16,y), (32,y), radius_x=8, radius_y=5)
            self.add_arc(label+"-right", (32,y), (44,y), radius_x=6, radius_y=5, sweep=False)
            self.add_contour(label, label+"-left", label+"-crest", label+"-right")

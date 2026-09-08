"""Libra dome above a parallel baseline. Extremes (2,8)-(46,40). Mirrored arch, no useful Lucide subject match; no features dropped."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cf03c01d-0ec1-5a48-b85f-a420423f6055'
SOURCE_PATH = 'pictographic-primitives/culture/batch-04/astrology libra_cf03c01d-0ec1-5a48-b85f-a420423f6055.svg'

class LibraZodiacSymbol(Solo48):
    icon_id = 'libra-zodiac-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/culture"
    aliases = ()
    keywords = ('libra', 'zodiac', 'astrology', 'scales', 'balance', 'horoscope', 'star sign', 'symbol')

    def build(self) -> None:
        self.add_line('left-arm',(2,32),(12,32))
        self.add_arc('dome',(12,32),(36,32),radius_x=15,large_arc=True)
        self.add_line('right-arm',(36,32),(46,32))
        self.add_contour('crown','left-arm','dome','right-arm')
        self.add_line('baseline',(2,40),(46,40))

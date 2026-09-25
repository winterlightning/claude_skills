"""Two repeated opening quotation loops with rising tails. Lucide quote informs repeated instances; direction follows the supplied opening marks.

SOLO48 HRECT_XL; geometry authored from its exact centerline extremes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b251c4a5-32cb-4f5c-a0d5-32ea0c61b0f1'
SOURCE_PATH = 'pictographic-primitives/symbol/quotation_b251c4a5-32cb-4f5c-a0d5-32ea0c61b0f1.svg'
AUTHOR = 'gpt-6'


class QuotationMarks(Solo48):
    icon_id = 'quotation-marks'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    categories = ("symbol",)
    aliases = ()
    keywords = ('quote', 'quotation', 'marks', 'citation', 'testimonial', 'speech', 'text', 'blockquote')

    def build(self) -> None:

        for i, left in enumerate((4,30)):
            p = 'quote-'+str(i)
            self.add_arc(p+'-loop-upper', (left,33), (left+14,33), radius_x=7)
            self.add_arc(p+'-loop-lower', (left+14,33), (left,33), radius_x=7)
            self.add_contour(p+'-loop', p+'-loop-upper', p+'-loop-lower', closed=True)
            self.add_line(p+'-tail-low', (left,33), (left,26))
            self.add_arc(p+'-tail-high', (left,26), (left+14,8), radius_x=24, sweep=True)
            self.add_contour(p+'-tail', p+'-tail-low', p+'-tail-high')
            self.relate('connect', p+'-loop', p+'-tail')

"""Lucide printer: paper emerging from broad housing. One text line; omitted tiny indicator and redundant rear seam."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '01574400-776e-5748-9773-f023d7884c14'
SOURCE_PATH = 'pictographic-primitives/shopping/receipt register_01574400-776e-5748-9773-f023d7884c14.svg'
AUTHOR = 'gpt-6'

class ReceiptPrinter(Solo48):
    icon_id = 'receipt-printer'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "shopping"
    aliases = ()
    keywords = ('receipt', 'printer', 'paper', 'checkout', 'retail', 'printing', 'device')

    def build(self) -> None:
        # SQUARE centerline extremes (6,6)-(42,42).
        self.add_polyline('paper',(14,28),(14,6),(34,6),(34,28),(29,24),(24,28),(19,24),(14,28),closed=True)
        self.add_line('text',(22,15),(26,15))
        self.add_polyline('housing',(14,20),(6,20),(6,34),(42,34),(42,20),(34,20))
        self.relate('connect','paper','housing')
        self.add_polyline('front',(6,34),(6,42),(42,42),(42,34))
        self.relate('connect','front','housing')

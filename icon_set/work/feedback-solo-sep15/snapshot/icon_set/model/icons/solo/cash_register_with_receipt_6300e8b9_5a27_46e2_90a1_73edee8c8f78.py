"""Lucide printer: stepped physical housing. Retained integral paper and display; omitted keys to keep the sloping deck clear."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6300e8b9-5a27-46e2-90a1-73edee8c8f78'
SOURCE_PATH = 'pictographic-primitives/shopping/receipt register print_6300e8b9-5a27-46e2-90a1-73edee8c8f78.svg'
AUTHOR = 'gpt-6'

class CashRegisterWithReceipt(Solo48):
    icon_id = 'cash-register-with-receipt'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/shopping"
    aliases = ()
    keywords = ('register', 'cash', 'receipt', 'checkout', 'keypad', 'retail', 'terminal')

    def build(self) -> None:
        # SQUARE centerline extremes (6,6)-(42,42).
        self.add_polyline('drawer',(6,32),(42,32),(42,42),(6,42),(6,32),closed=True)
        self.add_polyline('deck',(6,32),(10,22),(16,22),(24,22),(38,22),(42,32))
        self.relate('connect','deck','drawer')
        self.add_polyline('paper',(16,22),(16,8),(20,11),(24,8),(24,22))
        self.relate('connect','paper','deck')
        self.add_polyline('display',(32,6),(42,6),(42,14),(37,14),(32,14),(32,6),closed=True)
        self.add_line('post',(37,14),(37,22))
        self.relate('connect','post','display')
        self.relate('connect','post','deck')

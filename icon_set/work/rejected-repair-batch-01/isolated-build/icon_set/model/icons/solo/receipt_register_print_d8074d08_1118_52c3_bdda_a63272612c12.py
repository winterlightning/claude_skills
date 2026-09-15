'Receipt printer: regular paper slots, rounded body and a clear serrated receipt edge.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd8074d08-1118-52c3-bdda-a63272612c12'
SOURCE_PATH = 'pictographic-primitives/shopping/receipt register print_d8074d08-1118-52c3-bdda-a63272612c12.svg'
AUTHOR = 'gpt-6'

class ReceiptRegisterPrint(Solo48):
    icon_id = 'receipt-register-print'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shopping'
    aliases = ()
    keywords = ('receipt', 'register', 'print', 'shopping')

    def build(self):
        # Receipt printer: clear 8-unit body bands and a paper opening with no hidden edge across the receipt.
        l = self.add_line
        p = self.add_polyline
        link = self.relate

        def a(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx,
                         radius_y=rx if ry is None else ry, sweep=sweep)

        p('printer-top',(14,34),(6,34),(6,18),(42,18),(42,34),(34,34))
        p('paper-in',(12,18),(12,6),(36,6),(36,18))
        link('connect','paper-in','printer-top')
        p('receipt',(14,26),(14,42),(20,38),(26,42),(34,38),(34,26))
        l('slot',(10,26),(38,26))
        link('connect','receipt','slot')
        link('connect','receipt','printer-top')

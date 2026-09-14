'Layered currency: regular diamonds and separated layer strokes with deliberate straight edges.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '573e6276-1546-4e04-a069-78d9e36ee390'
SOURCE_PATH = 'icons-json/design/virtual coin cyrpto currency_573e6276-1546-4e04-a069-78d9e36ee390.json'
AUTHOR = 'gpt-6'

class VirtualCoinCyrptoCurrency(Solo48):
    icon_id = 'virtual-coin-cyrpto-currency'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('virtual', 'coin', 'cyrpto', 'currency', 'design')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('top-1', (8, 12), (24, 4))
        self.add_line('top-2', (24, 4), (40, 12))
        self.add_line('top-3', (40, 12), (24, 20))
        self.add_line('top-4', (24, 20), (8, 12))
        self.add_line('middle-1', (8, 24), (24, 32))
        self.add_line('middle-2', (24, 32), (40, 24))
        self.add_line('bottom-1', (8, 36), (24, 44))
        self.add_line('bottom-2', (24, 44), (40, 36))
        self.add_contour('top', *('top-1', 'top-2', 'top-3', 'top-4'), closed=False)
        self.add_contour('middle', *('middle-1', 'middle-2'), closed=False)
        self.add_contour('bottom', *('bottom-1', 'bottom-2'), closed=False)

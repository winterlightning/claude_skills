"""Lucide receipt-text: one paper contour and repeated rows. Three item/price rows; omitted final short total line."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7d81e55d-09f4-488e-996e-0f6472b01928'
SOURCE_PATH = 'pictographic-primitives/shopping/receipt slip_7d81e55d-09f4-488e-996e-0f6472b01928.svg'
AUTHOR = 'gpt-6'

class RoundedItemizedReceipt(Solo48):
    icon_id = 'rounded-itemized-receipt'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/shopping"
    aliases = ()
    keywords = ('receipt', 'slip', 'paper', 'invoice', 'purchase', 'checkout', 'itemized')

    def build(self) -> None:
        # VRECT_L centerline envelope (8,4)-(40,44).
        self.add_line('top',(12,4),(36,4))
        self.add_arc('tr',(36,4),(40,8),radius_x=4)
        self.add_line('sides-1',(40, 8),(40, 44))
        self.add_line('sides-2',(40, 44),(32, 39))
        self.add_line('sides-3',(32, 39),(24, 44))
        self.add_line('sides-4',(24, 44),(16, 39))
        self.add_line('sides-5',(16, 39),(8, 44))
        self.add_line('sides-6',(8, 44),(8, 8))
        self.add_arc('tl',(8,8),(12,4),radius_x=4)
        self.add_contour('paper','top','tr',*(f'sides-{i}' for i in range(1,7)),'tl',closed=True)
        for index,y in enumerate((13,22,31)):
            self.add_line(f'item-{index}',(17,y),(23,y))
            self.add_dot(f'price-{index}',(31,y))

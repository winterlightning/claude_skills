"""Lucide receipt-text: coherent paper outline and spaced rows. Three item/price rows retained; extra total line omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0ff678ff-6655-4906-a62a-7b01744b6388'
SOURCE_PATH = 'pictographic-primitives/shopping/receipt slip_0ff678ff-6655-4906-a62a-7b01744b6388.svg'
AUTHOR = 'gpt-6'

class ItemizedReceipt(Solo48):
    icon_id = 'itemized-receipt'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "shopping"
    categories = ("shopping", "primitives")
    aliases = ()
    keywords = ('receipt', 'slip', 'paper', 'invoice', 'purchase', 'checkout', 'itemized')

    def build(self) -> None:
        # VRECT_L centerline extremes (8,4)-(40,44).
        self.add_polyline('paper',(8,4),(40,4),(40,44),(32,39),(24,44),(16,39),(8,44),(8,4),closed=True)
        for index,y in enumerate((13,22,31)):
            self.add_line(f'item-{index}',(16,y),(23,y))
            self.add_dot(f'price-{index}',(32,y))

'Coin: concentric circular rims and a centered value mark; balanced radial spacing.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5cabb173-08d9-478c-9912-5357cbf2ed85'
SOURCE_PATH = 'pictographic-primitives/money/coins_5cabb173-08d9-478c-9912-5357cbf2ed85.svg'
AUTHOR = 'gpt-6'

class Coins(Solo48):
    icon_id = 'coins'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    aliases = ()
    keywords = ('coins', 'money')

    def build(self) -> None:
        self.add_arc('rim-top', (4,24), (44,24), radius_x=20, radius_y=20)
        self.add_arc('rim-bottom', (44,24), (4,24), radius_x=20, radius_y=20)
        self.add_contour('rim', 'rim-top', 'rim-bottom', closed=True)

        self.add_arc('inner-top', (13,24), (35,24), radius_x=11, radius_y=11)
        self.add_arc('inner-bottom', (35,24), (13,24), radius_x=11, radius_y=11)
        self.add_contour('inner', 'inner-top', 'inner-bottom', closed=True)
        self.add_line('value',(24,22),(24,26))

"""An arched headband joins two rounded ear cups. SQUARE extremes (6,6)-(42,42). Lucide headphones informs coherent band-to-cup connections and matched rounded cups. Preserve symmetry and omit no source component."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1107c9dd-40f5-4f90-9797-a72017359e90'
SOURCE_PATH = 'pictographic-primitives/symbol/headset_1107c9dd-40f5-4f90-9797-a72017359e90.svg'
AUTHOR = 'gpt-6'


class Headphones(Solo48):
    icon_id = 'headphones'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('headphones', 'headset', 'audio', 'music', 'listen', 'sound', 'support', 'earphones')

    def build(self) -> None:
        self.add_arc('headband',(6,28),(42,28),radius_x=18,radius_y=22)
        for name,x in [('left',6),('right',32)]:
            self.add_line(name+'-top',(x,28),(x+7,28))
            self.add_arc(name+'-tr',(x+7,28),(x+10,31),radius_x=3)
            self.add_line(name+'-right',(x+10,31),(x+10,39))
            self.add_arc(name+'-br',(x+10,39),(x+7,42),radius_x=3)
            self.add_line(name+'-bottom',(x+7,42),(x+3,42))
            self.add_arc(name+'-bl',(x+3,42),(x,39),radius_x=3)
            self.add_line(name+'-left',(x,39),(x,28))
            self.add_contour(name+'-cup',*(name+'-'+p for p in ['top','tr','right','br','bottom','bl','left']),closed=True)
            self.relate('connect','headband',name+'-cup')

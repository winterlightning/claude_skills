"""money bill pound: complete SOLO48 repair.
Kept the banknote enclosure and sterling denomination; removed four decorative corner loops to reserve room for the currency sign.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a2425a69-d3ed-4c10-8e19-41a99038d49e'
SOURCE_PATH = 'pictographic-primitives/other/money bill pound_a2425a69-d3ed-4c10-8e19-41a99038d49e.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'money-bill-pound'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('money bill pound',)




    def banknote(self):
        self.add_polyline('note',(4,8),(44,8),(44,40),(4,40),closed=True)
    def build(self):
        # Banknote corner decoration and a hand-authored pound sterling symbol.
        self.banknote()
        self.add_arc('pound-hook',(30,21),(22,21),radius_x=4,sweep=False)
        self.add_line('pound-upper',(22,21),(22,23))
        self.add_line('pound-lower',(22,23),(22,27))
        self.add_arc('pound-curve',(22,27),(18,31),radius_x=4)
        self.add_line('pound-base',(18,31),(30,31))
        self.add_contour('pound','pound-hook','pound-upper','pound-lower','pound-curve','pound-base')
        self.add_polyline('pound-bar',(18,23),(22,23),(26,23))
        self.relate('connect','pound','pound-bar')

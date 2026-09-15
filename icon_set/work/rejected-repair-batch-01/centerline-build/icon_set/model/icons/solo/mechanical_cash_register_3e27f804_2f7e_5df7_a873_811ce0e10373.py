"""No useful exact Lucide mechanical-register match. Tangent quarter-circle slope, rounded column, circular crank hub and one projecting key. Simplified the key bank and second crank joint."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3e27f804-2f7e-5df7-a873-811ce0e10373'
SOURCE_PATH = 'pictographic-primitives/shopping/receipt register_3e27f804-2f7e-5df7-a873-811ce0e10373.svg'
AUTHOR = 'gpt-6'

class MechanicalCashRegister(Solo48):
    icon_id = 'mechanical-cash-register'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/shopping"
    aliases = ()
    keywords = ('register', 'cash', 'mechanical', 'crank', 'keys', 'retail', 'checkout')

    def build(self) -> None:
        # VRECT_L centerline extremes (8,4)-(40,44).
        self.add_line('rear',(8,40),(8,8))
        self.add_arc('cap-left',(8,8),(12,4),radius_x=4)
        self.add_line('cap',(12,4),(16,4))
        self.add_arc('cap-right',(16,4),(20,8),radius_x=4)
        self.add_line('neck',(20,8),(20,16))
        self.add_arc('slope-a',(20,16),(32,22),radius_x=15)
        self.add_arc('slope-b',(32,22),(35,31),radius_x=15)
        self.add_line('base-1',(35,31),(40,31))
        self.add_line('base-2',(40,31),(40,44))
        self.add_line('base-3',(40,44),(8,44))
        self.add_line('base-4',(8,44),(8,40))
        self.add_contour('body','rear','cap-left','cap','cap-right','neck','slope-a','slope-b','base-1','base-2','base-3','base-4',closed=True)
        self.add_line('key',(32,22),(38,18))
        self.relate('connect','key','body')
        self.add_arc('hub-a',(17,29),(23,29),radius_x=3)
        self.add_arc('hub-b',(23,29),(17,29),radius_x=3)
        self.add_contour('hub','hub-a','hub-b',closed=True)
        self.add_line('crank',(23,29),(27,35))
        self.relate('connect','crank','hub')

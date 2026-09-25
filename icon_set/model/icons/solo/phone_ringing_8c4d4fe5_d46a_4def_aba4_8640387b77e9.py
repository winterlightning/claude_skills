"""A telephone handset with two radiating sound waves. SQUARE extremes (6,6)-(42,42). Lucide phone-call informs tangent handset curves and concentric quarter-circle waves. Omit end-piece dividing seams to preserve clear interior space; retain both waves and the diagonal handset."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8c4d4fe5-d46a-4def-aba4-8640387b77e9'
SOURCE_PATH = 'pictographic-primitives/symbol/phone with electric waves_8c4d4fe5-d46a-4def-aba4-8640387b77e9.svg'
AUTHOR = 'gpt-6'


class PhoneRinging(Solo48):
    icon_id = 'phone-ringing'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    aliases = ()
    keywords = ('phone', 'call', 'ringing', 'handset', 'telephone', 'contact', 'sound', 'incoming')

    def build(self) -> None:
        self.add_arc('ear-top-left',(6,10),(10,6),radius_x=4)
        self.add_line('ear-top',(10,6),(14,6))
        self.add_arc('ear-top-right',(14,6),(18,10),radius_x=4)
        self.add_line('ear-inner',(18,10),(18,14))
        self.add_arc('handset-inner',(18,14),(34,30),radius_x=16,sweep=False)
        self.add_line('mouth-top',(34,30),(38,30))
        self.add_arc('mouth-top-right',(38,30),(42,34),radius_x=4)
        self.add_line('mouth-right',(42,34),(42,38))
        self.add_arc('mouth-bottom',(42,38),(38,42),radius_x=4)
        self.add_arc('handset-outer',(38,42),(6,10),radius_x=32)
        self.add_contour('handset','ear-top-left','ear-top','ear-top-right','ear-inner','handset-inner','mouth-top','mouth-top-right','mouth-right','mouth-bottom','handset-outer',closed=True)
        self.add_arc('wave-outer',(27,6),(42,21),radius_x=15)
        self.add_arc('wave-inner',(27,15),(33,21),radius_x=6)

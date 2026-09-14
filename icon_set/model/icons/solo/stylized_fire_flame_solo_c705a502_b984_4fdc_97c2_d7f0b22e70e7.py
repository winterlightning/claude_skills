"""Asymmetric flame with tall tip, side tongue and round base. VRECT_XL centerlines 8,4–40,44. Lucide flame informs lobed contour; omit interior miniature flame to preserve generous clear space."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c705a502-b984-4fdc-97c2-d7f0b22e70e7'
SOURCE_PATH = 'pictographic-primitives/social/trends hot flame_c705a502-b984-4fdc-97c2-d7f0b22e70e7.svg'
AUTHOR = 'gpt-6'

class StylizedFireFlameSolo(Solo48):
    icon_id = 'stylized-fire-flame-solo'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/social"
    aliases = ()
    keywords = ('fire', 'flame', 'heat', 'burning', 'blaze', 'hot')

    def build(self):
        self.add_arc('outer-rise',(24,4),(40,28),radius_x=32,radius_y=32)
        self.add_arc('base',(40,28),(8,28),radius_x=16)
        self.add_arc('small-tongue',(8,28),(14,17),radius_x=6,radius_y=11)
        self.add_arc('hook',(14,17),(18,25),radius_x=9,sweep=False)
        self.add_arc('inner-rise',(18,25),(24,4),radius_x=22,sweep=False)
        self.add_contour('flame','outer-rise','base','small-tongue','hook','inner-rise',closed=True)

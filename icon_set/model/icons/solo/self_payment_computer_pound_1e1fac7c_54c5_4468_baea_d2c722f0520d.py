"""self payment computer pound: standalone batch 17 repair.
Retained the payment screen, stand, pound sign and two menu marks. Taller screen, shorter hook and crossbar; reduced menu rules to dots.
"""
from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
from ._base import Solo48
SOURCE_ICON_ID = '1e1fac7c-54c5-4468-baea-d2c722f0520d'
SOURCE_PATH = 'pictographic-primitives/other/self payment computer pound_1e1fac7c-54c5-4468-baea-d2c722f0520d.svg'
AUTHOR = 'gpt-6'
CONSTRUCTION_REFERENCE = 'pound-sterling'

class Drawing(Solo48):
    icon_id='self-payment-computer-pound'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('other', 'primitives-generate')
    aliases=()
    keywords=('self', 'payment', 'computer', 'pound')





    def terminal(self):
        self.add_polyline('screen',(8,4),(40,4),(40,36),(24,36),(8,36),closed=True)
        self.add_line('stand',(24,36),(24,44));self.relate('connect','screen','stand')
        self.add_polyline('foot',(16,44),(24,44),(32,44));self.relate('connect','stand','foot')
        for i,y in enumerate((18,26)):self.add_line(f'equals-{i}',(32,y),(32,y))


    def build(self):
        self.terminal()
        self.add_arc('hook',(23,16),(17,16),radius_x=3,sweep=False)
        self.add_polyline('stem',(17,16),(17,20),(17,28))
        self.add_polyline('bar',(17,20),(19,20))
        self.add_polyline('base',(17,28),(24,28))
        self.relate('connect','hook','stem');self.relate('connect','stem','bar');self.relate('connect','stem','base')


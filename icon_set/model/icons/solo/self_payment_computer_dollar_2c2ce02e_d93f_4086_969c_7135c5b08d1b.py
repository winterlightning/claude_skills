"""self payment computer dollar: standalone batch 17 repair.
Retained the payment screen, stand, dollar sign and two menu marks. Replaced the continuous dollar stem with connected top/bottom extensions to eliminate tiny enclosed pockets; reduced menu rules to dots.
"""
from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
from ._base import Solo48
SOURCE_ICON_ID = '2c2ce02e-d93f-4086-969c-7135c5b08d1b'
SOURCE_PATH = 'pictographic-primitives/other/self payment computer dollar_2c2ce02e-d93f-4086-969c-7135c5b08d1b.svg'
AUTHOR = 'gpt-6'
CONSTRUCTION_REFERENCE = 'dollar-sign'

class Drawing(Solo48):
    icon_id = 'self-payment-computer-dollar'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('self', 'payment', 'computer', 'dollar')


    def build(self):
        self.add_polyline('screen',(8,4),(40,4),(40,36),(24,36),(8,36),closed=True)
        self.add_line('stand',(24,36),(24,44))
        self.add_polyline('foot',(16,44),(24,44),(32,44))
        self.relate('connect','screen','stand');self.relate('connect','stand','foot')
        self.add_bezier('dollar-cap',(24,15),((23,14),(21,14),(20,14)))
        self.add_bezier('dollar-upper',(20,14),((16,14),(16,19),(20,20)))
        self.add_bezier('dollar-lower',(20,20),((24,21),(24,26),(20,26)))
        self.add_bezier('dollar-foot',(20,26),((19,26),(17,26),(17,25)))
        self.add_contour('dollar','dollar-cap','dollar-upper','dollar-lower','dollar-foot')
        self.add_line('stem-top',(20,12),(20,14))
        self.add_line('stem-bottom',(20,26),(20,28))
        self.relate('connect','dollar','stem-top');self.relate('connect','dollar','stem-bottom')
        for i,y in enumerate((16,24)):self.add_dot('menu-'+str(i),(32,y))


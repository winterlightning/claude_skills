"""A smartphone makes a contactless payment beside a register. SQUARE fits the paired devices. Lucide smartphone and nfc inform the rounded phone and signal; monitor informs the register display/post. Omit the dollar and one signal arc to retain both recognizable devices.
Centerline bounds: (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import rounded_rect
from ._payments_batch02 import small_dollar
SOURCE_ICON_ID='b8a858c7-f6b3-475c-af00-449b9b0294c2'
SOURCE_PATH='pictographic-primitives/payments/wireless payment smartphone_b8a858c7-f6b3-475c-af00-449b9b0294c2.svg'
AUTHOR='gpt-6'

class SmartphonePayingAtRegister(Solo48):
    icon_id='smartphone-paying-at-register'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/payments'
    aliases=()
    keywords=('wireless', 'payment', 'smartphone', 'register', 'checkout', 'nfc', 'dollar', 'pos')
    def build(self):
        # Two physically distinct checkout devices with a nine-unit clear aisle.
        # Equal corner radii; the bezel attachment is a shared node on each wall.
        self.add_line('phone-top',(30,18),(38,18))
        self.add_arc('phone-tr',(38,18),(42,22),radius_x=4)
        self.add_line('phone-right-top',(42,22),(42,34))
        self.add_line('phone-right-bottom',(42,34),(42,38))
        self.add_arc('phone-br',(42,38),(38,42),radius_x=4)
        self.add_line('phone-bottom',(38,42),(30,42))
        self.add_arc('phone-bl',(30,42),(26,38),radius_x=4)
        self.add_line('phone-left-bottom',(26,38),(26,34))
        self.add_line('phone-left-top',(26,34),(26,22))
        self.add_arc('phone-tl',(26,22),(30,18),radius_x=4)
        self.add_contour('phone','phone-top','phone-tr','phone-right-top','phone-right-bottom','phone-br','phone-bottom','phone-bl','phone-left-bottom','phone-left-top','phone-tl',closed=True)
        self.add_line('phone-bezel',(26,34),(42,34))
        self.relate('connect','phone','phone-bezel')
        self.add_arc('wireless',(26,10),(42,10),radius_x=8,radius_y=4)
        self.add_polyline('display',(6,14),(16,14),(16,22),(11,22),(6,22),closed=True)
        self.add_line('display-post',(11,22),(11,30))
        self.add_polyline('register',(6,38),(8,30),(11,30),(14,30),(16,38),closed=True)
        self.relate('connect','display','display-post')
        self.relate('connect','register','display-post')

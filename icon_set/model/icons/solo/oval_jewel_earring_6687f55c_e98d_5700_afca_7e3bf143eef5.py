"""Single jewel earring with open curved hook. VRECT_S extremes (14,2)-(34,46). Intentional right hook opening. No useful Lucide subject match; oval is unadorned."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6687f55c-e98d-5700-afca-7e3bf143eef5'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-03/earring jewel_6687f55c-e98d-5700-afca-7e3bf143eef5.svg'
AUTHOR = 'astra-chatgpt'


class OvalJewelEarring(Solo48):
    icon_id = 'oval-jewel-earring'
    keyshape = Keyshape.VRECT_S
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/accessories"
    aliases = ()
    keywords = ('earring', 'jewel', 'oval', 'hook', 'jewellery', 'jewelry', 'drop', 'accessory', 'gem')

    def build(self) -> None:
        self.add_arc('hook-top', (14, 9), (34, 9), radius_x=10, radius_y=7, sweep=True)
        self.add_arc('hook-bottom', (24, 16), (14, 9), radius_x=10, radius_y=7, sweep=True)
        self.add_line('post', (24, 16), (24, 24))
        self.add_contour('hook', 'hook-bottom', 'hook-top', closed=False)
        self.add_arc('jewel-0', (24, 24), (31, 35), radius_x=7, radius_y=11, sweep=True)
        self.add_arc('jewel-1', (31, 35), (24, 46), radius_x=7, radius_y=11, sweep=True)
        self.add_arc('jewel-2', (24, 46), (17, 35), radius_x=7, radius_y=11, sweep=True)
        self.add_arc('jewel-3', (17, 35), (24, 24), radius_x=7, radius_y=11, sweep=True)
        self.add_contour('jewel', 'jewel-0', 'jewel-1', 'jewel-2', 'jewel-3', closed=True)
        self.relate("connect", 'hook', 'post')
        self.relate("connect", 'post', 'jewel')

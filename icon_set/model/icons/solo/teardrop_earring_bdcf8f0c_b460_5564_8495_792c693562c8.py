"""A hooked earring with a pointed drop. VRECT_S extremes (14,2)-(34,46). Circular hook and circular lower bowl simplify the source; intentional opening on the left. No useful exact Lucide match."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bdcf8f0c-b460-5564-8495-792c693562c8'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-05/earring_bdcf8f0c-b460-5564-8495-792c693562c8.svg'
AUTHOR = 'astra-chatgpt'


class TeardropEarring(Solo48):
    icon_id = 'teardrop-earring'
    keyshape = Keyshape.VRECT_S
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/accessories"
    aliases = ()
    keywords = ('earring', 'teardrop', 'drop', 'hook', 'jewellery', 'jewelry', 'pendant', 'accessory')

    def build(self) -> None:
        self.add_arc('hook', (17, 9), (31, 9), radius_x=7, radius_y=7, sweep=True)
        self.add_arc('hook-return', (31, 9), (24, 16), radius_x=7, radius_y=7, sweep=True)
        self.add_line('post', (24, 16), (24, 23))
        self.add_contour('earwire', 'hook', 'hook-return', 'post', closed=False)
        self.add_arc('drop-left', (24, 23), (14, 36), radius_x=25, sweep=False)
        self.add_arc('drop-bottom', (14, 36), (34, 36), radius_x=10, sweep=False)
        self.add_arc('drop-right', (34, 36), (24, 23), radius_x=25, sweep=False)
        self.add_contour('pendant', 'drop-left', 'drop-bottom', 'drop-right', closed=True)
        self.relate('connect', 'earwire', 'pendant')

"""A diagonal hatchet with flared curved cutting edge and long handle; small butt cap omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6ab36fdc-b442-5f9f-afc2-c43f74bf4130'
SOURCE_PATH = 'pictographic-primitives/tools/tools axe_6ab36fdc-b442-5f9f-afc2-c43f74bf4130.svg'
AUTHOR = 'gpt-6'

class Hatchet(Solo48):
    icon_id = 'hatchet'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "tools"
    aliases = ()
    keywords = ('axe', 'hatchet', 'chop', 'wood', 'lumberjack', 'camping', 'blade', 'tool')

    def build(self) -> None:
        self.add_line('head-upper-1',(18, 6),(10, 14))
        self.add_line('head-upper-2',(10, 14),(24, 28))
        self.add_line('head-upper-3',(24, 28),(26, 38))
        self.add_arc('edge',(26,38),(42,22),radius_x=16,sweep=False)
        self.add_line('head-back-1',(42, 22),(32, 20))
        self.add_line('head-back-2',(32, 20),(18, 6))
        self.add_contour('head','head-upper-1','head-upper-2','head-upper-3','edge','head-back-1','head-back-2',closed=True)
        self.add_polyline('handle',(14,18),(6,34),(6,42),(14,40),(24,28))
        self.relate('connect','handle','head')

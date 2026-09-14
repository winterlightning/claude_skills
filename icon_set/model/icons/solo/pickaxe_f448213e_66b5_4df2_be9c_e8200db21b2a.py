"""A pickaxe has a bowed double-point head and diagonal handle; the small cap is omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f448213e-66b5-4df2-be9c-e8200db21b2a'
SOURCE_PATH = 'pictographic-primitives/tools/tools pickaxe_f448213e-66b5-4df2-be9c-e8200db21b2a.svg'
AUTHOR = 'gpt-6'

class Pickaxe(Solo48):
    icon_id = 'pickaxe'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/tools"
    aliases = ()
    keywords = ('pickaxe', 'pick', 'mining', 'dig', 'excavate', 'construction', 'miner', 'tool')

    def build(self) -> None:


        self.add_line('head-top',(12,6),(26,6))
        self.add_arc('head-bow',(26,6),(42,22),radius_x=16)
        self.add_line('head-tip',(42,22),(42,36))
        self.add_line('head-inner-1',(42, 36),(30, 18))
        self.add_line('head-inner-2',(30, 18),(12, 6))
        self.add_contour('head','head-top','head-bow','head-tip','head-inner-1','head-inner-2',closed=True)
        self.add_polyline('handle',(24,14),(6,32),(6,42),(16,42),(34,24))
        self.relate('connect','handle','head')

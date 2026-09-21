"""Capital S and M. Lucide type/strikethrough construction reviewed in preceding batches informs coherent monoline letters; deep M valley and leaning outer legs retained.

SOLO48 HRECT_L; live visible envelope (2, 6, 46, 42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4948e3d9-c691-4600-b65b-84b1ea7abd1c'
SOURCE_PATH = 'pictographic-primitives/symbol/sm_4948e3d9-c691-4600-b65b-84b1ea7abd1c.svg'
AUTHOR = 'gpt-6'


class SmText(Solo48):
    icon_id = 'sm-text'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('sm', 'letters', 'text', 'abbreviation', 'typography', 'label', 'size')

    def build(self) -> None:

        self.add_arc('s-crown',(18,16),(4,16),radius_x=7,radius_y=8,sweep=False)
        self.add_arc('s-upper',(4,16),(11,24),radius_x=7,radius_y=8,sweep=False)
        self.add_arc('s-lower',(11,24),(18,32),radius_x=7,radius_y=8)
        self.add_arc('s-base',(18,32),(4,32),radius_x=7,radius_y=8)
        self.add_contour('s','s-crown','s-upper','s-lower','s-base')
        self.add_polyline('m',(28,40),(30,8),(36,30),(42,8),(44,40))

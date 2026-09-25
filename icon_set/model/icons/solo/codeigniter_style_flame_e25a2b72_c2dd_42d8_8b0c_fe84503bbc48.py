"""Stylized Fire Flame Symbol."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e25a2b72-c2dd-42d8-8b0c-fe84503bbc48'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/fire/codeigniter logo_e25a2b72-c2dd-42d8-8b0c-fe84503bbc48.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'codeigniter-style-flame'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'fire'
    aliases = ()
    keywords = ('codeigniter', 'flame', 'fire', 'logo', 'burning', 'heat', 'symbol')

    def build(self):
        # Plan: Asymmetric outer flame with right spur and large returning interior tongue. Lucide flame bowl; retain the distinctive soft inward scoop. Bounds (8,4)-(40,44).
        self.add_bezier('outer',(16,44),((10,40),(8,35),(8,29)),((8,18),(23,16),(22,4)),((32,7),(30,15),(29,18)),((26,24),(36,27),(36,19)),((39,22),(40,27),(40,30)),((40,37),(34,42),(30,44)))
        self.add_bezier('tongue',(30,44),((35,34),(23,37),(23,27)),((16,31),(13,36),(16,44)))
        self.relate('connect','outer','tongue')

"""Two open angular arrow outlines point northeast, one large and one small. SQUARE retains diagonal spread. Lucide chevrons-up contributes separate coherent directional contours; source supplies unequal sizes and interrupted large diagonal. No essential details omitted.
Plan: exact SQUARE envelope; stroke 4, integer points, shared attachment nodes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ed207444-3fbc-43de-9ecc-94bbc442aafd'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_02/amazon appstream_ed207444-3fbc-43de-9ecc-94bbc442aafd.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'paired-northeast-outline-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = []
    keywords = ['paired', 'northeast', 'outline', 'arrows']

    def build(self):
        self.add_polyline('large-arrow',(18,18),(6,6),(42,6),(42,42),(30,30))
        self.add_polyline('small-arrow',(6,26),(22,26),(22,42),closed=True)

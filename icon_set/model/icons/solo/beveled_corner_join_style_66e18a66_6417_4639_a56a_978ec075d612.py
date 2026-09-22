"""An outlined L-shaped stroke with a clipped outer corner and inner construction guide. SQUARE preserves the equal horizontal and vertical arms. Guide is intrinsic drafting detail, not hosted content. Lucide corner-left-up supplies coherent turning strokes; bevel stays a deliberate diagonal. Small square control node omitted.
Source editorial brief is preserved in the gallery; source supplies identity and arrangement.
"""
from ._base import Solo48
from ...keyshapes import Keyshape

SOURCE_ICON_ID = '66e18a66-6417-4639-a56a-978ec075d612'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_06/bevel join_66e18a66-6417-4639-a56a-978ec075d612.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'beveled-corner-join-style'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "Uncategorized"
    aliases = ['Beveled Corner Join Style']
    keywords = ['bevel', 'corner', 'join', 'stroke', 'outline', 'design', 'guide']

    def build(self):
        self.add_polyline("outline",(6,14),(14,6),(42,6),(42,16),(42,24),(24,24),(24,42),(16,42),(6,42),closed=True)
        self.add_polyline("guide",(16,42),(16,16),(42,16))
        self.relate("connect","outline","guide")

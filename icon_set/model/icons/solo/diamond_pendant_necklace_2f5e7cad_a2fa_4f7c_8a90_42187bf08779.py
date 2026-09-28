"""A V-shaped necklace chain suspends a diamond-shaped pendant. SQUARE gives equal chain arms and enough pendant height. Axis24 owns mirrored chain and diamond vertices. Lucide gem supplies polygonal gem facets; source supplies pendant arrangement. Short bail and horizontal facet omitted for a clean open diamond.
Source editorial brief is preserved in the gallery; source supplies identity and arrangement.
"""
from ._base import Solo48
from ...keyshapes import Keyshape

SOURCE_ICON_ID = '2f5e7cad-a2fa-4f7c-8a90-42187bf08779'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_06/bijou_2f5e7cad-a2fa-4f7c-8a90-42187bf08779.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'diamond-pendant-necklace'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ['Diamond Pendant Necklace']
    keywords = ['pendant', 'diamond', 'necklace', 'chain', 'jewelry', 'gem', 'accessory']

    def build(self):
        self.add_polyline("chain",(6,6),(24,22),(42,6))
        self.add_polyline("pendant",(24,22),(34,32),(24,42),(14,32),closed=True)
        self.relate("connect","chain","pendant")

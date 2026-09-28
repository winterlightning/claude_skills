"""Axe in Tree Stump.
Plan: Broad axe blade joins a diagonal handle above a rooted stump. Extrema (6,6)-(42,42).
Reference: Lucide axe: broad wedge attached at a single handle junction.
Reduction: Bark grooves omitted; broad blade, diagonal handle and flared roots carry identity.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1058f16d-2519-4029-a167-bf1f868e8cc8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/farming/trees chop_1058f16d-2519-4029-a167-bf1f868e8cc8.svg'
AUTHOR = 'gpt-6'

class Batch27Icon(Solo48):
    icon_id = 'axe-embedded-tree-stump'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "farming"
    categories = ("farming", "primitives")
    aliases = ()
    keywords = ('axe', 'in', 'tree', 'stump')

    def build(self):

        self.add_polyline('stump',(6,42),(10,28),(19,28),(36,28),(42,42),(6,42))
        self.add_polyline('blade',(19,28),(14,12),(23,6),(29,18),(19,28))
        self.relate('connect','stump','blade')
        self.add_line('handle',(29,18),(42,6));self.relate('connect','handle','blade')

"""Diamond slab above a lower open chevron. SQUARE extremes (6,6)-(42,42). Reduce shallow doubled slab edges to one stroke per layer, preserving the stacked diamond silhouette. Lucide layers-2 informs matched perspective slopes."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='1d44c396-8886-4611-90cc-2e66acd82f3c'
SOURCE_PATH='pictographic-primitives/money/virtual coin crypto stratis_1d44c396-8886-4611-90cc-2e66acd82f3c.svg'
AUTHOR='gpt-6'

class StratisLayeredEmblem(Solo48):
    icon_id='stratis-layered-emblem'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "money"
    categories = ("primitives", "money")
    aliases=()
    keywords=('stratis', 'crypto', 'emblem', 'layer', 'stack', 'diamond')

    def build(self):
        self.add_polyline('upper',(6,16),(24,6),(42,16),(24,26),(6,16))
        self.add_polyline('lower',(6,32),(24,42),(42,32),(42,28))

"""Two irregular ground edges descend around an open fissure. Square envelope balances depth with separated ground surfaces. Reference supplies asymmetric zigzag banks. No useful Lucide geological crack match. Omit tiny bends; use a shared right-bank offset for consistent clearance."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = 'c325c94a-e25b-4856-9d79-9c47ededff04'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_11/chasm_c325c94a-e25b-4856-9d79-9c47ededff04.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = 'jagged-ground-fissure'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ['Jagged Ground Fissure']
    keywords = ['fissure', 'crack', 'ground', 'chasm', 'earth', 'jagged', 'geology']
    def build(self):
        self.add_polyline("left-bank",(6,6),(16,6),(16,14),(20,20),(16,28),(20,34),(18,42))
        bends = [(16,14),(20,20),(16,28),(20,34),(18,42)]
        self.add_polyline("right-bank",(42,6),(32,6),*((x+14,y) for x,y in bends))

"""A folded paper plane pointing upper right. SQUARE extremes (6,6)-(42,42). Lucide send informs the long diagonal fold and triangular wings. Retain the source V-shaped keel, but omit an extra short interior crease to keep the keel open."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '01b94b0f-3616-456d-bf73-a98d07147ec5'
SOURCE_PATH = 'pictographic-primitives/symbol/paper plane_01b94b0f-3616-456d-bf73-a98d07147ec5.svg'
AUTHOR = 'gpt-6'


class PaperPlane(Solo48):
    icon_id = 'paper-plane'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    categories = ("symbol", "state")
    aliases = ()
    keywords = ('paper-plane', 'send', 'message', 'email', 'telegram', 'submit', 'share', 'fly')

    def build(self) -> None:
        self.add_polyline('plane',(6,22),(42,6),(34,40),(24,34),(18,42),(16,28),(6,22),closed=True)
        self.add_line('fold',(42,6),(16,28))
        self.relate('connect','plane','fold')

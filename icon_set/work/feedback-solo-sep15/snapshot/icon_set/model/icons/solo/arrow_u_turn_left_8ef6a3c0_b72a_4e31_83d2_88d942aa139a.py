"""A left-pointing arrow with a tall return loop. SQUARE extremes (6,6)-(42,42). Lucide undo-2 informs tangent shaft and semicircle; direction requires deliberate asymmetry."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8ef6a3c0-b72a-4e31-83d2-88d942aa139a'
SOURCE_PATH = 'pictographic-primitives/symbol/flip arrow_8ef6a3c0-b72a-4e31-83d2-88d942aa139a.svg'
AUTHOR = 'gpt-6'


class ArrowUTurnLeft(Solo48):
    icon_id = 'arrow-u-turn-left'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('undo', 'back', 'u-turn', 'return', 'flip', 'arrow', 'revert', 'left')

    def build(self) -> None:
        self.add_polyline('head', (16,6), (6,16), (16,26))
        self.add_line('shaft', (6,16), (29,16))
        self.add_arc('turn', (29,16), (29,42), radius_x=13)
        self.add_line('return', (29,42), (23,42))
        self.add_contour('body', 'shaft', 'turn', 'return')
        self.relate('connect', 'head', 'body')

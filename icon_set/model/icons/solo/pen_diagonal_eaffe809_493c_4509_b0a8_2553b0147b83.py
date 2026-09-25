"""A diagonal pen with a lower-left nib and curved clip. SQUARE extremes (6,6)-(42,42). Lucide pen informs the broad diagonal barrel and pointed nib. Retain the source clip as one smooth return curve and straight arm, widening barrel and clip spacing."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'eaffe809-493c-4509-b0a8-2553b0147b83'
SOURCE_PATH = 'pictographic-primitives/symbol/pen_eaffe809-493c-4509-b0a8-2553b0147b83.svg'
AUTHOR = 'gpt-6'


class PenDiagonal(Solo48):
    icon_id = 'pen-diagonal'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    categories = ("symbol", "state")
    aliases = ()
    keywords = ('pen', 'write', 'edit', 'ballpoint', 'stationery', 'sign', 'draw', 'note')

    def build(self) -> None:
        self.add_polyline('barrel',(6,42),(10,32),(30,12),(34,8),(42,16),(18,40),(6,42),closed=True)
        self.add_arc('clip-turn',(30,12),(18,12),radius_x=6,sweep=False)
        self.add_line('clip',(18,12),(10,20))
        self.add_contour('clip-outline','clip-turn','clip')
        self.relate('connect','barrel','clip-outline')

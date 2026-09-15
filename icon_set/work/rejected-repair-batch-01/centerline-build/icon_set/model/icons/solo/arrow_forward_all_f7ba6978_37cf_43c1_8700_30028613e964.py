"""A curved forward arrow ends in two chevrons. SQUARE extremes (6,6)-(42,42). Lucide forward: tangent quarter-circle into shaft, repeated arrowheads; directional asymmetry preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f7ba6978-37cf-43c1-8700-30028613e964'
SOURCE_PATH = 'pictographic-primitives/symbol/forward arrow all_f7ba6978-37cf-43c1-8700-30028613e964.svg'
AUTHOR = 'gpt-6'


class ArrowForwardAll(Solo48):
    icon_id = 'arrow-forward-all'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('forward-all', 'forward', 'arrow', 'share', 'email', 'send', 'reply-all', 'redirect')

    def build(self) -> None:
        self.add_line('rise', (6,42), (6,30))
        self.add_arc('bend', (6,30), (20,16), radius_x=14)
        self.add_line('shaft', (20,16), (30,16))
        self.add_contour('body', 'rise', 'bend', 'shaft')
        self.add_polyline('head', (20,6), (30,16), (20,26))
        self.add_polyline('second-head', (32,6), (42,16), (32,26))
        self.relate('connect', 'body', 'head')

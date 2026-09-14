"""An Letters. Retains the complete text and original case with monoline construction.

HRECT_L visible extremes (2, 6, 46, 42), centerlines (4, 8, 44, 40).
Lucide type: coherent monoline letter strokes.
Geometry authored directly on SOLO48. Letter order and directional numerals
retain intentional asymmetry; repeated letters share construction parameters.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '952ce078-e06e-414f-9bfc-1d0ec3a9e267'
SOURCE_PATH = 'pictographic-primitives/symbol/An_952ce078-e06e-414f-9bfc-1d0ec3a9e267.svg'
AUTHOR = 'gpt-6'


class AnLetters(Solo48):
    icon_id = 'an-letters'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'symbols/labels'
    aliases = ()
    keywords = ('an', 'letters', 'text', 'typography', 'abbreviation', 'language', 'alphabet')

    def build(self) -> None:
        self.add_polyline('a-arch', (6, 40), (9, 24), (14, 8), (19, 24), (24, 40))
        self.add_line('a-bar', (9, 24), (19, 24))
        self.relate("connect", 'a-arch', 'a-bar')
        self.add_polyline('n-left', (34, 40), (34, 25), (34, 20))
        self.add_arc('n-arch', (34, 25), (42, 25), radius_x=5, radius_y=5, sweep=True)
        self.add_line('n-right', (42, 25), (42, 40))
        self.add_contour('n-shoulder', 'n-arch', 'n-right')
        self.relate("connect", 'n-left', 'n-shoulder')

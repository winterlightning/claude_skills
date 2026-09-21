"""NEW Text. Stacks NE over W to give the W open, recognizable valleys.

SQUARE visible extremes (4, 4, 44, 44), centerlines (6, 6, 42, 42).
Lucide type: coherent monoline letter strokes.
Geometry authored directly on SOLO48. Letter order and directional numerals
retain intentional asymmetry; repeated letters share construction parameters.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bceaa99b-b0d8-47fc-bb91-5b01dcec3319'
SOURCE_PATH = 'pictographic-primitives/symbol/NEW_bceaa99b-b0d8-47fc-bb91-5b01dcec3319.svg'
AUTHOR = 'gpt-6'


class NewText(Solo48):
    icon_id = 'new-text'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'symbols/labels'
    aliases = ()
    keywords = ('new', 'label', 'badge', 'fresh', 'latest', 'announcement', 'text')

    def build(self) -> None:
        self.add_polyline('n', (6, 22), (6, 6), (20, 22), (20, 6))
        self.add_polyline('e-frame', (42, 6), (30, 6), (30, 14), (30, 22), (42, 22))
        self.add_line('e-bar', (30, 14), (40, 14))
        self.relate("connect", 'e-frame', 'e-bar')
        self.add_polyline('w', (12, 30), (14, 42), (24, 36), (34, 42), (36, 30))

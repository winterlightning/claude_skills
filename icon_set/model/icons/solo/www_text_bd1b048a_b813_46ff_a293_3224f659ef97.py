"""WWW Text. Arranges three matching Ws on two rows to preserve open valleys and the complete WWW text.

SQUARE visible extremes (4, 4, 44, 44), centerlines (6, 6, 42, 42).
Lucide type: coherent monoline letter strokes.
Geometry authored directly on SOLO48. Letter order and directional numerals
retain intentional asymmetry; repeated letters share construction parameters.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bd1b048a-b813-46ff-a293-3224f659ef97'
SOURCE_PATH = 'pictographic-primitives/symbol/WWW_bd1b048a-b813-46ff-a293-3224f659ef97.svg'
AUTHOR = 'gpt-6'


class WwwText(Solo48):
    icon_id = 'www-text'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'symbols/labels'
    aliases = ()
    keywords = ('www', 'web', 'internet', 'website', 'url', 'online', 'text')

    def build(self) -> None:
        self.add_polyline('w-0', (6, 6), (8, 20), (13, 13), (18, 20), (20, 6))
        self.add_polyline('w-1', (28, 6), (30, 20), (35, 13), (40, 20), (42, 6))
        self.add_polyline('w-2', (17, 28), (19, 42), (24, 35), (29, 42), (31, 28))

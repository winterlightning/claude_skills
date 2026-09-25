"""Chain Link. Retains the identifying silhouette and visible features.

SQUARE visible extremes (4, 4, 44, 44); centerlines (6, 6, 42, 42).
Lucide link: opposing open links and rounded outer ends.
Repeated features share dimensions; deliberate asymmetry preserves the
letter order, handles and chart heights. Authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5920d6ee-48e2-4d20-8e91-997b3a3c17c5'
SOURCE_PATH = 'pictographic-primitives/symbol/atttachment_5920d6ee-48e2-4d20-8e91-997b3a3c17c5.svg'
AUTHOR = 'gpt-6'


class ChainLinkDiagonal(Solo48):
    icon_id = 'chain-link-diagonal'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    aliases = ()
    keywords = ('link', 'chain', 'url', 'hyperlink', 'attachment', 'connect', 'web', 'join')

    def build(self) -> None:
        self.add_line('ne-upper', (20, 14), (28, 6))
        self.add_arc('ne-cap', (28, 6), (42, 20), radius_x=14, radius_y=14, sweep=True)
        self.add_line('ne-lower', (42, 20), (34, 28))
        self.add_contour('ne-link', 'ne-upper', 'ne-cap', 'ne-lower')
        self.add_line('sw-lower', (28, 34), (20, 42))
        self.add_arc('sw-cap', (20, 42), (6, 28), radius_x=14, radius_y=14, sweep=True)
        self.add_line('sw-upper', (6, 28), (14, 20))
        self.add_contour('sw-link', 'sw-lower', 'sw-cap', 'sw-upper')
        self.add_line('joining-bar', (18, 30), (30, 18))

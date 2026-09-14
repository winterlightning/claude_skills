""".COM Text. Reflows .C above OM to keep all four characters legible with open spacing.

SQUARE visible extremes (4, 4, 44, 44); centerlines (6, 6, 42, 42).
Supplied reference; no useful exact Lucide match found.
Repeated features share dimensions; deliberate asymmetry preserves the
letter order, handles and chart heights. Authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f505a545-8fb1-4613-8d5a-685942f8d1c6'
SOURCE_PATH = 'pictographic-primitives/symbol/dot com_f505a545-8fb1-4613-8d5a-685942f8d1c6.svg'
AUTHOR = 'gpt-6'


class DotComText(Solo48):
    icon_id = 'dot-com-text'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbols/standalone"
    aliases = ()
    keywords = ('com', 'domain', 'website', 'url', 'internet', 'web', 'text', 'online')

    def build(self) -> None:
        self.add_dot('dot', (6, 18))
        self.add_arc('c-top', (42, 6), (24, 12), radius_x=18, radius_y=6, sweep=False)
        self.add_arc('c-bottom', (24, 12), (42, 18), radius_x=18, radius_y=6, sweep=False)
        self.add_contour('c', 'c-top', 'c-bottom')
        self.add_arc('o-top', (6, 34), (18, 34), radius_x=6, radius_y=6, sweep=True)
        self.add_line('o-right', (18, 34), (18, 36))
        self.add_arc('o-bottom', (18, 36), (6, 36), radius_x=6, radius_y=6, sweep=True)
        self.add_line('o-left', (6, 36), (6, 34))
        self.add_contour('o', 'o-top', 'o-right', 'o-bottom', 'o-left', closed=True)
        self.add_polyline('m', (28, 42), (31, 28), (35, 38), (39, 28), (42, 42))

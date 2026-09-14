"""CSS Text. Retains the complete text and original case with monoline construction.

HRECT_L visible extremes (2, 6, 46, 42), centerlines (4, 8, 44, 40).
Lucide type: coherent monoline letter strokes.
Geometry authored directly on SOLO48. Letter order and directional numerals
retain intentional asymmetry; repeated letters share construction parameters.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4e86ad2e-5a24-449c-8379-d7e832726bb6'
SOURCE_PATH = 'pictographic-primitives/symbol/CSS (text)_4e86ad2e-5a24-449c-8379-d7e832726bb6.svg'
AUTHOR = 'gpt-6'


class CssText(Solo48):
    icon_id = 'css-text'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'symbols/labels'
    aliases = ()
    keywords = ('css', 'code', 'stylesheet', 'web', 'development', 'programming', 'text', 'language')

    def build(self) -> None:
        self.add_line('c-top', (14, 8), (10, 8))
        self.add_arc('c-nw', (10, 8), (6, 14), radius_x=6, radius_y=6, sweep=False)
        self.add_line('c-left', (6, 14), (6, 34))
        self.add_arc('c-sw', (6, 34), (10, 40), radius_x=6, radius_y=6, sweep=False)
        self.add_line('c-bottom', (10, 40), (14, 40))
        self.add_contour('c', 'c-top', 'c-nw', 'c-left', 'c-sw', 'c-bottom')
        self.add_line('s-first-top', (29, 8), (26, 8))
        self.add_arc('s-first-upper', (26, 8), (26, 24), radius_x=3, radius_y=8, sweep=False)
        self.add_arc('s-first-lower', (26, 24), (26, 40), radius_x=3, radius_y=8, sweep=True)
        self.add_line('s-first-foot', (26, 40), (23, 40))
        self.add_contour('s-first', 's-first-top', 's-first-upper', 's-first-lower', 's-first-foot')
        self.add_line('s-second-top', (42, 8), (41, 8))
        self.add_arc('s-second-upper', (41, 8), (41, 24), radius_x=3, radius_y=8, sweep=False)
        self.add_arc('s-second-lower', (41, 24), (41, 40), radius_x=3, radius_y=8, sweep=True)
        self.add_line('s-second-foot', (41, 40), (38, 40))
        self.add_contour('s-second', 's-second-top', 's-second-upper', 's-second-lower', 's-second-foot')

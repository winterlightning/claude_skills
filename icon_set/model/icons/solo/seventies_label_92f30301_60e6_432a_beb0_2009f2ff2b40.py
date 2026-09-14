"""70s Label. Retains the complete text and original case with monoline construction.

HRECT_L visible extremes (2, 6, 46, 42), centerlines (4, 8, 44, 40).
Lucide type: coherent monoline letter strokes.
Geometry authored directly on SOLO48. Letter order and directional numerals
retain intentional asymmetry; repeated letters share construction parameters.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '92f30301-60e6-432a-beb0-2009f2ff2b40'
SOURCE_PATH = 'pictographic-primitives/symbol/70s_92f30301-60e6-432a-beb0-2009f2ff2b40.svg'
AUTHOR = 'gpt-6'


class SeventiesLabel(Solo48):
    icon_id = 'seventies-label'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'symbols/labels'
    aliases = ()
    keywords = ('70s', 'seventies', 'decade', 'retro', 'era', 'vintage', 'label', 'text')

    def build(self) -> None:
        self.add_polyline('seven', (6, 8), (12, 8), (6, 40))
        self.add_arc('zero-top', (21, 12), (29, 12), radius_x=4, radius_y=4, sweep=True)
        self.add_line('zero-right', (29, 12), (29, 36))
        self.add_arc('zero-bottom', (29, 36), (21, 36), radius_x=4, radius_y=4, sweep=True)
        self.add_line('zero-left', (21, 36), (21, 12))
        self.add_contour('zero', 'zero-top', 'zero-right', 'zero-bottom', 'zero-left', closed=True)
        self.add_line('lowercase-s-top', (42, 20), (41, 20))
        self.add_arc('lowercase-s-upper', (41, 20), (41, 30), radius_x=3, radius_y=5, sweep=False)
        self.add_arc('lowercase-s-lower', (41, 30), (41, 40), radius_x=3, radius_y=5, sweep=True)
        self.add_line('lowercase-s-foot', (41, 40), (38, 40))
        self.add_contour('lowercase-s', 'lowercase-s-top', 'lowercase-s-upper', 'lowercase-s-lower', 'lowercase-s-foot')

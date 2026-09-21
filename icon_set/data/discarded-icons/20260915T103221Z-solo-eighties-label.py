"""80s Label. Retains the complete text and original case with monoline construction.

HRECT_L visible extremes (2, 6, 46, 42), centerlines (4, 8, 44, 40).
Lucide type: coherent monoline letter strokes.
Geometry authored directly on SOLO48. Letter order and directional numerals
retain intentional asymmetry; repeated letters share construction parameters.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e6507059-e63e-42cc-bb37-3004dc017157'
SOURCE_PATH = 'pictographic-primitives/symbol/80s_e6507059-e63e-42cc-bb37-3004dc017157.svg'
AUTHOR = 'gpt-6'


class EightiesLabel(Solo48):
    icon_id = 'eighties-label'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'symbols/labels'
    aliases = ()
    keywords = ('80s', 'eighties', 'decade', 'retro', 'era', 'vintage', 'label', 'text')

    def build(self) -> None:
        self.add_arc('eight-upper-right', (8, 8), (8, 24), radius_x=4, radius_y=8, sweep=True)
        self.add_arc('eight-upper-left', (8, 24), (8, 8), radius_x=4, radius_y=8, sweep=True)
        self.add_contour('eight-upper', 'eight-upper-right', 'eight-upper-left', closed=True)
        self.add_arc('eight-lower-right', (8, 24), (8, 40), radius_x=4, radius_y=8, sweep=True)
        self.add_arc('eight-lower-left', (8, 40), (8, 24), radius_x=4, radius_y=8, sweep=True)
        self.add_contour('eight-lower', 'eight-lower-right', 'eight-lower-left', closed=True)
        self.relate("connect", 'eight-upper', 'eight-lower')
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

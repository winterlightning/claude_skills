"""GO Text. Retains the complete text and original case with monoline construction.

HRECT_L visible extremes (2, 6, 46, 42), centerlines (4, 8, 44, 40).
Lucide type: coherent monoline letter strokes.
Geometry authored directly on SOLO48. Letter order and directional numerals
retain intentional asymmetry; repeated letters share construction parameters.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6526c9e6-1222-445f-b7c5-c16580a2e930'
SOURCE_PATH = 'pictographic-primitives/symbol/GO_6526c9e6-1222-445f-b7c5-c16580a2e930.svg'
AUTHOR = 'gpt-6'


class GoText(Solo48):
    icon_id = 'go-text'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'symbols/labels'
    aliases = ()
    keywords = ('go', 'start', 'begin', 'text', 'action', 'proceed', 'letters')

    def build(self) -> None:
        self.add_arc('g-cap', (18, 15), (6, 15), radius_x=7, radius_y=7, sweep=False)
        self.add_line('g-left', (6, 15), (6, 33))
        self.add_arc('g-bottom', (6, 33), (18, 33), radius_x=7, radius_y=7, sweep=False)
        self.add_line('g-bar-1', (18, 33), (18, 25))
        self.add_line('g-bar-2', (18, 25), (12, 25))
        self.add_contour('g', 'g-cap', 'g-left', 'g-bottom', 'g-bar-1', 'g-bar-2')
        self.add_arc('o-top', (28, 16), (42, 16), radius_x=8, radius_y=8, sweep=True)
        self.add_line('o-right', (42, 16), (42, 32))
        self.add_arc('o-bottom', (42, 32), (28, 32), radius_x=8, radius_y=8, sweep=True)
        self.add_line('o-left', (28, 32), (28, 16))
        self.add_contour('o', 'o-top', 'o-right', 'o-bottom', 'o-left', closed=True)

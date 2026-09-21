"""C++ Text. Retains the identifying silhouette and visible features.

HRECT_L visible extremes (2, 6, 46, 42); centerlines (4, 8, 44, 40).
Supplied reference; no useful exact Lucide match found.
Repeated features share dimensions; deliberate asymmetry preserves the
letter order, handles and chart heights. Authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fe40b320-52ca-41ee-9fde-5c659d270f28'
SOURCE_PATH = 'pictographic-primitives/symbol/c++ (text)_fe40b320-52ca-41ee-9fde-5c659d270f28.svg'
AUTHOR = 'gpt-6'


class CppText(Solo48):
    icon_id = 'cpp-text'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbols/standalone"
    aliases = ()
    keywords = ('c++', 'cpp', 'code', 'programming', 'language', 'development', 'text', 'software')

    def build(self) -> None:
        # Envelope repair: shared boundary nodes and cardinal curve extrema;
        # retain the subject, grid, stroke, and declared physical joins.
        self.add_arc('c-upper', (14, 8), (4, 24), radius_x=10, radius_y=16, sweep=False)
        self.add_arc('c-lower', (4, 24), (14, 40), radius_x=10, radius_y=16, sweep=False)
        self.add_contour('c', 'c-upper', 'c-lower')
        self.add_polyline('plus-one-h', (20, 24), (24, 24), (28, 24))
        self.add_polyline('plus-one-v', (24, 20), (24, 24), (24, 28))
        self.relate("connect", 'plus-one-h', 'plus-one-v')
        self.add_polyline('plus-two-h', (36, 24), (40, 24), (44, 24))
        self.add_polyline('plus-two-v', (40, 20), (40, 24), (40, 28))
        self.relate("connect", 'plus-two-h', 'plus-two-v')

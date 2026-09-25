"""Turn Right Arrow. Retains all identifying parts, reconstructed on the integer grid.

HRECT_L visible extremes (2, 6, 46, 42); centerlines (4, 8, 44, 40).
Lucide rotate-cw and undo-2: coherent arcs, open arrowheads and explicit shaft joins.
Mirrored subjects use paired coordinates; directional parts preserve their
intentional asymmetry. Geometry is authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '90bda1dc-4ea8-4d9e-aace-a5784e398b7c'
SOURCE_PATH = 'pictographic-primitives/symbol/arrow turn right_90bda1dc-4ea8-4d9e-aace-a5784e398b7c.svg'
AUTHOR = 'gpt-6'


class ArrowTurnRight(Solo48):
    icon_id = 'arrow-turn-right'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    aliases = ()
    keywords = ('arrow', 'turn', 'right', 'redirect', 'forward', 'curve', 'direction', 'share')

    def build(self) -> None:
        # Envelope repair: shared boundary nodes and cardinal curve extrema;
        # retain the subject, grid, stroke, and declared physical joins.
        self.add_polyline('head', (32, 8), (44, 20), (32, 32))
        self.add_line('shaft', (44, 20), (16, 20))
        self.add_arc('bend', (16, 20), (4, 32), radius_x=12, radius_y=12, sweep=False)
        self.add_line('tail', (4, 32), (12, 40))
        self.add_contour('body', 'shaft', 'bend', 'tail')
        self.relate("connect", 'head', 'body')

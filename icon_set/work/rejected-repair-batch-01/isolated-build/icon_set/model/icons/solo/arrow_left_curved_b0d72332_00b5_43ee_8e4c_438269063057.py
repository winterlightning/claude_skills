"""Curved Left Arrow. Retains all identifying parts, reconstructed on the integer grid.

HRECT_L visible extremes (2, 6, 46, 42); centerlines (4, 8, 44, 40).
Lucide rotate-cw and undo-2: coherent arcs, open arrowheads and explicit shaft joins.
Mirrored subjects use paired coordinates; directional parts preserve their
intentional asymmetry. Geometry is authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b0d72332-00b5-43ee-8e4c-438269063057'
SOURCE_PATH = 'pictographic-primitives/symbol/arrow left curved_b0d72332-00b5-43ee-8e4c-438269063057.svg'
AUTHOR = 'gpt-6'


class ArrowLeftCurved(Solo48):
    icon_id = 'arrow-left-curved'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbols/standalone"
    aliases = ()
    keywords = ('arrow', 'left', 'curved', 'back', 'return', 'undo', 'reply', 'direction')

    def build(self) -> None:
        self.add_polyline('head', (18, 8), (4, 22), (18, 36))
        self.add_line('shaft', (4, 22), (26, 22))
        self.add_arc('bend', (26, 22), (44, 40), radius_x=18, radius_y=18, sweep=True)
        self.add_contour('body', 'shaft', 'bend')
        self.relate("connect", 'head', 'body')

"""Rotate Left 45 Degrees. Keeps 45 below the returning arc and the left-pointing head; widens the open lower side for legibility.

SQUARE visible extremes (4, 4, 44, 44); centerlines (6, 6, 42, 42).
Lucide rotate-cw and undo-2: coherent arcs, open arrowheads and explicit shaft joins.
Mirrored subjects use paired coordinates; directional parts preserve their
intentional asymmetry. Geometry is authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '61588196-4329-4f81-b407-7df1733cde4a'
SOURCE_PATH = 'pictographic-primitives/symbol/arrow rotate left 45_61588196-4329-4f81-b407-7df1733cde4a.svg'
AUTHOR = 'gpt-6'

class RotateLeft45(Solo48):
    icon_id = 'rotate-left-45'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbols/standalone'
    aliases = ()
    keywords = ('rotate', '45', 'degrees', 'left', 'anticlockwise', 'angle', 'turn', 'arrow')

    def build(self) -> None:
        """Use an open-top four with a full-width counter instead of a nearly closed triangular wedge."""
        self.add_polyline('head', (24, 6), (18, 12), (24, 18))
        self.add_line('shaft', (18, 12), (30, 12))
        self.add_arc('bend', (30, 12), (42, 24), radius_x=12, radius_y=12, sweep=True)
        self.add_line('tail', (42, 24), (42, 42))
        self.add_contour('arrow', 'shaft', 'bend', 'tail')
        self.relate('connect', 'head', 'arrow')
        self.add_polyline('four-arm', (6, 26), (6, 36), (14, 36))
        self.add_polyline('four-stem', (14, 26), (14, 36), (14, 42))
        self.relate('connect', 'four-arm', 'four-stem')
        self.add_line('five-cap-1', (33, 26), (25, 26))
        self.add_line('five-cap-2', (25, 26), (25, 34))
        self.add_line('five-cap-3', (25, 34), (29, 34))
        self.add_arc('five-bowl', (29, 34), (29, 42), radius_x=4, radius_y=4, sweep=True)
        self.add_line('five-foot', (29, 42), (25, 42))
        self.add_contour('five', 'five-cap-1', 'five-cap-2', 'five-cap-3', 'five-bowl', 'five-foot')

"""PDF Trefoil Logo. Retains all identifying parts, reconstructed on the integer grid.

SQUARE visible extremes (4, 4, 44, 44); centerlines (6, 6, 42, 42).
No useful Lucide trefoil match; uses the supplied PDF ribbon reference with enlarged loops.
Mirrored subjects use paired coordinates; directional parts preserve their
intentional asymmetry. Geometry is authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e5772ae5-6260-4859-a6ab-c6216f211330'
SOURCE_PATH = 'pictographic-primitives/symbol/adobe_e5772ae5-6260-4859-a6ab-c6216f211330.svg'
AUTHOR = 'gpt-6'


class PdfTrefoilLogo(Solo48):
    icon_id = 'pdf-trefoil-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    categories = ("symbol",)
    aliases = ()
    keywords = ('pdf', 'acrobat', 'document', 'logo', 'trefoil', 'reader', 'file', 'brand')

    def build(self) -> None:
        self.add_polyline('center', (18, 30), (24, 18), (32, 26), closed=True)
        self.add_line('upper-left', (24, 18), (18, 10))
        self.add_arc('upper-cap', (18, 10), (28, 10), radius_x=5, radius_y=4, sweep=True)
        self.add_line('upper-right', (28, 10), (24, 18))
        self.add_contour('upper-loop', 'upper-left', 'upper-cap', 'upper-right', closed=True)
        self.relate("connect", 'center', 'upper-loop')
        self.add_line('lower-left', (18, 30), (10, 42))
        self.add_arc('lower-cap', (10, 42), (6, 38), radius_x=4, radius_y=4, sweep=True)
        self.add_arc('lower-turn', (6, 38), (10, 34), radius_x=4, radius_y=4, sweep=True)
        self.add_line('lower-right', (10, 34), (18, 30))
        self.add_contour('lower-loop', 'lower-left', 'lower-cap', 'lower-turn', 'lower-right', closed=True)
        self.relate("connect", 'center', 'lower-loop')
        self.add_line('right-top', (32, 26), (38, 24))
        self.add_arc('right-cap-top', (38, 24), (42, 28), radius_x=4, radius_y=4, sweep=True)
        self.add_arc('right-cap-bottom', (42, 28), (38, 32), radius_x=4, radius_y=4, sweep=True)
        self.add_line('right-bottom', (38, 32), (32, 26))
        self.add_contour('right-loop', 'right-top', 'right-cap-top', 'right-cap-bottom', 'right-bottom', closed=True)
        self.relate("connect", 'center', 'right-loop')

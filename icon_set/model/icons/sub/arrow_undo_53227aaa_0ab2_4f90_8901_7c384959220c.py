"""Arrow Undo: A curved arrow rises around a broad right-hand bend and ends in a horizontal left-pointing head. Its lower tail starts near the bottom centre and remains open.

Construction: Semicircular return bow tangent to short rails; shared left-facing head tip.
Keyshape: SQUARE; extremes follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '53227aaa-0ab2-4f90-8901-7c384959220c'
SOURCE_PATH = 'pictographic-primitives/state/previous arrow_53227aaa-0ab2-4f90-8901-7c384959220c.svg'
AUTHOR = 'gpt-6'


class ArrowUndo(Sub32):
    icon_id = 'arrow-undo'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = "primitives/mark"
    aliases = ()
    keywords = ('arrow', 'undo', 'curved', 'rises', 'around', 'broad', 'right', 'hand')

    def build(self):
        self.add_line("top",(2,10),(20,10))
        self.add_arc("bow",(20,10),(20,30),radius_x=10)
        self.add_line("tail",(20,30),(16,30))
        self.add_contour("shaft","top","bow","tail")
        self.add_polyline("head",(10,2),(2,10),(10,18))
        self.relate("connect","shaft","head")

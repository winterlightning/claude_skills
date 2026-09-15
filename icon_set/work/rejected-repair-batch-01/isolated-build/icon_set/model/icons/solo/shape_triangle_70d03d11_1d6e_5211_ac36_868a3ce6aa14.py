"""shape-triangle: geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '70d03d11-1d6e-5211-ac36-868a3ce6aa14'
SOURCE_PATH = 'pictographic-primitives/design/shape triangle_70d03d11-1d6e-5211-ac36-868a3ce6aa14.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class ShapeTriangle(Solo48):
    icon_id = 'shape-triangle'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('shape', 'triangle', 'design')

    def build(self):
        # Plan: SQUARE; three straight sides, level baseline and shared axis.
        # Reference: Geometric triangle; remove the extra sagging base vertex.
        self.add_polyline('outline',(24,6),(42,42),(6,42),closed=True)

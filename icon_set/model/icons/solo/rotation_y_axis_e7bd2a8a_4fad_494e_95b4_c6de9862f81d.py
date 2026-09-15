"""rotation-y-axis: geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e7bd2a8a-4fad-494e-95b4-c6de9862f81d'
SOURCE_PATH = 'pictographic-primitives/design/rotation y axis_e7bd2a8a-4fad-494e-95b4-c6de9862f81d.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class RotationYAxis(Solo48):
    icon_id = 'rotation-y-axis'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('rotation', 'y', 'axis', 'design')

    def build(self):
        # Plan: SQUARE; centered axis and one smooth orbital sweep with intentional arrow gap.
        # Reference: Geometric ellipse-like orbit and clean attachment.
        self.add_line('axis',(24,6),(24,42))
        self.add_bezier('left-turn',(14,17),((9,18),(6,21),(6,24)),((6,30),(15,32),(24,32)))
        self.add_bezier('right-turn',(24,32),((33,32),(42,30),(42,24)),((42,20),(38,17),(34,16)))
        self.add_contour('rotation','left-turn','right-turn')
        self.add_polyline('head',(40,15),(34,16),(35,22))
        self.relate('connect','axis','rotation')
        self.relate('connect','head','rotation')

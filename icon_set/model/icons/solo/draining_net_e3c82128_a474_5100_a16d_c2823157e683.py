"""draining-net: geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e3c82128-a474-5100-a16d-c2823157e683'
SOURCE_PATH = 'pictographic-primitives/food/draining net_e3c82128-a474-5100-a16d-c2823157e683.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class DrainingNet(Solo48):
    icon_id = 'draining-net'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('draining', 'net', 'food')

    def build(self):
        # Plan: VRECT_L; matched handle walls and smooth mirrored bowl; remove degenerate tip dots.
        # Reference: Geometric capsule and ellipse with paired shoulders.
        self.add_arc('handle-top',(20,8),(28,8),radius_x=4)
        self.add_line('handle-right',(28,8),(28,22))
        self.add_bezier('neck-right',(28,22),((34,23),(40,27),(40,33)))
        self.add_arc('bowl',(40,33),(8,33),radius_x=16,radius_y=11)
        self.add_bezier('neck-left',(8,33),((8,27),(14,23),(20,22)))
        self.add_line('handle-left',(20,22),(20,8))
        self.add_contour('outline','handle-top','handle-right','neck-right','bowl','neck-left','handle-left',closed=True)

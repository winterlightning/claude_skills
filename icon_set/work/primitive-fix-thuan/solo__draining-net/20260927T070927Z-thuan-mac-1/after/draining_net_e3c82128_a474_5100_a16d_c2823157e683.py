"""draining-net: geometric reconstruction on SOLO48."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'e3c82128-a474-5100-a16d-c2823157e683'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__draining-net/20260927T070927Z-thuan-mac-1/reference/draining net_e3c82128-a474-5100-a16d-c2823157e683.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class DrainingNet(Solo48):
    icon_id = 'draining-net'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('draining', 'net', 'food')

    def build(self):
        # Plan: VRECT_L; matched handle walls and smooth mirrored bowl; remove degenerate tip dots.
        # Reference: Geometric capsule and ellipse with paired shoulders.
        self.add_arc('handle-top',(20,8),(28,8),radius_x=4)
        self.add_line('handle-right',(28,8),(28,20))
        self.add_bezier('neck-right',(28,20),((34,21),(38,26),(38,32)))
        self.add_arc('bowl',(38,32),(10,32),radius_x=14,radius_y=12)
        self.add_bezier('neck-left',(10,32),((10,26),(14,21),(20,20)))
        self.add_line('handle-left',(20,20),(20,8))
        self.add_contour('outline','handle-top','handle-right','neck-right','bowl','neck-left','handle-left',closed=True)

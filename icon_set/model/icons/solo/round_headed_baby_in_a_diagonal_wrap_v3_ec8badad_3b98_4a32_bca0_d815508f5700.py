"""Independent full icon-solo drawing from the original batch-04 brief."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ec8badad-3b98-4a32-bca0-d815508f5700'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_05/baby hold hands_ec8badad-3b98-4a32-bca0-d815508f5700.svg'
AUTHOR = 'gpt-6'


class IndependentSolo(Solo48):
    icon_id = 'round-headed-baby-in-a-diagonal-wrap-v3'
    variant_of = 'round-headed-baby-in-a-diagonal-wrap'
    variant_label = 'Independent icon-solo; original reference only'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('round', 'headed', 'baby', 'in', 'a', 'diagonal', 'wrap')

    def build(self):
        # Plan: circular exposed head, shared side junctions, diagonal blanket edge.
        # VRECT_M extremes (10,4)-(38,44). The wrap contacts the head, not a detached bust.
        # Shared human_ref/user.svg circular anatomy; no eyes or fingers at this scale.
        self.add_arc('head-top',(10,18),(38,18),radius_x=14)
        self.add_arc('head-bottom-right',(38,18),(24,32),radius_x=14)
        self.add_arc('head-bottom-left',(24,32),(10,18),radius_x=14)
        self.add_contour('head','head-top','head-bottom-right','head-bottom-left',closed=True)
        self.add_line('wrap-right',(38,18),(38,30))
        self.add_bezier('wrap-bottom-right',(38,30),((38,38),(32,44),(24,44)),((18,44),(14,41),(12,38)))
        self.add_bezier('wrap-bottom-left',(12,38),((10,35),(10,33),(10,30)))
        self.add_line('wrap-left',(10,30),(10,18))
        self.add_contour('wrap','wrap-right','wrap-bottom-right','wrap-bottom-left','wrap-left')
        self.relate('connect','head','wrap')
        self.add_line('fold',(12,38),(24,32))
        self.relate('connect','fold','head')
        self.relate('connect','fold','wrap')

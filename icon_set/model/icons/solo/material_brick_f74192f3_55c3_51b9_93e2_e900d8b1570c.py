"""material-brick: reviewed and repaired in place on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f74192f3-55c3-51b9-93e2-e900d8b1570c'
SOURCE_PATH = 'pictographic-primitives/construction/material brick_f74192f3-55c3-51b9-93e2-e900d8b1570c.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-repaired'

class MaterialBrick(Solo48):
    icon_id = 'material-brick'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'construction'
    categories = ('construction', 'primitives')
    aliases = ()
    keywords = ('material', 'brick', 'construction')

    def build(self):
        # HRECT_L (4,8)-(44,40); rebuild all brick joints without duplicate relationships.
        # Construction reference: Lucide shapes: clean shared edges; source supplies staggered courses
        # Three staggered courses, shared horizontal joints and integer spacing.
        self.add_polyline('middle',(4,19),(44,19),(44,29),(4,29),closed=True)
        self.add_polyline('top',(9,19),(9,8),(39,8),(39,19))
        self.add_polyline('bottom',(9,29),(9,40),(39,40),(39,29))
        for name,x,y1,y2 in [('top-joint',24,8,19),('bottom-joint',24,29,40),('mid-left',17,19,29),('mid-right',31,19,29)]:
            self.add_line(name,(x,y1),(x,y2))
            self.relate('connect',name,'middle')
            if name=='top-joint':self.relate('connect',name,'top')
            if name=='bottom-joint':self.relate('connect',name,'bottom')
        self.relate('connect','middle','top')
        self.relate('connect','middle','bottom')

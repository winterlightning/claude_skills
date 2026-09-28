"""Permafrost: six-arm snowflake in a tall rounded frame. VRECT_L centerlines8,4,40,44; nine-unit border gaps. Tall shape separates the true branch nodes."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '3f77b04c-ad63-443d-a816-599e467435a6'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__permafrost/20260927T143814Z-thuan-mac-1/reference/permafrost_3f77b04c-ad63-443d-a816-599e467435a6.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'permafrost'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ()
    # Keyshape chosen first; stroke centerlines inset 2 from the ink bounds.
    chosen_bounds = Keyshape.VRECT_L.bounds_for(Profile.SOLO48)
    def build(self):
        # Six arms and paired crystalline forks, following the reference snowflake.
        self.add_polyline('vertical',(24,6),(24,15),(24,24),(24,33),(24,42))
        self.add_polyline('diag-a',(6,14),(16,19),(24,24),(32,29),(42,34))
        self.add_polyline('diag-b',(6,34),(16,29),(24,24),(32,19),(42,14))
        self.relate('connect','vertical','diag-a')
        self.relate('connect','vertical','diag-b')
        self.relate('connect','diag-a','diag-b')
        self.add_polyline('top-fork',(19,10),(24,15),(29,10))
        self.add_polyline('bottom-fork',(19,38),(24,33),(29,38))
        self.relate('connect','top-fork','vertical')
        self.relate('connect','bottom-fork','vertical')

# Revision comparison: The rejected snowflake looked like a small sprig in a frame.
# Revision: Redrew it as a large six-arm snowflake with paired vertical branches.

"""EventBridge: four circular nodes around a hexagonal event bus. Square ink extremes 4,4,44,44."""
from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
from ._base import Solo48
SOURCE_ICON_ID = '34f87da9-e584-47f7-8fe0-ca66e9aa7da9'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_02/amazon eventbridge_34f87da9-e584-47f7-8fe0-ca66e9aa7da9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'amazon-eventbridge'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ()
    # Keyshape chosen first; stroke centerlines inset 2 from the ink bounds.
    chosen_bounds = Keyshape.SQUARE.bounds_for(Profile.SOLO48)
    def build(self):
        # Four repeated nodes, interrupted perimeter, nested central event bus.
        self.add_polyline('upper',(17,9),(32,9),(39,13))
        self.add_polyline('right',(42,16),(42,24),(34,36))
        self.add_polyline('lower',(31,39),(16,39),(9,35))
        self.add_polyline('left',(6,32),(6,24),(14,12))
        self.add_polyline('event-bus',(21,18),(27,18),(30,24),(27,30),(21,30),(18,24),closed=True)
        self.add_arc('top-a',(11,9),(17,9),radius_x=3)
        self.add_arc('top-b',(17,9),(11,9),radius_x=3)
        self.add_contour('top','top-a','top-b',closed=True)
        self.add_arc('right-node-a',(36,16),(42,16),radius_x=3)
        self.add_arc('right-node-b',(42,16),(36,16),radius_x=3)
        self.add_contour('right-node','right-node-a','right-node-b',closed=True)
        self.add_arc('bottom-a',(31,39),(37,39),radius_x=3)
        self.add_arc('bottom-b',(37,39),(31,39),radius_x=3)
        self.add_contour('bottom','bottom-a','bottom-b',closed=True)
        self.add_arc('left-node-a',(6,32),(12,32),radius_x=3)
        self.add_arc('left-node-b',(12,32),(6,32),radius_x=3)
        self.add_contour('left-node','left-node-a','left-node-b',closed=True)
        self.relate('connect','upper','top')
        self.relate('connect','upper','right-node')
        self.relate('connect','right','right-node')
        self.relate('connect','right','bottom')
        self.relate('connect','lower','bottom')
        self.relate('connect','lower','left-node')
        self.relate('connect','left','left-node')
        self.relate('connect','left','top')

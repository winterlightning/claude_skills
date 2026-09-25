"""Complete source composition; see the accompanying visual and validation evidence."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.sub._base import Sub32
SOURCE_ICON_ID = '05032593-c317-46fb-9187-d42561ffa0d2'
SOURCE_PATH = 'pictographic-primitives/state/circle thumbs up_05032593-c317-46fb-9187-d42561ffa0d2.svg'
AUTHOR = 'gpt-6'
REFERENCE_PARTS = ('circular frame', 'continuous raised-thumb silhouette', 'left wrist edge without an added cuff divider')

class Drawing(Sub32):
    variant_of = 'circle-thumbs-up-sub32'
    variant_label = 'Uniform 4px readability repair'
    REPAIR_PLAN = {'concept': 'Thumbs Up Approval Symbol', 'core_parts': ['circular frame', 'continuous raised-thumb silhouette', 'left wrist edge without an added cuff divider'], 'flexible_parts': 'Coordinates and proportions only; no parts removed.', 'repair': 'Bring the complete hand inward so its wrist and palm separate from the circle.'}
    icon_id = 'circle-thumbs-up-sub32-v2'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    keywords = ('thumbs', 'up', 'approval', 'symbol')

    def build(self):
        self.circle('frame', 16, 16, 14)
        self.add_line('wrist', (10, 16), (10, 21))
        self.add_bezier('palm', (10, 21), ((12, 21), (12, 22), (15, 22)), ((17, 22), (18, 22), (19, 22)), ((21, 22), (21, 20), (22, 19)), ((23, 16), (23, 15), (21, 15)))
        self.add_line('fingers', (21, 15), (17, 15))
        self.add_bezier('thumb', (17, 15), ((18, 13), (19, 11), (18, 9)), ((17, 7), (16, 10), (15, 12)), ((13, 15), (12, 16), (10, 16)))
        self.add_contour('hand', 'wrist', 'palm', 'fingers', 'thumb', closed=True)

    def circle(self, name, cx, cy, r):
        self.add_arc(name + '-top', (cx - r, cy), (cx + r, cy), radius_x=r)
        self.add_arc(name + '-bottom', (cx + r, cy), (cx - r, cy), radius_x=r)
        self.add_contour(name, name + '-top', name + '-bottom', closed=True)

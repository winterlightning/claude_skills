"""Complete source composition; see the accompanying visual and validation evidence."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.sub._base import Sub32
SOURCE_ICON_ID = '2a3f04f0-a404-41db-90b7-a6ee5813413b'
SOURCE_PATH = 'pictographic-primitives/symbol/messages bubble round heart_2a3f04f0-a404-41db-90b7-a6ee5813413b.svg'
AUTHOR = 'gpt-6'
REFERENCE_PARTS = ('oval speech bubble', 'lower-left pointed tail', 'outlined heart')

class Drawing(Sub32):
    variant_of = 'heart-speech-bubble-sub32'
    variant_label = 'Uniform 4px readability repair'
    REPAIR_PLAN = {'concept': 'Heart Speech Bubble', 'core_parts': ['oval speech bubble', 'lower-left pointed tail', 'outlined heart'], 'flexible_parts': 'Coordinates and proportions only; no parts removed.', 'repair': 'Smaller centered heart leaves more clearance inside the complete speech bubble.'}
    icon_id = 'heart-speech-bubble-sub32-v2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    keywords = ('heart', 'speech', 'bubble')

    def build(self):
        self.add_bezier('bubble-top', (7, 23), ((4, 21), (2, 18), (2, 15)), ((2, 8), (8, 2), (16, 2)), ((24, 2), (30, 8), (30, 15)), ((30, 22), (23, 26), (16, 26)), ((14, 26), (12, 26), (11, 25)))
        self.add_line('tail-1', (11, 25), (4, 30))
        self.add_line('tail-2', (4, 30), (7, 23))
        self.add_contour('frame', 'bubble-top', 'tail-1', 'tail-2', closed=True)
        self.add_bezier('heart', (16, 11), ((12, 7), (8, 11), (11, 14)), ((13, 16), (14, 17), (16, 19)), ((18, 17), (19, 16), (21, 14)), ((24, 11), (20, 7), (16, 11)))

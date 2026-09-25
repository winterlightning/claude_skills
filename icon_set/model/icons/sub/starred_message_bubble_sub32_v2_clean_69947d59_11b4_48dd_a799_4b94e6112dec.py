"""Uniform 4px complete-composition repair candidate; strict findings are retained."""
from ...keyshapes import Keyshape
from ._base import Sub32
from ...primitives import Bezier, Point
SOURCE_ICON_ID = '69947d59-11b4-48dd-a799-4b94e6112dec'
SOURCE_PATH = 'pictographic-primitives/messages/messages bubble square star_69947d59-11b4-48dd-a799-4b94e6112dec.svg'
AUTHOR = 'gpt-6'
REFERENCE_PARTS = ('rounded rectangular speech bubble', 'lower-left downward tail', 'outlined five-point star')
class Drawing(Sub32):
    icon_id = 'starred-message-bubble-sub32-v2-clean'
    variant_of = 'starred-message-bubble-sub32-v2'
    variant_label = 'Complete 4px cleanup'
    REPAIR_PLAN = {'concept': 'Starred Message Bubble', 'core_parts': ('rounded rectangular speech bubble', 'lower-left downward tail', 'outlined five-point star'), 'flexible_parts': 'Coordinates and proportions only; no original elements removed.', 'repair': 'Deepen the bubble and rebalance the five star points around a larger central opening.'}
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'messages'
    TYPEFACE_GLYPH_IDS = ()
    def build(self):
        self.message()
        self.add_polyline('star',(16,9),(18,11),(22,12),(19,15),(20,19),(16,17),(12,19),(13,15),(10,12),(14,11),closed=True)

    def message(self):
        self.add_line('frame-top',(4,2),(28,2))
        self.add_arc('frame-tr',(28,2),(30,4),radius_x=2)
        self.add_line('frame-right',(30,4),(30,25))
        self.add_arc('frame-br',(30,25),(28,27),radius_x=2)
        tail=[(28,27),(15,27),(9,30),(9,27),(4,27)]
        for i,(a,b) in enumerate(zip(tail,tail[1:]),1):self.add_line(f'frame-tail-{i}',a,b)
        self.add_arc('frame-bl',(4,27),(2,25),radius_x=2)
        self.add_line('frame-left',(2,25),(2,4))
        self.add_arc('frame-tl',(2,4),(4,2),radius_x=2)
        self.add_contour('frame','frame-top','frame-tr','frame-right','frame-br',*[f'frame-tail-{i}' for i in range(1,5)],'frame-bl','frame-left','frame-tl',closed=True)


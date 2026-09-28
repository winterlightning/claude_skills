"""Comment Bubble. Retains the identifying silhouette and visible features.

SQUARE visible extremes (4, 4, 44, 44); centerlines (6, 6, 42, 42).
Lucide message-square, inspected in batch 05: rounded perimeter and integrated tail; source sets the right-side tail and two text strokes.
Repeated features share dimensions; deliberate asymmetry preserves the
letter order, handles and chart heights. Authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '38cf6077-62d9-4591-96af-055f6c16edaf'
SOURCE_PATH = 'pictographic-primitives/symbol/comment 1_38cf6077-62d9-4591-96af-055f6c16edaf.svg'
AUTHOR = 'gpt-6'


class CommentBubbleTailRight(Solo48):
    icon_id = 'comment-bubble-tail-right'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    categories = ("symbol", "state")
    aliases = ()
    keywords = ('comment', 'chat', 'message', 'bubble', 'speech', 'text', 'conversation', 'reply')

    def build(self) -> None:
        self.add_line('top', (12, 6), (36, 6))
        self.add_arc('ne', (36, 6), (42, 12), radius_x=6, radius_y=6, sweep=True)
        self.add_line('right', (42, 12), (42, 30))
        self.add_arc('se', (42, 30), (36, 36), radius_x=6, radius_y=6, sweep=True)
        self.add_line('tail-1', (36, 36), (34, 36))
        self.add_line('tail-2', (34, 36), (34, 42))
        self.add_line('tail-3', (34, 42), (24, 36))
        self.add_line('tail-4', (24, 36), (12, 36))
        self.add_arc('sw', (12, 36), (6, 30), radius_x=6, radius_y=6, sweep=True)
        self.add_line('left', (6, 30), (6, 12))
        self.add_arc('nw', (6, 12), (12, 6), radius_x=6, radius_y=6, sweep=True)
        self.add_contour('bubble', 'top', 'ne', 'right', 'se', 'tail-1', 'tail-2', 'tail-3', 'tail-4', 'sw', 'left', 'nw', closed=True)
        self.add_line('text-one', (16, 16), (32, 16))
        self.add_line('text-two', (16, 25), (26, 25))

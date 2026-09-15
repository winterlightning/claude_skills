"""A text-message bubble with two equal text lines. HRECT_L centerline extremes (6,8)-(42,40). Lucide message-square-text informs the rounded rectangular outline and integrated pointed tail; retain the source two equal intrinsic text lines. Tail deliberately offsets left."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '34fbe308-bfd8-435f-929c-a1fdf524e16c'
SOURCE_PATH = 'pictographic-primitives/symbol/message lines_34fbe308-bfd8-435f-929c-a1fdf524e16c.svg'
AUTHOR = 'gpt-6'


class MessageBubbleLines(Solo48):
    icon_id = 'message-bubble-lines'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('message', 'chat', 'bubble', 'comment', 'text', 'conversation', 'speech', 'sms')

    def build(self) -> None:
        # Preserve interior detail sizes; move only the outer edge bands to the exact envelope.
        # Curves reaching an edge use bounded cubic controls, with shared endpoints retained.
        self.add_line('top',(6, 8),(42, 8))
        self.add_bezier('tr',(42, 8),*(((43.27421534, 8.80131331), (44, 10.3837142), (44, 12)),))
        self.add_line('right',(44, 12),(44, 30))
        self.add_bezier('br',(44, 30),*(((44, 31.6162858), (43.27421534, 33.19868669), (42, 34)),))
        self.add_line('bottom',(42, 34),(22, 34))
        self.add_line('tail-right',(22, 34),(12, 40))
        self.add_line('tail-left',(12, 40),(12, 34))
        self.add_line('bottom-left',(12, 34),(6, 34))
        self.add_bezier('bl',(6, 34),*(((4.72578466, 33.19868669), (4, 31.6162858), (4, 30)),))
        self.add_line('left',(4, 30),(4, 12))
        self.add_bezier('tl',(4, 12),*(((4, 10.3837142), (4.72578466, 8.80131331), (6, 8)),))
        self.add_line('text-top',(14, 17),(34, 17))
        self.add_line('text-bottom',(14, 25),(34, 25))
        self.add_contour('bubble',*('top', 'tr', 'right', 'br', 'bottom', 'tail-right', 'tail-left', 'bottom-left', 'bl', 'left', 'tl'),closed=True)

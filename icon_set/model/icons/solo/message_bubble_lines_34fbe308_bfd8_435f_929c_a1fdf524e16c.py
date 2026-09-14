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
        self.add_line('top',(8,8),(40,8))
        self.add_arc('tr',(40,8),(42,12),radius_x=4)
        self.add_line('right',(42,12),(42,30))
        self.add_arc('br',(42,30),(40,34),radius_x=4)
        self.add_line('bottom',(40,34),(22,34))
        self.add_line('tail-right',(22,34),(12,40))
        self.add_line('tail-left',(12,40),(12,34))
        self.add_line('bottom-left',(12,34),(8,34))
        self.add_arc('bl',(8,34),(6,30),radius_x=4)
        self.add_line('left',(6,30),(6,12))
        self.add_arc('tl',(6,12),(8,8),radius_x=4)
        self.add_contour('bubble','top','tr','right','br','bottom','tail-right','tail-left','bottom-left','bl','left','tl',closed=True)
        self.add_line('text-top',(14,17),(34,17))
        self.add_line('text-bottom',(14,25),(34,25))

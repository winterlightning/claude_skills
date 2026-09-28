"""question mark in chat bubble. Revision of reviewer feedback: Bad stroke drawn.
Plan: Round speech bubble with a lower-left tail and enlarged clear question mark. Square6..42. Symmetric round main balloon; directional tail.
Construction reference: Lucide message-circle-question-mark: round balloon with a clear hook and detached dot.
Omissions: None
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='1af2cc96-98e1-4c11-bd26-fef6f9c101b4'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__question-mark-chat-bubble-solo/20260927T144036Z-thuan-mac-1/reference/question mark in chat bubble_1af2cc96-98e1-4c11-bd26-fef6f9c101b4.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'question-mark-chat-bubble-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    categories = ('symbol', 'state')
    aliases = ()
    keywords = ('question', 'mark', 'in', 'chat', 'bubble')
    def build(self):
        # Circular chat bubble with a left tail; question mark has a broad crown.
        self.add_bezier('upper-left',(6,24),((6,14),(14,6),(24,6)))
        self.add_bezier('upper-right',(24,6),((34,6),(42,14),(42,24)))
        self.add_bezier('lower-right',(42,24),((42,34),(34,42),(24,42)),((22,42),(20,42),(18,41)))
        self.add_line('tail-bottom',(18,41),(6,42))
        self.add_line('tail-left',(6,42),(10,34))
        self.add_bezier('lower-left',(10,34),((7,31),(6,28),(6,24)))
        self.add_contour('bubble','upper-left','upper-right','lower-right','tail-bottom','tail-left','lower-left',closed=True)
        self.add_bezier('question-crown',(17,19),((17,13),(31,13),(31,19)))
        self.add_line('question-turn',(31,19),(24,24))
        self.add_contour('question','question-crown','question-turn')
        self.add_dot('question-dot',(24,33))


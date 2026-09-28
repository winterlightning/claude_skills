"""book-open-b5768591: next fifty AI review; original preserved."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'b5768591-30d0-458a-8f42-f8fa19890c4e'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__book-open-b5768591/20260926T073831Z-thuan-mac/reference/book open_b5768591-30d0-458a-8f42-f8fa19890c4e.svg'
AUTHOR = "claude-opus-5-5"

class BookOpenB5768591(Solo48):
    icon_id = 'book-open-b5768591'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'content'
    categories = ('primitives', 'content')
    aliases = ()
    keywords = ('book', 'open', 'content', 'solo-ai-next50')

    def build(self):
        # Revision per review: the book is taller (SQUARE 36 x 36, was 40 x 32) and drawn as one
        # empty outline with no inner lines. Each top edge is a cubic that rises from the outer
        # corner (6, 10)/(42, 10) to y 6 and dips into the spine (24, 10) (equal control heights,
        # so its top is exactly 6); the sides run straight down to (6, 38)/(42, 38); each bottom
        # edge curves gently down to the spine point (24, 42). A straight-edged version read as a
        # shield.
        c = 14 / 3
        self.add_bezier('top-left', (6, 10), ((10, c), (22, c), (24, 10)))
        self.add_bezier('top-right', (24, 10), ((26, c), (38, c), (42, 10)))
        self.add_line('side-right', (42, 10), (42, 38))
        self.add_bezier('bottom-right', (42, 38), ((36, 39), (28, 40), (24, 42)))
        self.add_bezier('bottom-left', (24, 42), ((20, 40), (12, 39), (6, 38)))
        self.add_line('side-left', (6, 38), (6, 10))
        self.add_contour('book', 'top-left', 'top-right', 'side-right', 'bottom-right', 'bottom-left', 'side-left',
                         closed=True)

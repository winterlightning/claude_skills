"""A happy face reading an open book held in front of its chin.

Plan: SQUARE (6,6)-(42,42). The head is a circle of radius 14 about (28,20): two true quarter arcs over the top from (14,20) to (42,20), a cubic from the right point down to the book's top-right corner (30,32), and a straight cheek line from (14,20) down to (14,32) where it meets the left page's top edge. The open book is a closed outline with a V-shaped top edge, (6,30)-(14,32)-(18,34)-(30,32)-(30,42)-(6,42), and a spine from (18,34) to (18,42); the face outline ends on its nodes so the book reads as held in front of the face. Dot eyes at (23,17)/(33,17).
Review of the rejected drawing: the head was a dome sitting on a flat book with two arches, so it read as a helmet or a jar lid; the original shows a round face whose lower part is hidden by an open book.
Omissions: the smile (no 8-unit room between the eyes and the book edge) and the hand on the book's right page; the closed-eye arches become dots.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '35d8adfa-635c-4306-8acd-147f2e6dbc87'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__smiling-face-holding-open-book/20260928T042731Z-thuan-mac-1/reference/emoji reading lover hug_35d8adfa-635c-4306-8acd-147f2e6dbc87.svg'
AUTHOR = "claude-fable-5-1"


class SmilingFaceHoldingOpenBook(Solo48):
    icon_id = 'smiling-face-holding-open-book'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ('happy-face-reading-a-book', 'reading-lover')
    keywords = ('emoji', 'reading', 'book', 'lover', 'happy', 'face', 'read')

    def build(self) -> None:
        # head: r14 circle about (28,20); cheek line down to the left page, jaw cubic down to the book corner
        self.add_line('cheek', (14, 32), (14, 20))
        self.add_arc('crown-left', (14, 20), (28, 6), radius_x=14, sweep=True)
        self.add_arc('crown-right', (28, 6), (42, 20), radius_x=14, sweep=True)
        self.add_bezier('jaw', (42, 20), ((42, 27), (36, 32), (30, 32)))
        self.add_contour('head', 'cheek', 'crown-left', 'crown-right', 'jaw')
        # open book: V-shaped top edge, split where the cheek meets the left page
        self.add_line('page-left-top-a', (6, 30), (14, 32))
        self.add_line('page-left-top-b', (14, 32), (18, 34))
        self.add_line('page-right-top', (18, 34), (30, 32))
        self.add_line('book-right', (30, 32), (30, 42))
        self.add_line('book-bottom-right', (30, 42), (18, 42))
        self.add_line('book-bottom-left', (18, 42), (6, 42))
        self.add_line('book-left', (6, 42), (6, 30))
        self.add_contour('book', 'page-left-top-a', 'page-left-top-b', 'page-right-top', 'book-right',
                         'book-bottom-right', 'book-bottom-left', 'book-left', closed=True)
        self.add_line('spine', (18, 34), (18, 42))
        self.relate('connect', 'spine', 'book')
        self.relate('connect', 'head', 'book')
        self.add_dot('eye-left', (23, 17))
        self.add_dot('eye-right', (33, 17))

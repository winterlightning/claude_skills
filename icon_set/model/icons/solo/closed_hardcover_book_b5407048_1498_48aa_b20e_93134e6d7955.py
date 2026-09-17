"""Closed Hardcover Book.

Plan: Tall closed book with a shallow concave page edge, r6 spine rounds. Centerline bounds (8,4)-(40,44).
Construction: Lucide book: rounded spine and page-block seam; keep the source page block at the upper edge.
Reduction: Preserve the complete single subject; no unrelated detail added.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b5407048-1498-48aa-b20e-93134e6d7955'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/container/Book 1_b5407048-1498-48aa-b20e-93134e6d7955.svg'
AUTHOR = "gpt-6"

class Batch02Icon2(Solo48):
    icon_id = 'closed-hardcover-book-b5407048'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/book"
    aliases = ('closed-hardcover-book',)
    keywords = ('closed', 'hardcover', 'book')

    def build(self):
        def path(name, start, commands, closed=False):
            here = start
            members = []
            for i, (kind, end, *args) in enumerate(commands):
                member = f"{name}-{i}"
                if kind == "L": self.add_line(member, here, end)
                elif kind == "A": self.add_arc(member, here, end, radius_x=args[0], radius_y=args[1], sweep=args[2])
                elif kind == "C": self.add_bezier(member, here, (args[0], args[1], end))
                members.append(member)
                here = end
            self.add_contour(name, *members, closed=closed)
        path("cover",(14,4),[("L",(40,4)),("C",(40,16),(36,8),(36,12)),("L",(40,44)),("L",(14,44)),("A",(8,38),6,6,True),("L",(8,10)),("A",(14,4),6,6,True)],True)
        path("pages",(8,10),[("A",(14,16),6,6,False),("L",(40,16))])
        self.relate("connect","cover","pages")

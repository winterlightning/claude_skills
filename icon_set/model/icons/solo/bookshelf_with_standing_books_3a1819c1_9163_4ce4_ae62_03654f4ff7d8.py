"""Bookshelf with Standing Books.

Plan: Square cabinet x6..42, shelf y24; one upper book and two adjacent lower books use shared 8-unit width.
Construction: Lucide library: parallel upright book spines.
Reduction: Squared cabinet corners keep book clearances exact.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3a1819c1-9163-4ce4-ae62-03654f4ff7d8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-002/references/06-3a1819c1-9163-4ce4-ae62-03654f4ff7d8.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'bookshelf-with-standing-books'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('bookshelf', 'with', 'standing', 'books')

    def build(self):

        def path(name, start, commands, closed=False):
            here = start
            members = []
            for index, (kind, end, *args) in enumerate(commands):
                member = f"{name}-{index}"
                if kind == 'L': self.add_line(member, here, end)
                elif kind == 'A': self.add_arc(member, here, end, radius_x=args[0], radius_y=args[1], sweep=args[2])
                elif kind == 'C': self.add_bezier(member, here, (args[0], args[1], end))
                members.append(member)
                here = end
            self.add_contour(name, *members, closed=closed)
        def circle(name, x, y, r):
            path(name, (x-r,y), [('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)], True)
        def rect(name, x, y, w, h, r=0):
            if not r:
                self.add_polyline(name, (x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True)
            else:
                path(name,(x+r,y),[('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)
        def line(name, a, b): self.add_line(name,a,b)
        def poly(name, *points, closed=False): self.add_polyline(name,*points,closed=closed)
        def join(a,b): self.relate('connect',a,b)
        rect('cabinet',6,6,36,36)
        line('shelf',(6,24),(42,24));join('shelf','cabinet')
        poly('upper-book',(14,24),(14,14),(22,14),(22,24));join('upper-book','shelf')
        poly('lower-books',(26,42),(26,32),(34,32),(42,32));join('lower-books','cabinet')
        line('lower-spine',(34,32),(34,42));join('lower-spine','lower-books');join('lower-spine','cabinet')

"""Book with Bookmark.

Plan: Rounded book x8..40, top page band 8 high, bottom forked ribbon reaching y44.
Construction: Lucide book: long cover and rounded page spine.
Reduction: No page-line texture.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e3ce9c51-448a-4bbb-bb83-f2712afce608'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-002/references/05-e3ce9c51-448a-4bbb-bb83-f2712afce608.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'closed-book-with-ribbon-bookmark'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('closed', 'book', 'with', 'ribbon', 'bookmark')

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
        path('cover',(12,4),[('L',(40,4)),('L',(40,34)),('L',(12,34)),('A',(8,30),4,4,True),('L',(8,8)),('A',(12,4),4,4,True)],True)
        path('pages',(8,8),[('A',(12,12),4,4,False),('L',(40,12))]);join('cover','pages')
        poly('bookmark',(22,34),(22,44),(28,40),(34,44),(34,34));join('cover','bookmark')

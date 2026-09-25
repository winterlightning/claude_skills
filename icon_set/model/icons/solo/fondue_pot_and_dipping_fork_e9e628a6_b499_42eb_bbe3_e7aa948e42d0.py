"""Fondue Pot with Dipping Fork.

Plan: Bowl on two splayed legs; dipping fork above it carries a rounded food piece. Bounds (6,6)-(42,42).
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Removed tiny flame, dripping strand, and stand crossbar to retain a clear bowl, stand and dipping fork.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e9e628a6-b499-42eb-bbe3-e7aa948e42d0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-005/references/03-e9e628a6-b499-42eb-bbe3-e7aa948e42d0.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'fondue-pot-and-dipping-fork'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('fondue', 'pot', 'and', 'dipping', 'fork')

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
        path('bowl',(6,23),[('L',(42,23)),('A',(30,35),12,12,True),('L',(18,35)),('A',(6,23),12,12,True)],True)
        line('left-leg',(18,35),(14,42));line('right-leg',(30,35),(34,42))
        join('bowl','left-leg');join('bowl','right-leg')
        rect('food',20,6,10,8,4)
        line('fork',(30,10),(42,6));join('food','fork')

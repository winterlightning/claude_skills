"""Suit with Bow Tie.

Plan: Formal suit with central bow tie and long V lapels; bounds (6,6)-(42,42).
Construction: Lucide shirt informs broad garment outline; source bow and V lapels define the formal suit.
Reduction: No shirt buttons; bow crossing remains integral to suit.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2487ed91-55b8-44a8-a6e9-f9630de162fe'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-014/references/48-2487ed91-55b8-44a8-a6e9-f9630de162fe.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'bow-tie-suit'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('bow', 'tie', 'suit')

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
        poly('bow',(14,6),(24,12),(34,6),(34,18),(24,12),(14,18),closed=True)
        poly('left-lapel',(14,18),(24,34),(34,18));join('bow','left-lapel')
        path('left-jacket',(14,18),[('L',(6,22)),('L',(12,42))]);path('right-jacket',(34,18),[('L',(42,22)),('L',(36,42))]);join('bow','left-jacket');join('bow','right-jacket')
        line('seam',(24,34),(24,42));join('left-lapel','seam')

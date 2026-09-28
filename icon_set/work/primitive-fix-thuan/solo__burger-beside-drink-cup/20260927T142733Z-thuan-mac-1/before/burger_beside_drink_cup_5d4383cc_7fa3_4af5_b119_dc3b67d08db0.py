"""Burger and Soda with Straw.

Plan: Tapering cup at left, short straw above and burger in front-right; x6..42 y6..42.
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Cup straw ends at rim; burger filling represented by one seam.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5d4383cc-7fa3-4af5-b119-dc3b67d08db0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-002/references/20-5d4383cc-7fa3-4af5-b119-dc3b67d08db0.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'burger-beside-drink-cup'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('burger', 'beside', 'drink', 'cup')

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
        poly('cup',(6,18),(8,42),(16,42),(18,18),(6,18))
        poly('straw',(12,18),(16,6),(26,6));join('straw','cup')
        path('burger',(27,30),[('C',(42,30),(27,18),(42,18)),('L',(42,38)),('A',(38,42),4,4,True),('L',(31,42)),('A',(27,38),4,4,True),('L',(27,30))],True)
        line('filling',(27,33),(42,33));join('filling','burger')

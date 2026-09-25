"""Small Market Stall Kiosk.

Plan: Roofed market stall on two posts, counter and broad platform; bounds (6,6)-(42,42).
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Small counter panel inscription omitted; roof, posts, serving opening, counter and base retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9e1193a3-d007-4fdb-a204-58c17689d073'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-013/references/22-9e1193a3-d007-4fdb-a204-58c17689d073.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'pitched-roof-market-kiosk'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('pitched', 'roof', 'market', 'kiosk')

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
        poly('roof',(6,18),(24,6),(42,18),(34,18),(14,18),closed=True)
        poly('counter',(14,18),(14,30),(14,42),(34,42),(34,30),(34,18));join('roof','counter')
        line('counter-top',(14,30),(34,30));join('counter','counter-top')
        poly('platform',(6,42),(14,42),(34,42),(42,42));join('counter','platform')

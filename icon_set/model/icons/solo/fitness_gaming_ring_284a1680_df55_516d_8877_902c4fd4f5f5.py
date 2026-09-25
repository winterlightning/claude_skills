"""Gaming Fitness Ring.

Plan: Exercise ring with distinct top module and side grip. Extremes6,6,42,42.
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Omit tiny plus/button controls; retain the exercise ring and top control module. A straight section of the ring represents the side grip without a duplicate stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '284a1680-df55-516d-8877-902c4fd4f5f5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-022/references/10-284a1680-df55-516d-8877-902c4fd4f5f5.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'fitness-gaming-ring'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "video-games"
    categories = ("primitives", "video-games")
    aliases = ()
    keywords = ('fitness', 'gaming', 'ring')

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
        path('ring',(14,12),[('C',(6,21),(9,14),(6,17)),('L',(6,31)),('C',(24,42),(6,38),(15,42)),('A',(42,26),18,16,False),('A',(34,12),18,18,False)])
        path('module',(18,6),[('L',(30,6)),('A',(34,10),4,4,True),('L',(34,12)),('L',(34,14)),('A',(30,18),4,4,True),('L',(18,18)),('A',(14,14),4,4,True),('L',(14,12)),('L',(14,10)),('A',(18,6),4,4,True)],True);join('ring','module')
        

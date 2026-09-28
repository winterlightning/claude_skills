"""Catalytic Converter Heat Warning.

Plan: Horizontal converter capsule connected to inlet/outlet, three equal heat curves. Extremes 4,8,44,40.
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Keep three heat wisps; simplify each pipe to a single stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '83f2d586-e1c0-4aaf-81ac-49e5994ec8e0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-021/references/14-83f2d586-e1c0-4aaf-81ac-49e5994ec8e0.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'catalytic-converter-heat-waves'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transportation"
    categories = ("transportation", "primitives")
    aliases = ()
    keywords = ('catalytic', 'converter', 'heat', 'waves')

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
        path('housing',(18,24),[('L',(30,24)),('A',(36,30),6,6,True),('L',(36,32)),('L',(36,34)),('A',(30,40),6,6,True),('L',(18,40)),('A',(12,34),6,6,True),('L',(12,32)),('L',(12,30)),('A',(18,24),6,6,True)],True)
        for a,b,name in [((4,32),(12,32),'inlet'),((36,32),(44,32),'outlet')]:line(name,a,b);join('housing',name)
        for x in (14,24,34):path(f'heat-{x}',(x,8),[('C',(x,15),(x-3,11),(x+3,12))])

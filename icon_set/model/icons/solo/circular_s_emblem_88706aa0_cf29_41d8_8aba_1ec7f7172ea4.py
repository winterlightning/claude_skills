"""Stylized Circular S Symbol.

Plan: Circular abstract emblem divided by one flowing S curve; radius20 centered24.
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Abstract circular division retained; this is not treated as a literal typeface letter.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '88706aa0-cf29-41d8-8aba-1ec7f7172ea4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-014/references/39-88706aa0-cf29-41d8-8aba-1ec7f7172ea4.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'circular-s-emblem'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('circular', 's', 'emblem')

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
        self.add_arc('rim-left',(12,8),(36,40),radius_x=20,radius_y=20,sweep=False)
        self.add_arc('rim-right',(36,40),(12,8),radius_x=20,radius_y=20,sweep=False)
        self.add_contour('rim','rim-left','rim-right',closed=True)
        path('divider',(12,8),[('C',(24,24),(4,25),(15,24)),('C',(36,40),(35,24),(44,25))]);join('rim','divider')

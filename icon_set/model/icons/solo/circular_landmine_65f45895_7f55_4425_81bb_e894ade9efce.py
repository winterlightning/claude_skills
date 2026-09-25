"""Circular Explosive Landmine.

Plan: Pressure plate and cylindrical body as nested stepped contour, with top ellipse and lower band; x4..44 y8..40.
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Removed small central lens and external ticks; preserved raised circular pressure plate and cylindrical base.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '65f45895-7f55-4425-81bb-e894ade9efce'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-002/references/38-65f45895-7f55-4425-81bb-e894ade9efce.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'circular-landmine'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('circular', 'landmine')

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
        path('plate-top',(12,12),[('A',(36,12),12,4,True),('A',(12,12),12,4,True)],True)
        path('plate-side',(12,12),[('L',(12,24)),('A',(36,24),12,4,False),('L',(36,12))]);join('plate-side','plate-top')
        path('base',(12,24),[('L',(4,28)),('L',(4,32)),('A',(44,32),20,8,False),('L',(44,28)),('L',(36,24))]);join('base','plate-side')

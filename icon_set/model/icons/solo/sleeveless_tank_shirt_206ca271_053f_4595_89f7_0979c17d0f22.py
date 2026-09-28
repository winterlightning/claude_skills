"""Sleeveless Casual Tank Top.

Plan: Symmetric straight-sided tank shirt with broad straps and U neck; bounds (8,4)-(40,44).
Construction: Lucide shirt: coherent garment outline with intrinsic collar and armholes.
Reduction: Plain hem and two broad shoulder straps retained; no texture added.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '206ca271-053f-4595-89f7-0979c17d0f22'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-013/references/09-206ca271-053f-4595-89f7-0979c17d0f22.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'sleeveless-tank-shirt'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('sleeveless', 'tank', 'shirt')

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
        path('shirt',(8,44),[('L',(8,20)),('C',(12,4),(12,16),(12,10)),('L',(20,4)),('L',(20,10)),('A',(28,10),4,6,False),('L',(28,4)),('L',(36,4)),('C',(40,20),(36,10),(36,16)),('L',(40,44)),('L',(8,44))],True)

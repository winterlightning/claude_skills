"""Traditional Asian Teapot.

Plan: Centerline4,8,44,40. Squat vessel with overhead arch, broad left spout, right loop and centered pedestal.
Construction: No useful direct Lucide teapot match; source overhead arch and asymmetric spout/loop retained.
Reduction: Omitted tiny lid knob; vessel base simplified into the pedestal junction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f439bad7-bf84-59e6-9fdd-6df7d285d27a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-020/references/01-f439bad7-bf84-59e6-9fdd-6df7d285d27a.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'asian-teapot-overhead-handle'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('asian', 'teapot', 'overhead', 'handle')

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
        path('vessel',(14,22),[('L',(34,22)),('L',(34,26)),('A',(28,32),6,6,True),('L',(20,32)),('A',(14,26),6,6,True),('L',(14,22))],True)
        path('arch',(14,22),[('L',(14,18)),('A',(34,18),10,10,True),('L',(34,22))]);join('arch','vessel')
        poly('spout',(14,22),(4,16),(4,26),(14,26));join('spout','vessel')
        path('loop',(34,22),[('C',(44,27),(39,17),(44,20)),('C',(28,32),(44,33),(38,35))]);join('vessel','loop')
        poly('foot',(20,32),(20,40),(28,40),(28,32));join('foot','vessel')

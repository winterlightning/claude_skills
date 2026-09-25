"""Standing Dairy Cow.

Plan: Right-facing cow with broad body, short ear, muzzle, udder and two legs; bounds (4,8)-(44,40).
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Two visible legs retained; tail, eye and tiny udder omitted to prioritize the short-necked cow silhouette.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e86bdf40-e8f1-4d65-a5ae-e3b40658db61'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-014/references/21-e86bdf40-e8f1-4d65-a5ae-e3b40658db61.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'standing-cow-profile'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('standing', 'cow', 'profile')

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
        path('cow',(4,40),[('L',(4,21)),('A',(12,13),8,8,True),('L',(30,13)),('L',(31,8)),('L',(36,13)),('L',(44,21)),('L',(44,30)),('L',(36,28)),('L',(31,32)),('L',(31,40)),('L',(23,40)),('L',(23,31)),('L',(17,31)),('L',(12,31)),('L',(12,40)),('L',(4,40))],True)

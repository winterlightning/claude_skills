"""Two User Profiles.

Plan: Centerline4,8,44,40. Two equal circular heads and independent rounded shoulders repeated24u apart. Exact4u visible head/body gap.
Construction: Shared human-reference.md and human_ref/user.svg: equal circular heads, broad curved shoulders and separate body silhouettes. Lucide users original/debug inspected.
Reduction: Matched equal heads retained; shoulder lengths regularized for a balanced pair.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e5a4ad79-c26e-47fd-b9ee-41daa531ad17'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-020/references/05-e5a4ad79-c26e-47fd-b9ee-41daa531ad17.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'two-user-profiles'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('two', 'user', 'profiles')

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
        for j,cx in enumerate((12,36)):
         circle(f'head-{j}',cx,14,6)
         path(f'body-{j}',(cx-8,40),[('L',(cx-8,32)),('A',(cx-4,28),4,4,True),('L',(cx+4,28)),('A',(cx+8,32),4,4,True),('L',(cx+8,40))])

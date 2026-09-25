"""Simple Shopping Bag.

Plan: Centerline8,4,40,44. Tall blank rounded bag with centered low broad top handle.
Construction: Lucide shopping-basket informs shared handle attachment; original tall blank bag preserved.
Reduction: No identifying parts omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '963531cf-b4bd-429d-bd6b-fd5917cf751e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-019/references/26-963531cf-b4bd-429d-bd6b-fd5917cf751e.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'shopping-bag-draft'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('shopping', 'bag', 'draft')

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
        path('body',(12,16),[('L',(16,16)),('L',(32,16)),('L',(36,16)),('A',(40,20),4,4,True),('L',(40,40)),('A',(36,44),4,4,True),('L',(12,44)),('A',(8,40),4,4,True),('L',(8,20)),('A',(12,16),4,4,True)],True)
        path('handle',(16,16),[('L',(16,10)),('A',(22,4),6,6,True),('L',(26,4)),('A',(32,10),6,6,True),('L',(32,16))])
        join('handle','body')

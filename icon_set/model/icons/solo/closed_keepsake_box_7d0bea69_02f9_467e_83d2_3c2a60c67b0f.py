"""Storage Box with Lid.

Plan: Keepsake storage box with wide lid and small clasp; bounds (6,6)-(42,42).
Construction: Lucide box: shared lid/body structure; small center clasp remains.
Reduction: No identifying parts omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7d0bea69-02f9-467e-83d2-3c2a60c67b0f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-014/references/32-7d0bea69-02f9-467e-83d2-3c2a60c67b0f.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'closed-keepsake-box'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('closed', 'keepsake', 'box')

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
        path('lid',(10,6),[('L',(38,6)),('A',(42,10),4,4,True),('L',(42,16)),('L',(30,16)),('L',(18,16)),('L',(6,16)),('L',(6,10)),('A',(10,6),4,4,True)],True)
        path('body',(6,16),[('L',(6,36)),('A',(12,42),6,6,False),('L',(36,42)),('A',(42,36),6,6,False),('L',(42,16))]);join('lid','body')
        poly('clasp',(18,16),(18,24),(30,24),(30,16));join('lid','clasp')

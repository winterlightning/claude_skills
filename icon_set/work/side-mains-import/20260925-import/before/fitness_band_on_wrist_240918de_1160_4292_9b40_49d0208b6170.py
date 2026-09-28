"""Smart Fitness Tracker on Wrist.

Plan: Centerline4,10,44,38. Horizontal forearm, broad wristband and compact closed hand with attached thumb.
Construction: Shared human-reference.md and full_body_ref.png for simple anatomy, rounded hand vocabulary; Lucide hand original/debug inspected.
Reduction: Omitted diagonal band seam to preserve a clear10u-wide wristband interior. No detached head is present.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '240918de-1160-4292-9b40-49d0208b6170'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-019/references/31-240918de-1160-4292-9b40-49d0208b6170.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'fitness-band-on-wrist'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('fitness', 'band', 'on', 'wrist')

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
        rect('band',12,10,10,28,4)
        line('forearm-top',(4,14),(12,14));line('forearm-bottom',(4,34),(12,34))
        path('hand',(22,14),[('L',(36,14)),('A',(44,22),8,8,True),('L',(44,28)),('A',(40,32),4,4,True),('L',(33,32)),('C',(22,34),(30,40),(27,38))])
        for p in ('forearm-top','forearm-bottom','hand'):join('band',p)

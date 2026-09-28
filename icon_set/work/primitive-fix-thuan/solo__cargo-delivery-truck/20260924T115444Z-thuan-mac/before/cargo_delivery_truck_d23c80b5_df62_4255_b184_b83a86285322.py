"""Cargo Delivery Truck.

Plan: Truck body with wheel openings in bottom boundary; x4..44 y8..40, wheel centers12,36 and36,36.
Construction: Lucide truck: outline terminates at wheel side endpoints, avoiding tangent overlaps.
Reduction: Removed chassis double band and upper wheel interior arcs; two curved wheel bumps remain in the outer silhouette.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd23c80b5-df62-4255-b184-b83a86285322'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-002/references/30-d23c80b5-df62-4255-b184-b83a86285322.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'cargo-delivery-truck'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('cargo', 'delivery', 'truck')

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
        path('cargo',(8,8),[('L',(28,8)),('L',(28,36)),('L',(16,36)),('A',(8,36),4,4,True),('L',(4,36)),('L',(4,12)),('A',(8,8),4,4,True)],True)
        path('cab',(28,16),[('L',(36,16)),('L',(44,28)),('L',(44,36)),('L',(40,36)),('A',(32,36),4,4,True),('L',(28,36))]);join('cab','cargo')
        line('window',(28,24),(41,24));join('window','cargo');join('window','cab')

"""Rolled Blueprint Paper.

Plan: Centerline6,6,42,42. Blank sheet joins upright right roll; bottom roll seam has10u clearance.
Construction: Lucide scroll original and atomic-debug: sheet and explicit roll junctions.
Reduction: No identifying parts omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3ab75fea-801a-4cd2-b00b-8df6b38205e4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-019/references/07-3ab75fea-801a-4cd2-b00b-8df6b38205e4.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'rolled-blueprint'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('rolled', 'blueprint')

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
        poly('sheet',(32,12),(6,12),(6,42),(32,42))
        path('roll',(32,6),[('L',(36,6)),('A',(42,12),6,6,True),('L',(42,36)),('A',(36,42),6,6,True),('L',(32,42)),('L',(32,32)),('L',(32,12)),('L',(32,6))],True)
        path('curl',(32,32),[('L',(36,32)),('A',(42,36),6,4,True)])
        join('sheet','roll');join('curl','roll')

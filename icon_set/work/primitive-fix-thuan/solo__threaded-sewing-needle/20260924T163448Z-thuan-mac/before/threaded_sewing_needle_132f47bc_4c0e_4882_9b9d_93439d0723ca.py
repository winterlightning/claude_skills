"""Sewing Needle with Thread.

Plan: Centerline6,6,42,42. Diagonal pointed needle with broad rounded eye; thread passes through eye and shares a split outline node.
Construction: No useful direct Lucide match; diagonal needle and loose thread rebuilt with explicit passage junction.
Reduction: No identifying parts omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '132f47bc-4c0e-4882-9b9d-93439d0723ca'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-019/references/14-132f47bc-4c0e-4882-9b9d-93439d0723ca.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'threaded-sewing-needle'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('threaded', 'sewing', 'needle')

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
        path('needle',(6,42),[('L',(26,14)),('A',(34,6),8,8,True),('A',(42,14),8,8,True),('L',(34,22)),('L',(6,42))],True)
        path('thread',(30,14),[('L',(34,22)),('C',(36,34),(42,25),(42,28)),('L',(28,42))]);join('thread','needle')

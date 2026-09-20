"""Trash Can with Lid.

Plan: Centerline8,4,40,44. Plain straight-sided bin with projecting flat lid and central vertical knob.
Construction: Lucide trash original/debug: rounded lower sides and shared projecting lid.
Reduction: No identifying parts omitted; no absent front-panel detail added.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9164134d-338e-42a2-b57a-19c5716550d1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-020/references/03-9164134d-338e-42a2-b57a-19c5716550d1.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'waste-bin-with-central-lid-knob'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('waste', 'bin', 'with', 'central', 'lid', 'knob')

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
        poly('lid',(8,12),(10,12),(24,12),(38,12),(40,12))
        path('bin',(10,12),[('L',(10,38)),('A',(16,44),6,6,False),('L',(32,44)),('A',(38,38),6,6,False),('L',(38,12))])
        line('knob',(24,4),(24,12));join('bin','lid');join('lid','knob')

"""Smiling Mouth with Teeth.

Plan: Broad open mouth with upper and lower tooth rows, shared spacing10; bounds (4,8)-(44,40).
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Teeth reduced to four broad divisions per row; shallow upper-lip dip replaced with a clean broad edge.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8c9b5e16-c176-42c7-adbe-fdcaffda9cfc'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-013/references/44-8c9b5e16-c176-42c7-adbe-fdcaffda9cfc.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'open-smiling-mouth-teeth'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('open', 'smiling', 'mouth', 'teeth')

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
        path('mouth',(12,8),[('L',(14,8)),('L',(24,8)),('L',(34,8)),('L',(36,8)),('A',(44,16),8,8,True),('L',(44,32)),('A',(36,40),8,8,True),('L',(34,40)),('L',(24,40)),('L',(14,40)),('L',(12,40)),('A',(4,32),8,8,True),('L',(4,16)),('A',(12,8),8,8,True)],True)
        poly('upper-row',(4,16),(14,16),(24,16),(34,16),(44,16));poly('lower-row',(4,32),(14,32),(24,32),(34,32),(44,32));join('mouth','upper-row');join('mouth','lower-row')
        for j,x in enumerate((14,24,34)):
         line(f'upper-tooth-{j}',(x,8),(x,16));line(f'lower-tooth-{j}',(x,32),(x,40))
         for side in ('upper','lower'):join('mouth',f'{side}-tooth-{j}');join(f'{side}-row',f'{side}-tooth-{j}')

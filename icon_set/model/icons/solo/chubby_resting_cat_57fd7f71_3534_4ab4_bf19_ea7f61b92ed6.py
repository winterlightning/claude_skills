"""Cute Chubby Sitting Cat.

Plan: Long resting cat contour with spaced short ears, sleepy eyes, open haunch seam. Extremes4,8,44,40.
Construction: Lucide cat original/atomic-debug: spaced ears and sparse eyes.
Reduction: Omit mouth, paw subdivisions and inner haunch seam; long low contour and short ears preserve resting cat.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '57fd7f71-3534-4ab4-bf19-ea7f61b92ed6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-021/references/43-57fd7f71-3534-4ab4-bf19-ea7f61b92ed6.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'chubby-resting-cat'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('chubby', 'resting', 'cat')

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
        path('cat',(4,33),[('L',(4,23)),('C',(8,17),(4,20),(6,18)),('L',(8,8)),('L',(15,16)),('L',(23,16)),('L',(28,8)),('L',(29,16)),('L',(32,16)),('A',(44,28),12,12,True),('A',(32,40),12,12,True),('L',(10,40)),('A',(4,34),6,6,True),('L',(4,33))],True)
        for x in (13,23):self.add_dot(f'eye-{x}',(x,26))
        

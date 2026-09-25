"""Camping Teepee Tent.

Plan: Mirrored teepee with crossed poles and central triangular doorway, x6..42 y6..42.
Construction: Lucide tent: crossing support poles, broad triangular base, smaller opening.
Reduction: No omissions.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9a8df6e7-ee7a-4aa0-83a1-d092fac93c04'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-002/references/25-9a8df6e7-ee7a-4aa0-83a1-d092fac93c04.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'crossed-pole-teepee'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('crossed', 'pole', 'teepee')

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
        poly('left-pole',(6,42),(28,6))
        poly('right-pole',(42,42),(20,6));join('left-pole','right-pole')
        line('ground',(6,42),(42,42));join('ground','left-pole');join('ground','right-pole')
        poly('door',(16,42),(24,28),(32,42));join('door','ground')

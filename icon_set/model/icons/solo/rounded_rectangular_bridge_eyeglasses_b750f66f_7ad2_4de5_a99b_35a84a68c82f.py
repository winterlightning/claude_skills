"""Classic Rectangular Eyeglasses.

Plan: Two matching rectangular lenses rotated45 degrees; local long/short half-axis6/3, centers15,15 and33,33. Bounds6..42.
Construction: Lucide glasses: matched lens frames and connecting arch.
Reduction: Rotated whole glasses45 degrees to preserve wide rectangular lens proportions; round stroke joins provide modest corner rounding.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b750f66f-7ad2-4de5-a99b-35a84a68c82f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-002/references/47-b750f66f-7ad2-4de5-a99b-35a84a68c82f.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'rounded-rectangular-bridge-eyeglasses'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('rounded', 'rectangular', 'bridge', 'eyeglasses')

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
        poly('left-lens',(6,12),(12,6),(24,18),(18,24),closed=True)
        poly('right-lens',(24,30),(30,24),(42,36),(36,42),closed=True)
        path('bridge',(24,18),[('C',(30,24),(29,17),(31,19))]);join('bridge','left-lens');join('bridge','right-lens')

"""Bright Sun Symbol.

Plan: Circular sun and eight mirrored radial rays; cardinal tips at 4 and44, diagonal tips at10 and38.
Construction: Lucide sun: circular center, eight equal ray directions.
Reduction: No omissions.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '264df487-e0d4-4d8b-872e-1c53eccec98f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-002/references/14-264df487-e0d4-4d8b-872e-1c53eccec98f.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'bright-sun-symbol'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('bright', 'sun', 'symbol')

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
        circle('disc',24,24,8)
        for j,(a,b) in enumerate([((24,4),(24,7)),((24,41),(24,44)),((4,24),(7,24)),((41,24),(44,24)),((10,10),(12,12)),((36,12),(38,10)),((10,38),(12,36)),((36,36),(38,38))]): line(f'ray-{j}',a,b)

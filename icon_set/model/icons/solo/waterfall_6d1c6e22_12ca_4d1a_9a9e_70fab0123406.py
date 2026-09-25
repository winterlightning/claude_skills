"""Cascading Waterfall into Water Waves.

Plan: Four evenly spaced streams with radius1 ledge bends, above three wave lobes; x6..42 y6..42.
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Sharper ledge bend to preserve four independent streams; retained waterline waves.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6d1c6e22-12ca-4d1a-9a9e-70fab0123406'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-002/references/31-6d1c6e22-12ca-4d1a-9a9e-70fab0123406.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'waterfall'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('waterfall',)

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
        line('ledge',(6,6),(41,6))
        for j,x in enumerate((12,22,32,42)):
         path(f'stream-{j}',(x-1,6),[('A',(x,7),1,1,True),('L',(x,29))]);join('ledge',f'stream-{j}')
        path('pool',(6,40),[('A',(18,40),6,2,False),('A',(30,40),6,2,True),('A',(42,40),6,2,False)])

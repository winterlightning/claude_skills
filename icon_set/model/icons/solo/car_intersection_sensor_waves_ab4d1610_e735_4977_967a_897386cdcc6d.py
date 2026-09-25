"""Car with Intersection Sensor Waves.

Plan: Front car below signal wave pair, mirrored road edges. Extremes 6,6,42,42.
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Retain front car, road flare and one wave each side; omit second arcs and separate bumper detail.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ab4d1610-e735-4977-967a-897386cdcc6d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-021/references/12-ab4d1610-e735-4977-967a-897386cdcc6d.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'car-intersection-sensor-waves'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transportation"
    categories = ("transportation", "primitives")
    aliases = ()
    keywords = ('car', 'intersection', 'sensor', 'waves')

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
        path('car',(19,22),[('L',(29,22)),('L',(31,32)),('L',(30,32)),('L',(18,32)),('L',(17,32)),('L',(19,22))],True)
        for x in (18,30):line(f'wheel-{x}',(x,32),(x,38));join('car',f'wheel-{x}')
        for s in (-1,1):
         x=lambda v:24+s*v
         line(f'road-{s}',(x(17),24),(x(18),42))
         path(f'wave-{s}',(x(7),6),[('C',(x(18),16),(x(13),6),(x(18),10))])

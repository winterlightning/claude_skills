"""Geometric Hexagonal Video Play Symbol.

Plan: Six alternating outlined triangles with central diagonal crossing. Shared triangle grid. Extremes 6,6,42,42.
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: No identifying parts omitted.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '676befa5-604d-5f0a-9344-ef3dfc7baea7'
SOURCE_PATH = 'pictographic-primitives/video/amazon web service interactive video service_676befa5-604d-5f0a-9344-ef3dfc7baea7.svg'
AUTHOR = "gpt-6"


class Drawing(Solo48):
    icon_id = 'triangular-video-emblem'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('triangular', 'video', 'emblem')

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
        for n,pts in enumerate([[(10,12),(20,6),(20,18)],[(28,6),(38,12),(28,18)],[(6,20),(16,26),(6,32)],[(42,20),(32,26),(42,32)],[(10,36),(20,30),(20,42)],[(28,30),(38,36),(28,42)]]):poly(f'triangle-{n}',*pts,closed=True)
        line('diagonal-a',(20,18),(32,26));line('diagonal-b',(16,26),(28,30))
        for a,b in [('diagonal-a','triangle-0'),('diagonal-a','triangle-3'),('diagonal-b','triangle-2'),('diagonal-b','triangle-5')]:join(a,b)

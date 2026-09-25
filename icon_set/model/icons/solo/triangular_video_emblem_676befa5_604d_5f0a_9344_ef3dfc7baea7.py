"""A geometric video emblem made from six alternating triangles.
Plan: VRECT_L gives three rows extra vertical room within centerlines (8,4)-(40,44).
Reduction: Omitted the two central diagonal joining strokes and shortened the triangles to separate the repeated rows; retained all six alternating triangles.
Construction: No useful exact Lucide logo match; the supplied emblem governs the six-triangle arrangement.
Layout: Each triangle uses the same width and height; rows and columns are mirrored with alternating direction."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '676befa5-604d-5f0a-9344-ef3dfc7baea7'
SOURCE_PATH = 'pictographic-primitives/video/amazon web service interactive video service_676befa5-604d-5f0a-9344-ef3dfc7baea7.svg'
AUTHOR = "gpt-6"


class Drawing(Solo48):
    icon_id = 'triangular-video-emblem'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "video"
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
        for n,pts in enumerate([[(8,9),(20,4),(20,14)],[(28,4),(40,9),(28,14)],[(8,19),(20,24),(8,29)],[(40,19),(28,24),(40,29)],[(8,39),(20,34),(20,44)],[(28,34),(40,39),(28,44)]]):poly(f'triangle-{n}',*pts,closed=True)


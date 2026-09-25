"""Global Warming Burning Earth.

Plan: Globe below a detached flame crown; globe radius11, meridian and equator split at center; bounds (8,4)-(40,44).
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Three flame tips hover above the globe as in the original detached flame contour; dense globe grid reduced to one meridian/equator.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2e25e231-835a-48a3-bfbd-617111835a09'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-005/references/32-2e25e231-835a-48a3-bfbd-617111835a09.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'burning-globe'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('burning', 'globe')

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
        path('globe',(13,33),[('A',(24,22),11,11,True),('A',(35,33),11,11,True),('A',(24,44),11,11,True),('A',(13,33),11,11,True)],True)
        poly('equator',(13,33),(24,33),(35,33));poly('meridian',(24,22),(24,33),(24,44));join('globe','equator');join('globe','meridian');join('equator','meridian')
        path('flames',(8,14),[('L',(8,6)),('C',(16,14),(11,9),(12,14)),('C',(24,4),(20,14),(24,9)),('C',(32,14),(28,6),(30,11)),('L',(40,6)),('L',(40,14))])

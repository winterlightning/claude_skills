"""Celtic Trinity Knot Symbol.

Plan: Triquetra drawn as three pointed outer lobes and central curved triangle, each shared edge emitted once.
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Removed minute interweave gap and consolidated shared crossing edges; retained three pointed lobes and central triangular opening.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b1a69064-0e42-4be6-b058-9e7b790a01f4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-002/references/32-b1a69064-0e42-4be6-b058-9e7b790a01f4.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'triquetra-knot'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('triquetra', 'knot')

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
        path('outer',(24,6),[('C',(33,25),(30,10),(33,18)),('C',(42,42),(39,27),(42,34)),('C',(24,37),(36,42),(30,42)),('C',(6,42),(18,42),(12,42)),('C',(15,25),(6,34),(9,27)),('C',(24,6),(15,18),(18,10))],True)
        path('center',(15,25),[('C',(33,25),(20,22),(28,22)),('C',(24,37),(32,31),(29,35)),('C',(15,25),(19,35),(16,31))],True);join('outer','center')

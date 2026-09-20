"""Small Segmented Caterpillar.

Plan: Caterpillar with three rising lobed segments and round head plus short antenna; bounds (6,6)-(42,42).
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Tiny segment seams reduced to one; rounded head, rising body and antenna remain.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '81d9a460-8b31-4216-99ca-84b48ac5cd1c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-013/references/28-81d9a460-8b31-4216-99ca-84b48ac5cd1c.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'upright-segmented-caterpillar'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('upright', 'segmented', 'caterpillar')

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
        path('body',(6,36),[('C',(20,26),(6,30),(12,26)),('C',(30,18),(20,20),(24,18)),('A',(42,18),6,6,True),('A',(36,24),6,6,True),('C',(27,34),(36,30),(34,34)),('C',(16,42),(26,39),(22,42)),('C',(6,36),(10,42),(6,40))],True)
        path('segment-one',(20,26),[('C',(27,34),(18,32),(20,35))]);join('body','segment-one')
        line('antenna',(36,12),(38,6));join('body','antenna')

"""Classic Soccer Ball.

Plan: Circular ball r20 around central pentagon; five outward panel seams.
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Five broad surrounding panels replace secondary peripheral seams.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5d4b02d3-d5b1-419c-8699-81abf1e0d06e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-002/references/48-5d4b02d3-d5b1-419c-8699-81abf1e0d06e.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'paneled-soccer-ball'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('paneled', 'soccer', 'ball')

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
        circle('ball',24,24,20)
        poly('center-panel',(24,14),(34,22),(30,34),(18,34),(14,22),closed=True)
        for j,(a,b) in enumerate([((24,14),(24,4)),((34,22),(44,24)),((30,34),(36,40)),((18,34),(12,40)),((14,22),(4,24))]):
         line(f'seam-{j}',a,b);join(f'seam-{j}','center-panel');join(f'seam-{j}','ball')

"""Gherkin Skyscraper Building.

Plan: Tapered tower with two facade diagonals attached at exact silhouette nodes; bounds (10,4)-(38,44).
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Two facade bands retained instead of a dense diagonal glazing grid.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4836dd68-7a04-4bdf-9a6e-f17bd69f11c0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-005/references/26-4836dd68-7a04-4bdf-9a6e-f17bd69f11c0.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'gherkin-tower-silhouette'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('gherkin', 'tower', 'silhouette')

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
        path('tower',(16,44),[('C',(10,29),(12,42),(10,36)),('C',(14,16),(10,24),(12,19)),('C',(24,4),(17,9),(21,4)),('C',(38,29),(29,4),(38,18)),('C',(37,35),(38,31),(38,33)),('C',(32,44),(36,40),(34,43)),('L',(28,44)),('L',(16,44))],True)
        line('band-one',(14,16),(37,35));line('band-two',(10,29),(28,44));join('tower','band-one');join('tower','band-two')

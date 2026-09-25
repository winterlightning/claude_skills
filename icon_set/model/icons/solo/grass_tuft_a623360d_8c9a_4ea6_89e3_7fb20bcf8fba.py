"""Small Patch of Growing Grass.

Plan: Three grass blades from a shared ground line; bounds (4,8)-(44,40).
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Each pointed outlined blade reduced to a curved stroke; three blade directions and ground retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a623360d-8c9a-4ea6-89e3-7fb20bcf8fba'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-013/references/23-a623360d-8c9a-4ea6-89e3-7fb20bcf8fba.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'grass-tuft'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('grass', 'tuft')

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
        poly('ground',(4,40),(14,40),(24,40),(34,40),(44,40))
        path('left',(14,40),[('C',(7,15),(15,29),(11,20))]);path('middle',(24,40),[('C',(29,8),(22,29),(25,16))]);path('right',(34,40),[('C',(42,20),(34,31),(37,24))])
        for p in ('left','middle','right'):join('ground',p)

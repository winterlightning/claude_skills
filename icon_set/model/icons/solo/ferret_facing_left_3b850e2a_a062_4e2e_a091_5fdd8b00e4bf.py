"""Standing Ferret Animal.

Plan: Low left-facing ferret with small muzzle, long back, front paw, broad haunch and tapered tail; bounds (4,8)-(44,40).
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Tail curl and inner haunch crease consolidated into the lower silhouette; long arched back retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3b850e2a-a062-4e2e-a091-5fdd8b00e4bf'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-014/references/22-3b850e2a-a062-4e2e-a091-5fdd8b00e4bf.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'ferret-facing-left'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('ferret', 'facing', 'left')

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
        path('ferret',(4,14),[('L',(14,8)),('C',(21,20),(20,8),(16,20)),('C',(37,26),(29,13),(37,17)),('C',(44,34),(37,30),(44,29)),('C',(34,40),(44,39),(38,40)),('L',(24,40)),('L',(29,32)),('L',(19,32)),('L',(15,40)),('L',(4,40)),('L',(10,31)),('L',(10,20)),('L',(4,18)),('L',(4,14))],True)

"""Small Branch with Three Leaves.

Plan: Three pointed leaves around a stem, one upward and two outward; bounds (6,6)-(42,42).
Construction: Lucide sprout: pointed leaf loops and attached stem; three leaves retained.
Reduction: Reoriented twig upright and omitted leaf veins to keep three clear leaves.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7d0f9012-8ae7-419f-ac3b-fd25f10824f4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-013/references/14-7d0f9012-8ae7-419f-ac3b-fd25f10824f4.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'three-leaf-twig'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('three', 'leaf', 'twig')

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
        poly('stem',(24,20),(24,34),(24,42))
        path('top-leaf',(24,6),[('C',(24,20),(16,10),(16,16)),('C',(24,6),(32,16),(32,10))],True);join('stem','top-leaf')
        path('left-leaf',(24,34),[('C',(6,24),(18,24),(10,24)),('C',(24,34),(6,35),(17,40))],True)
        path('right-leaf',(24,34),[('C',(42,24),(30,24),(38,24)),('C',(24,34),(42,35),(31,40))],True)
        join('stem','left-leaf');join('stem','right-leaf');join('left-leaf','right-leaf')

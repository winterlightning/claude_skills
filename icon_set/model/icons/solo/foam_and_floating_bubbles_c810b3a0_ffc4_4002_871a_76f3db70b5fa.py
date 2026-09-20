"""Soap Bubbles and Foam.

Plan: Foam mound and two floating circles; bounds (4,8)-(44,40). Repeated bubble arcs, asymmetric rising mound.
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Foam lobes consolidated; two detached bubble marks retained at different sizes; smallest reads as a dot.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c810b3a0-ffc4-4002-871a-76f3db70b5fa'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-014/references/01-c810b3a0-ffc4-4002-871a-76f3db70b5fa.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'foam-and-floating-bubbles'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('foam', 'and', 'floating', 'bubbles')

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
        circle('bubble-large',10,14,6);circle('bubble-small',26,10,2)
        path('foam',(4,40),[('C',(16,30),(4,32),(10,30)),('C',(25,30),(19,25),(22,25)),('C',(32,24),(24,26),(28,24)),('A',(44,24),6,6,True),('C',(44,31),(44,26),(44,28)),('A',(35,40),9,9,True),('L',(4,40))],True)

"""Retail Store Shopping Cart.

Plan: Centerline4,8,44,40. Left grip, shallow basket and two matching open circular wheels with9u floor-to-wheel clearance.
Construction: Lucide shopping-basket informs trapezoid construction; source-specific left grip and open wheels.
Reduction: Omitted the tight under-basket curl; wheel openings preserved instead of filling them.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3352f8c5-b764-483d-b1b4-cbbf08da871f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-019/references/04-3352f8c5-b764-483d-b1b4-cbbf08da871f.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'shopping-cart-angular-open-wheels'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("other", "primitives-generate")
    aliases = ()
    keywords = ('shopping', 'cart', 'angular', 'open', 'wheels')

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
        poly('handle',(4,8),(10,8),(12,14))
        poly('basket',(12,14),(44,14),(41,23),(14,23),closed=True)
        join('handle','basket')
        circle('left-wheel',18,36,4);circle('right-wheel',36,36,4)

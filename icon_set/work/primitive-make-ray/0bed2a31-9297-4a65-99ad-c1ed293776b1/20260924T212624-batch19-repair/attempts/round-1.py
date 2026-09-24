"""User Centered Geometric Interaction.

Plan: Central user with three different orbit shapes and curved connectors. Extremes 6,6,42,42.
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Retain all three shapes and central user; reduce orbit to two visible curved connectors. Detached head to shoulders target 4 ink units.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '0bed2a31-9297-4a65-99ad-c1ed293776b1'
SOURCE_PATH = 'pictographic-primitives/users/user experience design_0bed2a31-9297-4a65-99ad-c1ed293776b1.svg'
AUTHOR = "gpt-6"


class Drawing(Solo48):
    icon_id = 'user-centered-shape-diagram'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('user', 'centered', 'shape', 'diagram')

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
        rect('square',20,6,8,8)
        circle('circle',10,36,4)
        poly('triangle',(34,42),(42,42),(38,34),closed=True)
        circle('head',24,24,3)
        path('shoulders',(18,39),[('A',(30,39),6,6,True)])
        path('orbit-left',(6,25),[('C',(11,14),(6,20),(8,17))])
        path('orbit-right',(37,14),[('C',(42,25),(40,17),(42,20))])

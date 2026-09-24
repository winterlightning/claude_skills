"""A user surrounded by square, circular and triangular design symbols.
Plan: SQUARE accommodates the square above, small circle left and large triangle lower-right.
Reduction: Reduced the head and circular symbol to tiny complete circles, narrowed the shoulders and shortened the two orbit arcs.
Construction: human_ref/user.svg: round head and broad shoulder arc; source owns the surrounding shapes.
Layout: User shifted left to clear the enlarged triangle. Head center (19,24), radius2, bottom y26; shoulder apex y34 gives exactly four units of detached ink clearance."""
from ...keyshapes import Keyshape
from ._base import Solo48

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
        circle('circle',8,29,2)
        poly('triangle',(30,42),(42,42),(37,26),closed=True)
        circle('head',19,24,2)
        path('shoulders',(15,38),[('A',(23,38),4,4,True)])
        path('orbit-left',(6,19),[('C',(11,10),(6,15),(8,12))])
        path('orbit-right',(37,10),[('C',(42,17),(40,11),(42,14))])

"""Rounded shopping cart with a left handle, shallow basket, and two open wheels. Local Lucide shopping-cart informed the basket and wheel rhythm; the source supplies the rounded lower corner."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '09afbc31-5487-4884-b5bb-9534c9f636f2'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__shopping-cart-rounded-open-wheels/20260927T172707Z-thuan-mac-1/reference/cart 1_09afbc31-5487-4884-b5bb-9534c9f636f2.svg'
AUTHOR = "gpt-6"


class Drawing(Solo48):
    icon_id = 'shopping-cart-rounded-open-wheels'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("other", "primitives-generate")
    aliases = ()
    keywords = ('shopping', 'cart', 'rounded', 'open', 'wheels')

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
        poly('handle',(6,6),(10,6),(13,14))
        path('basket',(13,14),[('L',(42,14)),('L',(41,19)),('A',(36,24),5,5,True),('L',(16,24)),('L',(13,14))],True)
        join('handle','basket')
        circle('left-wheel',18,37,5);circle('right-wheel',36,37,5)

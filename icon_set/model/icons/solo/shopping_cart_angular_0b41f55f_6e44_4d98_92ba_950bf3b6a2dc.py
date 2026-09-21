"""Simple Retail Shopping Cart.

Plan: Basket with two repeated circular wheels, left handle; bounds6,6,42,42. Wheel centers share baseline and radius3.
Construction reference: shopping-cart.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0b41f55f-6e44-4d98-92ba-950bf3b6a2dc'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/cart 1_0b41f55f-6e44-4d98-92ba-950bf3b6a2dc.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'shopping-cart-angular'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('shopping', 'cart', 'angular')

    def build(self):

        def path(name, start, commands, closed=False):
            here=start; members=[]
            for index,(kind,end,*args) in enumerate(commands):
                member=f"{name}-{index}"
                if kind=='L': self.add_line(member,here,end)
                elif kind=='A': self.add_arc(member,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(member,here,(args[0],args[1],end))
                here=end; members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def rect(name,x,y,w,h,r=4):
            path(name,(x+r,y),[('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*points,closed=False): self.add_polyline(name,*points,closed=closed)
        def join(a,b): self.relate('connect',a,b)

        poly('handle',(6,6),(12,6),(14,14));
        poly('basket',(14,14),(42,14),(36,28),(18,28),(14,14));join('handle','basket')
        for j,x in enumerate((20,36)): circle(f'wheel-{j}',x,39,3)

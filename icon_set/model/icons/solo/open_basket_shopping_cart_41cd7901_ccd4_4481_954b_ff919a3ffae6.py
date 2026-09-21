"""Retail Shopping Cart.

Plan: Sloped shopping basket and handle with two circular wheels; bounds4,8,44,40. Simplify lower return frame.
Construction reference: Lucide shopping-cart: angled basket and paired round wheels
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '41cd7901-ccd4-4481-954b-ff919a3ffae6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_10/cartload_41cd7901-ccd4-4481-954b-ff919a3ffae6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'open-basket-shopping-cart'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('open', 'basket', 'shopping', 'cart')

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

        poly('frame',(4,8),(10,8),(12,15),(14,23),(38,23),(44,15),(12,15))
        circle('wheel-left',18,36,4);circle('wheel-right',36,36,4)

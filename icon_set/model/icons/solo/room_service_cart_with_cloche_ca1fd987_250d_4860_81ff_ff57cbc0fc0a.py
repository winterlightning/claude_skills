"""Room Service Food Cart.

Plan: Service cart with dome above and paired wheels; bounds6,6,42,42. Single cart rail replaces crowded body striations.
Construction reference: No useful exact Lucide match; source-specific construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ca1fd987-250d-4860-81ff-ff57cbc0fc0a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_33/room service cart food_ca1fd987-250d-4860-81ff-ff57cbc0fc0a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'room-service-cart-with-cloche'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('room', 'service', 'cart', 'with', 'cloche')

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
            path(name,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def rect(name,x,y,w,h,r=4):
            path(name,(x+r,y),[('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*points,closed=False): self.add_polyline(name,*points,closed=closed)
        def join(a,b): self.relate('connect',a,b)

        path('cover',(16,22),[('A',(28,10),12,12,True),('A',(40,22),12,12,True)])
        line('knob',(28,6),(28,10));join('knob','cover')
        poly('cart',(12,22),(16,22),(40,22),(42,22),(42,34),(36,34),(16,34),(12,34),closed=True);join('cover','cart')
        poly('handle',(6,14),(6,22),(12,22));join('handle','cart')
        circle('wheel-a',16,38,4);circle('wheel-b',36,38,4);join('wheel-a','cart');join('wheel-b','cart')

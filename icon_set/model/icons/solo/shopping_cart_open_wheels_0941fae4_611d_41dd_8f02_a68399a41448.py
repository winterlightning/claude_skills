"""Fresh reference repair. Construction reference: Lucide shopping-cart.
Keyshape SQUARE; source identity is preserved separately from its icon name.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '0941fae4-611d-41dd-8f02-a68399a41448'
SOURCE_PATH = 'pictographic-primitives/shopping/cart_0941fae4-611d-41dd-8f02-a68399a41448.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'shopping-cart-open-wheels'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shopping'
    aliases = ()
    keywords = ('cart',)

    def path(self,n,start,*steps,closed=False):
        here=start; ids=[]
        for i,step in enumerate(steps):
            kind,end,*v=step; name=f'{n}-{i}';ids.append(name)
            if kind=='L':self.add_line(name,here,end)
            elif kind=='A':self.add_arc(name,here,end,radius_x=v[0],radius_y=v[1],sweep=v[2])
            elif kind=='C':self.add_bezier(name,here,(v[0],v[1],end))
            here=end
        self.add_contour(n,*ids,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x,y-r),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True),('A',(x,y-r),r,r,True),closed=True)

    def build(self):

        # Deeper reference trapezoid, extending directly into its right handle; identical open wheels.
        self.add_polyline('basket',(42,12),(4,12),(12,24),(36,24),(42,12),closed=True)
        self.add_line('handle',(42,12),(44,8))
        for i,x in enumerate((16,32)):self.circle(f'wheel-{i}',x,36,4)
        self.relate('connect','basket','handle')

    icon_id = 'shopping-cart-open-wheels'
    category = 'shopping'
    aliases = ()
    keywords = ('cart', 'shopping', 'trolley', 'basket', 'wheels', 'retail', 'supermarket')
    semantic_role = 'MAIN'
    semantic_kind = 'noun'

'shopping cart. Deeper tapered basket, right grip, continuous lower support and attached equal circular wheels restore missing chassis structure. Construction reference: local Lucide shopping-cart.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '22ba9936-54d3-4de1-815f-e80d16f43ff1'
SOURCE_PATH = 'pictographic-primitives/shopping/shopping cart_22ba9936-54d3-4de1-815f-e80d16f43ff1.svg'
AUTHOR = 'gpt-6'
PARENT_MODULE = 'icon_set/model/icons/solo/shopping_cart_right_grip_lower_rail_22ba9936_54d3_4de1_815f_e80d16f43ff1.py'
class Drawing(Solo48):
    icon_id = 'shopping-cart-right-grip-lower-rail'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shopping'
    aliases = ()
    keywords = ('shopping cart',)

    def path(self,n,start,commands,closed=False):
        ids=[]
        for i,c in enumerate(commands):
            k=f'{n}-{i}';end=c[1]
            if c[0]=='L':self.add_line(k,start,end)
            elif c[0]=='A':self.add_arc(k,start,end,radius_x=c[2],radius_y=c[3],sweep=c[4])
            elif c[0]=='C':self.add_bezier(k,start,(c[2],c[3],end))
            ids.append(k);start=end
        self.add_contour(n,*ids,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
    def box(self,n,l,t,r,b,rad=4):
        self.path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)

    def build(self):
        self.add_polyline('basket',(6,14),(38,14),(35,26),(10,26),(6,14),closed=True)
        self.add_polyline('handle',(38,14),(40,6),(42,6));self.relate('connect','basket','handle')
        self.path('support',(35,26),[('C',(32,34),(35,30),(35,34)),('L',(14,34))])
        self.relate('connect','basket','support')
        for x in (14,32):
            self.path(f'wheel-{x}',(x,34),[('A',(x,42),4,4,True),('A',(x,34),4,4,True)],True)
            self.relate('connect','support',f'wheel-{x}')

    icon_id = 'shopping-cart-right-grip-lower-rail'
    category = 'shopping'
    aliases = ()
    keywords = ('cart', 'shopping', 'trolley', 'basket', 'wheels', 'retail', 'supermarket')
    semantic_role = 'MAIN'
    semantic_kind = 'noun'

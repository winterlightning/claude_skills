'cart. Deeper basket, small curved right handle, restored support curl and two equal outlined wheels. Source asymmetry and shopping direction preserved. Construction reference: local Lucide shopping-cart.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '4f97114c-a7e4-4f5d-935d-2b5d4711fb3f'
SOURCE_PATH = 'pictographic-primitives/shopping/cart_4f97114c-a7e4-4f5d-935d-2b5d4711fb3f.svg'
AUTHOR = 'gpt-6'
PARENT_MODULE = 'icon_set/model/icons/solo/shopping_cart_rounded_basket_4f97114c_a7e4_4f5d_935d_2b5d4711fb3f.py'
class Drawing(Solo48):
    icon_id = 'shopping-cart-rounded-basket'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shopping'
    categories = ('shopping', 'primitives')
    aliases = ()
    keywords = ('cart',)

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
        self.path('basket',(38,14),[('L',(6,14)),('L',(9,23)),('A',(13,26),4,4,False),('L',(34,26)),('L',(38,14))],True)
        self.path('handle',(38,14),[('L',(40,8)),('A',(42,6),2,2,True)])
        self.relate('connect','handle','basket')
        self.path('support',(34,26),[('A',(34,34),4,4,True),('L',(14,34))])
        self.relate('connect','support','basket')
        for x in (14,34):
            self.path(f'wheel-{x}',(x,34),[('A',(x,42),4,4,True),('A',(x,34),4,4,True)],True)
            self.relate('connect','support',f'wheel-{x}')

    icon_id = 'shopping-cart-rounded-basket'
    category = 'shopping'
    categories = ('shopping', 'primitives')
    aliases = ()
    keywords = ('cart', 'shopping', 'trolley', 'basket', 'wheels', 'retail', 'supermarket')
    semantic_role = 'MAIN'
    semantic_kind = 'noun'

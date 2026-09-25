'Cart with rounded basket corner, curled support and equal open wheels.'
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='09afbc31-5487-4884-b5bb-9534c9f636f2'
SOURCE_PATH='pictographic-primitives/other/cart 1_09afbc31-5487-4884-b5bb-9534c9f636f2.svg'
AUTHOR='gpt-6'
PLAN='Cart with rounded basket corner, curled support and equal open wheels.'
CONSTRUCTION_REFERENCE='Lucide shopping-cart: basket, curled undercarriage and circular wheels.'
class Drawing(Solo48):
    icon_id='rounded-retail-cart'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('cart', '1')
    def circle(self,n,x,y,r):
        self.add_arc(n+'-top',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-bottom',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-top',n+'-bottom',closed=True)

    def path(self,n,start,commands,closed=False):
        ids=[];here=start
        for i,c in enumerate(commands):
            tag,end,*args=c; eid=f'{n}-{i}'
            if tag=='L': self.add_line(eid,here,end)
            elif tag=='A': self.add_arc(eid,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            elif tag=='C': self.add_bezier(eid,here,(args[0],args[1],end))
            ids.append(eid);here=end
        self.add_contour(n,*ids,closed=closed)

    def box(self,n,l,t,r,b,rad=4):
        self.path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)

    def file(self,l=8,t=4,r=40,b=44):
        self.path('page',(l+4,t),[('L',(r-10,t)),('L',(r,t+10)),('L',(r,b-4)),('A',(r-4,b),4,4,True),('L',(l+4,b)),('A',(l,b-4),4,4,True),('L',(l,t+4)),('A',(l+4,t),4,4,True)],True)

    def build(self):
        self.add_polyline('handle',(4,8),(8,8),(12,12))
        self.path('basket',(12,12),[('L',(44,12)),('L',(42,20)),('C',(38,24),(41,23),(40,24)),('L',(16,24)),('L',(12,12))],True)
        self.path('support',(16,24),[('C',(18,32),(10,27),(18,28))])
        self.circle('left-wheel',18,36,4);self.circle('right-wheel',36,36,4)
        for a,b in [('handle','basket'),('basket','support'),('support','left-wheel')]:self.relate('connect',a,b)

# Keyshape: HRECT_L balances the basket, handle and matching wheels.
# Visual review: Deeper basket, rounded lower-right corner and a curled support reaching the rear wheel. Equal open wheel circles.
OMISSIONS='No defining parts omitted; the support curl is compacted to clear the wheel opening.'

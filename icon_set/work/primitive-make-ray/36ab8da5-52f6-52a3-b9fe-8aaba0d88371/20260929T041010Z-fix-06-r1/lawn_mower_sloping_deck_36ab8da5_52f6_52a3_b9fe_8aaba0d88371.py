"""Rejected disconnected wheel struts and engine outline read as a cart. Restore a continuous mower deck, underbody and engine, keeping the reference handle direction."""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='36ab8da5-52f6-52a3-b9fe-8aaba0d88371'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__lawn-mower-sloping-deck/20260929T041010Z-thuan-mac/reference/gardening lawn mower_36ab8da5-52f6-52a3-b9fe-8aaba0d88371.svg'
AUTHOR='gpt-6'
PLAN='Rejected disconnected wheel struts and engine outline read as a cart. Restore a continuous mower deck, underbody and engine, keeping the reference handle direction.'
CONSTRUCTION_REFERENCE='Lucide car original and atomic-debug: coherent chassis and round wheels; mower form from original.'
OMISSIONS='Only insignificant source detail omitted.'
class Drawing(Solo48):
    icon_id='lawn-mower-sloping-deck'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=()

    def circle(self,n,x,y,r):
        self.add_arc(n+'a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'a',n+'b',closed=True)
    def path(self,n,start,commands,closed=False):
        ids=[]; here=start
        for i,c in enumerate(commands):
            tag,end,*args=c; eid=f'{n}-{i}'
            if tag=='L': self.add_line(eid,here,end)
            elif tag=='A': self.add_arc(eid,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            elif tag=='C': self.add_bezier(eid,here,(args[0],args[1],end))
            ids.append(eid); here=end
        self.add_contour(n,*ids,closed=closed)
    def box(self,n,l,t,r,b,rad=3):
        self.path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)

    def build(self):
        self.circle('rear-wheel',11,35,7)
        self.circle('front-wheel',38,37,5)
        self.path('deck',(7,29),[('L',(7,27)),('C',(13,23),(7,24),(9,22)),('L',(37,28)),('C',(43,32),(41,29),(43,29))])
        self.add_line('underdeck',(18,37),(33,37))
        self.path('engine',(19,24),[('L',(19,19)),('A',(22,16),3,3,True),('L',(28,16)),('A',(31,19),3,3,True),('L',(33,27))])
        self.relate('connect','deck','rear-wheel','front-wheel','engine'); self.relate('connect','underdeck','rear-wheel','front-wheel')

        self.path('handle',(12,23),[('L',(6,8)),('L',(4,8))])
        self.relate('connect','handle','deck')

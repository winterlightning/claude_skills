"""Rejected chassis reads as a simple bicycle/cart. Restore ATV engine body, concave saddle, high steering handle and heavy wheels with hubs."""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='b3f07500-0d8f-5bbb-b806-122fe5e29847'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__quad-bike/20260929T041010Z-thuan-mac/reference/atv_b3f07500-0d8f-5bbb-b806-122fe5e29847.svg'
AUTHOR='gpt-6'
PLAN='Rejected chassis reads as a simple bicycle/cart. Restore ATV engine body, concave saddle, high steering handle and heavy wheels with hubs.'
CONSTRUCTION_REFERENCE='Lucide car original and atomic-debug: independent circular wheels and connected chassis; ATV saddle from original.'
OMISSIONS='Only insignificant source detail omitted.'
class Drawing(Solo48):
    icon_id='quad-bike'
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
        self.circle('rear-wheel',12,32,8);self.circle('front-wheel',36,32,8)
        self.add_dot('rear-hub',(12,32));self.add_dot('front-hub',(36,32))
        self.path('body',(4,26),[('L',(4,20)),('L',(17,20)),('C',(26,20),(17,28),(26,28)),('L',(36,20)),('A',(42,26),6,6,True)])
        self.add_line('underbody',(20,34),(28,34))
        self.add_polyline('handle',(34,20),(29,8),(23,8))
        self.relate('connect','body','rear-wheel','front-wheel','handle');self.relate('connect','underbody','rear-wheel','front-wheel')

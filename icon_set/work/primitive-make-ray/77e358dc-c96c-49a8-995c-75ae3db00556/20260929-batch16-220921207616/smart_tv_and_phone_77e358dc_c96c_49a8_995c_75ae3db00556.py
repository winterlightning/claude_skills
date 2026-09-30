"""The rejected television is an open C and only one wireless arc survives. Restore the wide screen, its stand and two Wi-Fi arcs beside the phone.
Plan: SQUARE exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: Lucide monitor-smartphone: interrupted screen behind a separate phone and a T stand.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='77e358dc-c96c-49a8-995c-75ae3db00556'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__smart-tv-and-phone/20260929T145934Z-thuan-mac/reference/smart tv and phone_77e358dc-c96c-49a8-995c-75ae3db00556.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='smart-tv-and-phone'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('smart', 'tv', 'and', 'phone')
    def build(self):

        def path(n,start,steps,closed=False):
            members=[];here=start
            for j,(kind,end,*args) in enumerate(steps):
                m=f'{n}-{j}'
                if kind=='L':self.add_line(m,here,end)
                elif kind=='A':self.add_arc(m,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C':self.add_bezier(m,here,(args[0],args[1],end))
                members.append(m);here=end
            self.add_contour(n,*members,closed=closed)
        def oval(n,x,y,rx,ry):path(n,(x-rx,y),[('A',(x+rx,y),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
        def box(n,l,t,r,b,rad=0):
            if not rad:self.add_polyline(n,(l,t),(r,t),(r,b),(l,b),closed=True);return
            path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        path('screen',(24,24),[('L',(10,24)),('A',(6,28),4,4,False),('L',(6,30)),('A',(10,34),4,4,False),('L',(42,34))])
        line('stand',(20,34),(20,42));line('foot',(12,42),(28,42));join('stand','screen');join('stand','foot')
        box('phone',34,14,42,26,2)
        path('wifi',(6,10),[('A',(16,6),10,4,True),('A',(26,10),10,4,True)])
        self.add_dot('wifi-inner',(16,15))

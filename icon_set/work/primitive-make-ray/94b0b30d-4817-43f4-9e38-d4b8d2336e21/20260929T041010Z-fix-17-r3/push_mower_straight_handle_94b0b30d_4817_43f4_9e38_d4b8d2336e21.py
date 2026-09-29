"""Rejected disconnected wheel struts and engine outline read as a cart. Restore a continuous mower deck, underbody and engine, keeping the reference handle direction."""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='94b0b30d-4817-43f4-9e38-d4b8d2336e21'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__push-mower-straight-handle/20260929T041010Z-thuan-mac/reference/lawn mower_94b0b30d-4817-43f4-9e38-d4b8d2336e21.svg'
AUTHOR='gpt-6'
PLAN='Rejected disconnected wheel struts and engine outline read as a cart. Restore a continuous mower deck, underbody and engine, keeping the reference handle direction.'
CONSTRUCTION_REFERENCE='Lucide car original and atomic-debug: coherent chassis and round wheels; mower form from original.'
OMISSIONS='Only insignificant source detail omitted.'
class Drawing(Solo48):
    icon_id='push-mower-straight-handle'
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
        self.circle('wheel-left',10,34,6)
        self.circle('wheel-right',34,34,6)
        self.path('deck',(4,30),[('A',(10,24),6,6,True),('L',(34,24)),('L',(34,28))])
        self.add_line('underdeck',(16,35),(28,35))
        self.box('engine',12,16,26,24,3)
        self.add_line('handle',(34,24),(44,8))
        self.relate('connect','deck','wheel-left','wheel-right','engine','handle'); self.relate('connect','underdeck','wheel-left','wheel-right')

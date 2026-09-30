"""The rejected drainage channel has flat square sidewall tops and no front sidewall seam. Round the wall caps and show the recessed channel behind its curved front edge.
Plan: HRECT_L exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: No useful direct match.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='bee047c3-d480-4b1e-8469-37570947d8bd'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__open-drainage-channel/20260929T135612Z-thuan-mac/reference/canal_bee047c3-d480-4b1e-8469-37570947d8bd.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='open-drainage-channel'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('open', 'drainage', 'channel')
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

        path('channel',(4,28),[('L',(8,12)),('A',(16,12),4,4,True),('L',(16,24)),('A',(20,28),4,4,False),('L',(28,28)),('A',(32,24),4,4,False),('L',(32,12)),('A',(40,12),4,4,True),('L',(44,28)),('A',(32,40),12,12,True),('L',(16,40)),('A',(4,28),12,12,True)],True)
        line('back',(16,19),(32,19));join('back','channel')
        line('front-left',(4,28),(16,28));line('front-right',(32,28),(44,28));join('front-left','channel');join('front-right','channel')

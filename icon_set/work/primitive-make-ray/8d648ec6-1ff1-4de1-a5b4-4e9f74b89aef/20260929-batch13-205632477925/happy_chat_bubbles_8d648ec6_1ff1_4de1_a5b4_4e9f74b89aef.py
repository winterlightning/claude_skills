"""Foreground reply is too narrow and tails collapse into nubs; restore a square reply and legible diagonal tails.
Plan: SQUARE exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: messages-square: overlapping rounded message contours
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='8d648ec6-1ff1-4de1-a5b4-4e9f74b89aef'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__happy-chat-bubbles/20260929T135357Z-thuan-mac/reference/conversation smile type_8d648ec6-1ff1-4de1-a5b4-4e9f74b89aef.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='happy-chat-bubbles'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('happy', 'chat', 'bubbles')
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

        path('back',(32,20),[('L',(32,10)),('A',(28,6),4,4,False),('L',(10,6)),('A',(6,10),4,4,False),('L',(6,31)),('A',(10,35),4,4,False),('L',(14,35)),('L',(14,42)),('L',(22,35))])
        path('front',(32,20),[('L',(38,20)),('A',(42,24),4,4,True),('L',(42,33)),('A',(38,37),4,4,True),('L',(38,42)),('L',(32,37)),('L',(30,37)),('A',(26,33),4,4,True),('L',(26,24)),('A',(30,20),4,4,True),('L',(32,20))],True);join('front','back')
        self.add_dot('eye-left',(15,15));self.add_dot('eye-right',(23,15))
        path('smile',(14,24),[('C',(20,24),(16,27),(18,27))])

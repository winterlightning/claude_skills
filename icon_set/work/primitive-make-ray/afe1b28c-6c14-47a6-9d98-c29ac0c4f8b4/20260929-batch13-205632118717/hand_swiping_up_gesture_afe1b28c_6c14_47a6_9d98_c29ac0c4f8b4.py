"""Angular polygon hand and faceted contact arc obscure touch gesture. Replace with rounded index, thumb and a smooth contact arc.
Plan: HRECT_L exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: hand and pointer: continuous rounded outline
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='afe1b28c-6c14-47a6-9d98-c29ac0c4f8b4'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__hand-swiping-up-gesture/20260929T135357Z-thuan-mac/reference/gesture tap swipe up 1_afe1b28c-6c14-47a6-9d98-c29ac0c4f8b4.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='hand-swiping-up-gesture'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('hand', 'swiping', 'up', 'gesture')
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

        path('hand',(4,38),[('L',(4,30)),('L',(16,23)),('C',(19,29),(24,20),(26,25)),('L',(28,29)),('A',(28,37),4,4,True),('L',(20,37)),('L',(18,40)),('L',(4,38))],True)
        path('contact',(36,20),[('A',(36,40),8,10,True)])
        poly('arrow',(20,12),(24,8),(28,12));line('shaft',(24,8),(24,14));join('shaft','arrow')

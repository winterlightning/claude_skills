"""Phone frame is too narrow and arrowhead too short. Widen phone and enlarge the outgoing arrow while preserving side opening.
Plan: SQUARE exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: smartphone and arrow-up: rounded device, open arrowhead
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='bc63b0a1-e317-45a2-a96b-d545b39f1c83'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__mobile-phone-outgoing-arrow/20260929T135357Z-thuan-mac/reference/mobile phone call forwarding outgoing 1_bc63b0a1-e317-45a2-a96b-d545b39f1c83.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='mobile-phone-outgoing-arrow'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('mobile', 'phone', 'outgoing', 'arrow')
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

        path('phone',(28,14),[('L',(28,10)),('A',(24,6),4,4,False),('L',(10,6)),('A',(6,10),4,4,False),('L',(6,38)),('A',(10,42),4,4,False),('L',(24,42)),('A',(28,38),4,4,False),('L',(28,30))])
        line('bezel',(6,34),(28,34));join('bezel','phone')
        line('shaft',(18,22),(42,22));poly('arrow',(36,16),(42,22),(36,28));join('shaft','arrow')

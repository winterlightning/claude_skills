"""The rejected helmet has one short central stroke instead of its raised ridge, and the shoulders form a thin open arch. Restore an outlined helmet ridge and fuller shoulders.
Plan: VRECT_L exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: Lucide hard-hat: outlined central ridge and curved shell; human_ref/user.svg: round jaw and shoulders.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='cebbf3d1-bb8e-43cf-aead-55d0c45594f5'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__worker-wearing-ridged-hard-hat/20260929T145934Z-thuan-mac/reference/engineer_cebbf3d1-bb8e-43cf-aead-55d0c45594f5.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='worker-wearing-ridged-hard-hat'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('worker', 'wearing', 'ridged', 'hard', 'hat')
    human_construction = "bust"
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

        poly('ridge',(20,12),(20,4),(28,4),(28,12))
        path('shell-left',(20,8),[('A',(8,20),12,12,False),('L',(40,20)),('A',(28,8),12,12,False)]);join('ridge','shell-left')
        path('jaw',(34,20),[('A',(14,20),10,10,True)]);join('jaw','shell-left')
        path('body',(8,44),[('L',(8,40)),('A',(24,34),16,6,True),('A',(40,40),16,6,True),('L',(40,44)),('L',(8,44))],True);join('body','jaw')

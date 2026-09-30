"""The rejected police avatar removes the raised arm and V collar and changes the cap into a tall roof. Restore the raised left arm, broad cap and uniform collar.
Plan: SQUARE exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: human_ref/user.svg: circular jaw and broad shoulders; intentional raised-arm asymmetry.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='37ab5a7a-3b36-4e23-875f-657b67943fc3'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__police-avatar/20260929T145934Z-thuan-mac/reference/police_37ab5a7a-3b36-4e23-875f-657b67943fc3.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='police-avatar'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('police', 'avatar')
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

        poly('cap',(24,16),(22,6),(42,8),(40,16),(24,16))
        path('jaw',(40,16),[('A',(24,16),8,8,True)]);join('cap','jaw')
        path('body',(22,42),[('L',(22,36)),('A',(32,28),10,8,True),('A',(42,36),10,8,True),('L',(42,42))]);join('body','jaw')
        path('arm',(22,36),[('C',(6,20),(10,30),(6,26)),('L',(6,14))]);join('arm','body')

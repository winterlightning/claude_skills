"""The rejected sketch is a rigid cross in a circle on square shoulders. Curve the horizontal face guide and shoulders while preserving both construction axes.
Plan: VRECT_L exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: human_ref/user.svg: circular face and broad shoulder arcs; touching bust ink.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='fd53a710-719c-568e-86b2-b68384d280c0'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__portrait-construction-sketch/20260929T135704Z-thuan-mac/reference/draft sketch_fd53a710-719c-568e-86b2-b68384d280c0.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='portrait-construction-sketch'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('portrait', 'construction', 'sketch')
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

        path('head',(24,4),[('A',(36,16),12,12,True),('A',(24,28),12,12,True),('A',(12,16),12,12,True),('A',(24,4),12,12,True)],True)
        poly('vertical',(24,4),(24,14),(24,28));join('head','vertical')
        path('horizontal',(12,16),[('C',(24,14),(16,15),(20,14)),('C',(36,16),(28,14),(32,15))]);join('horizontal','head');join('horizontal','vertical')
        path('shoulders',(8,44),[('A',(24,32),16,12,True),('A',(40,44),16,12,True)]);join('head','shoulders')

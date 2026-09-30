"""The rejected apple is a flattened bean and its arrows are stubs. Restore a tall lobed apple with a stem above three downward arrows.
Plan: HRECT_L exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: Lucide apple: coherent lobes, stem and bottom cleft.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='3f5c0a54-044c-49ec-b70a-9297048b4eec'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__science-apple-gravity/20260929T141757Z-thuan-mac/reference/science apple gravity_3f5c0a54-044c-49ec-b70a-9297048b4eec.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='science-apple-gravity'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('science', 'apple', 'gravity')
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

        path('apple',(24,14),[('C',(10,16),(16,8),(10,10)),('C',(18,27),(10,22),(14,27)),('C',(24,26),(20,27),(22,26)),('C',(30,27),(26,26),(28,27)),('C',(38,16),(34,27),(38,22)),('C',(24,14),(38,10),(32,8))],True)
        path('stem',(24,14),[('C',(28,8),(24,11),(26,9))]);join('stem','apple')
        for x,top in ((8,32),(24,35),(40,32)):
         n='fall'+str(x);line(n,(x,top),(x,40));poly(n+'head',(x-4,36),(x,40),(x+4,36));join(n,n+'head')

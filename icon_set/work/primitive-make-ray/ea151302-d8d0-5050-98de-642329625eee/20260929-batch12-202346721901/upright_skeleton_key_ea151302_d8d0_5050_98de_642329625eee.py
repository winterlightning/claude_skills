"""Long teeth and solid stem read as an F; restore outlined shaft integrated with bow and shorter teeth.
Plan: VRECT_M exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: key-round: continuous bow-to-shaft silhouette
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='ea151302-d8d0-5050-98de-642329625eee'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__upright-skeleton-key/20260929T131521Z-thuan-mac/reference/key_ea151302-d8d0-5050-98de-642329625eee.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='upright-skeleton-key'
    keyshape=Keyshape.VRECT_M
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('upright', 'skeleton', 'key')
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

        path('key',(20,28),[('C',(10,16),(14,26),(10,22)),('A',(24,4),14,12,True),('A',(38,16),14,12,True),('C',(28,28),(38,22),(34,26)),('L',(28,40)),('A',(20,40),4,4,True),('L',(20,28))],True)
        oval('hole',24,16,3,3)
        for y in (34,42):line(f'tooth{y}',(28,y),(35,y));join(f'tooth{y}','key')

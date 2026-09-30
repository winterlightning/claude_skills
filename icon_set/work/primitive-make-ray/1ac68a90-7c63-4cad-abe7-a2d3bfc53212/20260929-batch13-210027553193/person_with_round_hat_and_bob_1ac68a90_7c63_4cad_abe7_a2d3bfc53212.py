"""Rejected portrait resembles headphones and bib; restore round hat brim with flared bob hair beside circular face.
Plan: VRECT_L exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: human_ref/user.svg: circular face and smooth shoulders; source bob silhouette
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='1ac68a90-7c63-4cad-abe7-a2d3bfc53212'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__person-with-round-hat-and-bob/20260929T135610Z-thuan-mac/reference/wide hat girl_1ac68a90-7c63-4cad-abe7-a2d3bfc53212.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='person-with-round-hat-and-bob'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('person', 'with', 'round', 'hat', 'and', 'bob')
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

        path('hat',(8,22),[('L',(8,20)),('A',(24,4),16,16,True),('A',(40,20),16,16,True),('L',(40,22))])
        oval('head',24,21,7,7)
        for s in (-1,1):
         x=lambda d:24+s*d
         path(f'hair{s}',(x(16),22),[('C',(x(16),34),(x(12),28),(x(14),32)),('L',(x(10),36))]);join(f'hair{s}','hat')
        path('body',(8,44),[('A',(24,32),16,12,True),('A',(40,44),16,12,True)]);join('head','body')

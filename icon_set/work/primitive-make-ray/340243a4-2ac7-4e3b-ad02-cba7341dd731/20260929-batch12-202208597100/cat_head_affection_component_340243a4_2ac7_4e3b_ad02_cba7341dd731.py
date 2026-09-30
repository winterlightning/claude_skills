"""Rejected drawing omits the heart and thought mark entirely. Restore heart above a compact cat head.
Plan: SQUARE exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: cat and heart: ear silhouette and rounded lobes
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='340243a4-2ac7-4e3b-ad02-cba7341dd731'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__cat-head-affection-component/20260929T131521Z-thuan-mac/reference/cat breeding_340243a4-2ac7-4e3b-ad02-cba7341dd731.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='cat-head-affection-component'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('cat', 'head', 'affection', 'component')
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

        path('cat',(6,26),[('L',(12,30)),('L',(18,30)),('L',(24,26)),('L',(24,33)),('A',(15,42),9,9,True),('A',(6,33),9,9,True),('L',(6,26))],True)
        path('heart',(32,9),[('C',(22,11),(25,1),(22,7)),('C',(32,22),(22,15),(28,19)),('C',(42,11),(36,19),(42,15)),('C',(32,9),(42,7),(39,1))],True)

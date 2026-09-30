"""The rejected selection arrow has no readable shaft, and the row is compressed into a pill. Restore a shafted arrow, a divided selected row and partial neighboring rows.
Plan: HRECT_L exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: Lucide list-indent-increase: distinct arrow and aligned content rows.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='888e184a-239b-4644-8a3e-4dd840b12966'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__row-selected-point/20260929T141753Z-thuan-mac/reference/row selected point_888e184a-239b-4644-8a3e-4dd840b12966.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='row-selected-point'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('row', 'selected', 'point')
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

        box('row',20,20,44,28,2);line('divider',(32,20),(32,28));join('divider','row')
        poly('arrow',(6,18),(12,24),(6,30));line('shaft',(4,24),(12,24));join('arrow','shaft')
        path('above',(28,12),[('L',(28,10)),('A',(30,8),2,2,True),('L',(44,8))])
        path('below',(28,36),[('L',(28,38)),('A',(30,40),2,2,False),('L',(44,40))])

"""Rejected chart uses solid nodes and a tiny magnifier handle. Restore outlined data nodes and a clearer diagonal lens handle; reduce the node count to two for space.
Plan: SQUARE; coherent source-specific contours with shared physical joins.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='f2405205-3905-48f0-b56a-6cbf57184545'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__cost-explorer/20260929T132613Z-thuan-mac/reference/cost explorer_f2405205-3905-48f0-b56a-6cbf57184545.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='cost-explorer'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('cost', 'explorer')
    def build(self):

        def path(name,start,steps,closed=False):
            here=start; members=[]
            for i,step in enumerate(steps):
                kind,end,*args=step; ident=f"{name}-{i}"
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                here=end; members.append(ident)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def join(a,b): self.relate('connect',a,b)

        def box(name,l,t,r,b,rad=0):
            if not rad:self.add_polyline(name,(l,t),(r,t),(r,b),(l,b),closed=True)
            else:path(name,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)

        self.add_polyline('axes',(6,6),(6,30),(6,42),(14,42))
        circle('point-0',17,15,3);circle('point-1',36,9,3)
        self.add_line('series-start',(6,30),(14,15));join('series-start','axes');join('series-start','point-0')
        self.add_line('series-middle',(20,15),(33,9));join('series-middle','point-0');join('series-middle','point-1')
        self.add_line('series-end',(39,9),(42,6));join('series-end','point-1')
        path('lens',(37,40),[('A',(25,24),10,10,True),('A',(37,40),10,10,True)],True)
        self.add_line('handle',(37,40),(42,42));join('handle','lens')

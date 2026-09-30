"""The rejected row is a capsule with semicircular end cells. Restore a rectangular row with modest rounded corners and three equal cells.
Plan: HRECT_M exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: Lucide columns-3: shared rectangle and evenly spaced dividers.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='0237638d-10fe-435f-be3f-042d60a75995'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__three-cell-row/20260929T145934Z-thuan-mac/reference/row selected single_0237638d-10fe-435f-be3f-042d60a75995.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='three-cell-row'
    keyshape=Keyshape.HRECT_M
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('three', 'cell', 'row')
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

        box('row',4,10,44,38,3)
        for x in (17,31):line('divider'+str(x),(x,10),(x,38));join('divider'+str(x),'row')

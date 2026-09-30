"""The rejected person loses the entire right shoulder. Restore a complete symmetrical shoulder arch and retain the circular object at lower right.
Plan: SQUARE exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: human_ref/user.svg: circular head and broad shoulders; exact detached head gap 4 ink units.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='6de68afc-a779-4fdd-b312-74634ba89fcd'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__person-with-circular-object/20260929T135704Z-thuan-mac/reference/forager_6de68afc-a779-4fdd-b312-74634ba89fcd.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='person-with-circular-object'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('person', 'with', 'circular', 'object')
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

        oval('head',24,12,6,6)
        path('body',(6,42),[('L',(6,34)),('A',(14,26),8,8,True),('L',(34,26)),('A',(42,34),8,8,True),('L',(42,42))])
        oval('object',28,38,4,4)

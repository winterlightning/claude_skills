"""Diagonal satellite with rounded main capsule, two broad solar panels and a curved dish at the lower-left end.
Keyshape SQUARE: exact SOLO48 contract envelope.
Construction: satellite: paired diagonal panels, body and attached dish
Omissions: Fine panel divisions and radiating waves omitted to protect the body/dish spacing.
Feedback: Bad stroke drawn. Fresh reference-based revision."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='ff0c5fdb-1159-4e0b-9e80-1a4fa4f96e73'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__diagonal-satellite-with-a-dish/20260924T150246Z-thuan-mac/reference/antenna 1_ff0c5fdb-1159-4e0b-9e80-1a4fa4f96e73.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='diagonal-satellite-with-a-dish'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('diagonal', 'satellite', 'with', 'a', 'dish')
    def build(self):

        def path(name, start, steps, closed=False):
            members=[]; here=start
            for i,step in enumerate(steps):
                tag=f'{name}-{i}'; kind,end,*args=step
                if kind=='L': self.add_line(tag,here,end)
                elif kind=='A': self.add_arc(tag,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(tag,here,(args[0],args[1],end))
                here=end;members.append(tag)
            self.add_contour(name,*members,closed=closed)
        def ellipse(name,x,y,rx,ry):
            path(name,(x-rx,y),[('A',(x+rx,y),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
        def box(name,l,t,r,b,rad):
            path(name,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        path('body',(22,20),[('L',(32,10)),('C',(40,18),(36,6),(44,14)),('L',(30,28)),('C',(22,20),(26,32),(18,24))],True)
        poly('panel-left',(6,14),(14,6),(24,16),(16,24),closed=True)
        poly('panel-right',(26,34),(34,26),(42,34),(34,42),closed=True)
        line('left-link',(20,20),(24,24));join('left-link','panel-left');join('left-link','body')
        line('right-link',(28,26),(30,30));join('right-link','body');join('right-link','panel-right')
        path('dish',(6,30),[('C',(18,42),(16,28),(20,32)),('L',(6,30))],True)
        line('dish-link',(18,30),(22,26));join('dish-link','body');join('dish-link','dish')

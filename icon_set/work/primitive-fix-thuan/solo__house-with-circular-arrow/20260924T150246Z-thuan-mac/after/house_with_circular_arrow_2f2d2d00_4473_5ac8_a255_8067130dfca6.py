"""House with a doorway shares a baseline with a surrounding clockwise renewal arrow.
Keyshape SQUARE: exact SOLO48 contract envelope.
Construction: house and rotate-cw: closed roof/body and continuous circular arrow
Omissions: Roof lowered to leave clearance beneath the arrowhead.
Feedback: Bad stroke drawn. Fresh reference-based revision."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='2f2d2d00-4473-5ac8-a255-8067130dfca6'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__house-with-circular-arrow/20260924T150246Z-thuan-mac/reference/renovation_2f2d2d00-4473-5ac8-a255-8067130dfca6.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='house-with-circular-arrow'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('house', 'with', 'circular', 'arrow')
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

        path('renewal-left',(10,42),[('C',(6,26),(6,38),(6,32)),('C',(24,10),(6,16),(14,10)),('C',(31,12),(27,10),(29,11))])
        poly('arrowhead',(25,6),(31,12),(25,18));join('arrowhead','renewal-left')
        path('renewal-right',(40,20),[('C',(42,26),(41,22),(42,24)),('C',(38,42),(42,34),(41,39))])
        line('baseline',(10,42),(38,42));join('baseline','renewal-left');join('baseline','renewal-right')
        poly('house',(12,42),(12,34),(24,26),(36,34),(36,42));join('house','baseline')
        poly('door',(20,42),(20,34),(28,34),(28,42));join('door','baseline')

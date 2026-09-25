"""One diagonal shaft and a joined right-angle arrowhead; common endpoint removes the tiny spurious arc.
Keyshape SQUARE: exact SOLO48 contract envelope.
Construction: arrow-down-right: shared arrowhead vertex
Omissions: None.
Feedback: Bad stroke drawn. Fresh reference-based revision."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5d1e690d-7cb8-4583-96b6-60ab81cb1101'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_03/angle down_5d1e690d-7cb8-4583-96b6-60ab81cb1101.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='angle-down'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    aliases=()
    keywords=('angle', 'down')
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

        poly('head',(20,42),(42,42),(42,20))
        line('shaft',(6,6),(42,42));join('shaft','head')

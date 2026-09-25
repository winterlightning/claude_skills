"""Diagonal barbecue fork with equal parallel tines, rounded U bend and oval-ended handle.
Keyshape SQUARE: exact SOLO48 contract envelope.
Construction: syringe and pill: diagonal parallel sides and smooth end cap
Omissions: None.
Feedback: Bad stroke drawn. Fresh reference-based revision."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3191e728-462d-507c-a5f1-052df6e82cf4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/barbecue stick_3191e728-462d-507c-a5f1-052df6e82cf4.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='barbecue-fork-two-tines'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases=()
    keywords=('barbecue', 'fork', 'two', 'tines')
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

        path('tines',(34,6),[('L',(22,18)),('C',(22,26),(18,22),(18,24)),('C',(30,26),(25,29),(27,29)),('L',(42,14))])
        line('shaft',(22,26),(17,31));join('shaft','tines')
        path('handle',(13,27),[('L',(21,35)),('L',(16,40)),('C',(12,42),(15,41),(14,42)),('A',(6,36),6,6,True),('C',(8,32),(6,34),(7,33)),('L',(13,27))],True);join('shaft','handle')

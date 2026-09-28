"""Diagonal toothbrush with a rounded outlined handle and two evenly spaced bristles on its inner head edge.
Keyshape SQUARE: exact SOLO48 contract envelope.
Construction: brush and pill: parallel diagonal tool edges with rounded terminal
Omissions: Two separated bristle strokes retained; dense extra bristles omitted.
Feedback: Bad stroke drawn. Fresh reference-based revision."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c34cfd53-4164-42f5-92e3-fa800780972e'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_38/toothbrush_c34cfd53-4164-42f5-92e3-fa800780972e.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='diagonal-manual-toothbrush'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases=()
    keywords=('diagonal', 'manual', 'toothbrush')
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

        path('body',(6,36),[('L',(30,12)),('C',(42,12),(34,8),(38,8)),('L',(12,42)),('A',(6,36),6,6,True)],True)
        for i,(x,y) in enumerate(((22,20),(30,12))):
         line(f'bristle-{i}',(x,y),(x-6,y-6));join(f'bristle-{i}','body')

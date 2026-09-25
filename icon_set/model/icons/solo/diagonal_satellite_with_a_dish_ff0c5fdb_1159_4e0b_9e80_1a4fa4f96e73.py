"""Diagonal satellite with rounded main capsule, two broad solar panels and a curved dish at the lower-left end.
Keyshape SQUARE: exact SOLO48 contract envelope.
Construction: satellite: paired diagonal panels, body and attached dish
Omissions: Fine panel divisions and radiating waves omitted to protect the body/dish spacing.
Feedback: Bad stroke drawn. Fresh reference-based revision."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ff0c5fdb-1159-4e0b-9e80-1a4fa4f96e73'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_03/antenna 1_ff0c5fdb-1159-4e0b-9e80-1a4fa4f96e73.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='diagonal-satellite-with-a-dish'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
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

        path('body',(20,22),[('L',(30,12)),('C',(36,18),(34,8),(40,14)),('L',(26,28)),('L',(20,22))],True)
        poly('panel-left',(20,22),(10,12),(16,6),(26,16));join('panel-left','body')
        poly('panel-right',(30,24),(36,30),(42,24),(36,18));join('panel-right','body')
        path('dish',(6,30),[('C',(12,30),(8,28),(10,28)),('C',(18,42),(17,33),(20,38)),('L',(6,30))],True)
        line('dish-link',(20,22),(12,30));join('dish-link','body');join('dish-link','panel-left');join('dish-link','dish')

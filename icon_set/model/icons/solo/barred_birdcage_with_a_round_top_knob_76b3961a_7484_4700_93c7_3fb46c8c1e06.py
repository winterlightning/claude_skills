"""Rounded birdcage with a true circular knob, hanging stem, domed roof and three evenly spaced bars.
Keyshape VRECT_L: exact SOLO48 contract envelope.
Construction: cooking-pot: continuous rounded enclosure; source governs dome and bars
Omissions: Extra lower rail omitted to keep open bar cells.
Feedback: Bad stroke drawn. Fresh reference-based revision."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '76b3961a-7484-4700-93c7-3fb46c8c1e06'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_06/birdcage_76b3961a-7484-4700-93c7-3fb46c8c1e06.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='barred-birdcage-with-a-round-top-knob'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('barred', 'birdcage', 'with', 'a', 'round', 'top', 'knob')
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

        ellipse('knob',24,6,2,2)
        line('stem',(24,8),(24,16));join('stem','knob')
        path('cage',(8,28),[('A',(24,16),16,12,True),('A',(40,28),16,12,True),('L',(40,44)),('L',(8,44)),('L',(8,28))],True)
        join('stem','cage')
        line('roof-rail',(8,28),(40,28));join('roof-rail','cage')
        for x in (16,24,32):
         name=f'bar-{x}';line(name,(x,28),(x,44));join(name,'roof-rail');join(name,'cage')

"""Shorebird with long sloping back, rounded head and breast, folded wing and two feet. Directional asymmetry follows reference.
Keyshape SQUARE: exact SOLO48 contract envelope.
Construction: bird: coherent sloping back and round breast
Omissions: Tiny eye omitted to avoid crowding the head.
Feedback: Bad stroke drawn. Fresh reference-based revision."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '97e41960-6ce8-41c3-8079-4ffcd2a54d73'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_31/plover_97e41960-6ce8-41c3-8079-4ffcd2a54d73.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='plover-standing-in-profile'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('plover', 'standing', 'in', 'profile')
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

        path('bird',(6,34),[('L',(12,28)),('L',(22,18)),('C',(30,6),(23,10),(25,6)),('A',(38,14),8,8,True),('L',(42,16)),('L',(38,19)),('C',(30,33),(38,27),(35,31)),('C',(24,34),(28,34),(26,34)),('L',(6,34))],True)
        path('wing',(12,28),[('C',(29,22),(23,30),(29,28))]);join('wing','bird')
        poly('leg-left',(20,34),(20,42),(16,42));join('leg-left','bird')
        poly('leg-right',(30,33),(32,42),(36,42));join('leg-right','bird')

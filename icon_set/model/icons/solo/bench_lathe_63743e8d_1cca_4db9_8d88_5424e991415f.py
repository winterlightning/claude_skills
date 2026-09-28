"""Bench lathe with rounded rectangular headstock, supported tailstock, spindle and bed.
Keyshape HRECT_L: exact SOLO48 contract envelope.
Construction: cooking-pot: tangent rounded rectangular construction
Omissions: Small spindle cap and foot recess omitted to preserve open gaps.
Feedback: Bad stroke drawn. Fresh reference-based revision."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '63743e8d-1cca-4db9-8d88-5424e991415f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_24/lathe_63743e8d-1cca-4db9-8d88-5424e991415f.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='bench-lathe'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases=()
    keywords=('bench', 'lathe')
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

        box('bed',4,32,44,40,2)
        path('headstock',(6,32),[('L',(6,11)),('A',(9,8),3,3,True),('L',(15,8)),('A',(18,11),3,3,True),('L',(18,32))]);join('headstock','bed')
        box('tailstock',32,12,44,22,2)
        line('spindle',(18,17),(32,17));join('spindle','headstock');join('spindle','tailstock')
        line('support',(38,22),(38,32));join('support','tailstock');join('support','bed')

"""Two matched circular objectives and tapered barrels with rounded upper ends, joined by a horizontal bridge.
Keyshape HRECT_L: exact SOLO48 contract envelope.
Construction: binoculars: mirrored barrels and bridge; source retains circular objectives
Omissions: None.
Feedback: Bad stroke drawn. Fresh reference-based revision."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c302c027-d345-469d-98e7-0e924b296946'
SOURCE_PATH = 'pictographic-primitives/outdoors/binoculars_c302c027-d345-469d-98e7-0e924b296946.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='binoculars'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='outdoors'
    aliases=()
    keywords=('binoculars',)
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

        for side in (-1,1):
         x=lambda d:24+side*d
         name=f'barrel-{side}'
         # Separate coherent barrel outline joins the circular lens at its lateral extremes.
         ellipse('lens'+name,x(12),32,8,8)
         path(name,(x(20),32),[('L',(x(16),14)),('C',(x(10),8),(x(15),10),(x(14),8)),('C',(x(4),14),(x(6),8),(x(4),10)),('L',(x(4),32))]);join(name,'lens'+name)
        line('bridge',(20,18),(28,18));join('bridge','barrel--1');join('bridge','barrel-1')

"""Exploration rover with two full circular wheels, a low deck, small equipment housing and a tall capped antenna.
Keyshape SQUARE: exact SOLO48 contract envelope.
Construction: tractor: full wheels below chassis and clear vehicle silhouette
Omissions: Tiny wheel hubs and secondary sloping deck details omitted.
Feedback: Bad stroke drawn. Fresh reference-based revision."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4b9bc9ba-d2b6-4767-ac5b-bbf8bd5f90c7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_26/lunar rover_4b9bc9ba-d2b6-4767-ac5b-bbf8bd5f90c7.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='exploration-rover-with-tall-antenna'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases=()
    keywords=('exploration', 'rover', 'with', 'tall', 'antenna')
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

        box('deck',6,20,42,30,2)
        for i,x in enumerate((12,36)):
         ellipse(f'wheel-{i}',x,36,6,6);join(f'wheel-{i}','deck')
        poly('equipment',(10,20),(12,12),(18,12),(18,20));join('equipment','deck')
        ellipse('antenna-tip',28,8,2,2)
        line('antenna',(28,10),(28,20));join('antenna','antenna-tip');join('antenna','deck')

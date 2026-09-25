'Three curved wind strokes sweep horizontally above and beside a large snowflake. The snowflake has six branching arms, while the wind lines curl back at their left ends.\nPlan: Three wind strokes and six-armed snowflake form one weather scene. Exact centerline extremes follow the declared SOLO48 keyshape.\nConstruction reference: Lucide wind original and atomic-debug: parallel open curls; source snowflake retained as six radial strokes.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1ffc8be7-b610-46ec-bae8-c4432ec5f9cf'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_07/blizzards 2_1ffc8be7-b610-46ec-bae8-c4432ec5f9cf.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'wind-gusts-with-snowflake'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('wind', 'gusts', 'with', 'snowflake')

    # Repair: Inset left curls to exact square bounds and shorten middle wind stroke to clear the snowflake.
    # Repair: Shorten the middle gust two more units to clear the six-armed snowflake.
    def build(self):

        def path(name,start,steps,closed=False):
            here=start; members=[]
            for j,(kind,end,*args) in enumerate(steps):
                member=f'{name}-{j}'
                if kind=='L':self.add_line(member,here,end)
                elif kind=='A':self.add_arc(member,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C':self.add_bezier(member,here,(args[0],args[1],end))
                here=end;members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def line(name,a,b):self.add_line(name,a,b)
        def poly(name,*points):self.add_polyline(name,*points,closed=points[0]==points[-1])
        def join(a,b):self.relate('connect',a,b)
        def box(name,l,t,r,b,rad=4):
            path(name,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        def oval(name,x,y,rx,ry):
            path(name,(x-rx,y),[('A',(x,y-ry),rx,ry,True),('A',(x+rx,y),rx,ry,True),('A',(x,y+ry),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)

        path('wind1',(26,6),[('A',(26,14),4,4,False),('L',(42,14))])
        path('wind2',(12,10),[('A',(12,22),6,6,False),('L',(20,22))])
        path('wind3',(16,30),[('L',(12,30)),('A',(12,42),6,6,False),('L',(16,42))])
        poly('snow1',(32,26),(32,34),(32,42));poly('snow2',(24,29),(32,34),(40,39));poly('snow3',(24,39),(32,34),(40,29));join('snow1','snow2');join('snow1','snow3');join('snow2','snow3')

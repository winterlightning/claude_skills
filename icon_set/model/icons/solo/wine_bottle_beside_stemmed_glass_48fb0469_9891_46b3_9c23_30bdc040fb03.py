'A tall wine bottle with a narrow neck and broad label band stands beside a stemmed glass. A horizontal liquid line crosses the glass above its rounded bowl and flat foot.\nPlan: Wine bottle with label beside glass, bowl, stem and foot. Exact centerline extremes follow the declared SOLO48 keyshape.\nConstruction reference: Lucide wine original and atomic-debug: bowl attached to centered stem and foot; companion bottle retained.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '48fb0469-9891-46b3-9c23-30bdc040fb03'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_10/champagne bottle glass_48fb0469-9891-46b3-9c23-30bdc040fb03.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'wine-bottle-beside-stemmed-glass'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('wine', 'bottle', 'beside', 'stemmed', 'glass')

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

        path('bottle',(6,22),[('C',(10,14),(6,18),(10,18)),('L',(10,6)),('L',(18,6)),('L',(18,14)),('C',(22,22),(18,18),(22,18)),('L',(22,32)),('L',(22,42)),('L',(6,42)),('L',(6,32)),('L',(6,22))],True)
        line('label',(6,32),(22,32));join('label','bottle')
        path('glass',(30,18),[('L',(42,18)),('L',(42,26)),('A',(36,32),6,6,True),('A',(30,26),6,6,True),('L',(30,18))],True)
        line('stem',(36,32),(36,42));poly('foot',(30,42),(36,42),(42,42));join('stem','glass');join('stem','foot')

"A single almond has a pointed top and a broad rounded base. Three long interior grooves follow its upright body, with the outer two curving along the nut's sides.\nPlan: Pointed almond outline with three long grooves. Exact centerline extremes follow the declared SOLO48 keyshape.\nConstruction reference: Lucide nut original and atomic-debug: coherent shell silhouette; source almond point retained, side grooves omitted to preserve clearance."
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '21cf2891-95c7-45ad-8e85-cab9a6e17c04'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_02/almond_21cf2891-95c7-45ad-8e85-cab9a6e17c04.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'almond-with-longitudinal-grooves'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('almond', 'with', 'longitudinal', 'grooves')

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

        path('nut',(24,4),[('C',(38,30),(34,14),(38,22)),('C',(24,44),(38,40),(32,44)),('C',(10,30),(16,44),(10,40)),('C',(24,4),(10,22),(14,14))],True)
        line('groove',(24,18),(24,34))

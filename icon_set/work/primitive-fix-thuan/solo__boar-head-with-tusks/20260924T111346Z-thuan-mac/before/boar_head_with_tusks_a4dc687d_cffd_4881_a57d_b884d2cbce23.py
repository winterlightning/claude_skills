'A boar head faces right with an upright pointed ear and a long projecting snout. A curved lower mouth frames a sharp upward tusk beneath the rounded nose.\nPlan: Boar head right profile with upright ear, projecting snout and upward tusk. Exact centerline extremes follow the declared SOLO48 keyshape.\nConstruction reference: No useful direct Lucide match; coherent contours reconstructed from the inspected original.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a4dc687d-cffd-4881-a57d-b884d2cbce23'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_07/boar_a4dc687d-cffd-4881-a57d-b884d2cbce23.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'boar-head-with-tusks'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('boar', 'head', 'with', 'tusks')

    # Repair: Raise the upper snout to give the upward tusk a clearer opening.
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

        path('head',(8,40),[('C',(4,24),(4,36),(4,30)),('C',(14,14),(4,18),(10,14)),('L',(14,8)),('C',(26,14),(20,10),(24,12)),('C',(38,18),(30,14),(30,18)),('L',(44,18)),('L',(44,30)),('L',(34,30)),('L',(28,24)),('L',(24,34)),('L',(32,34)),('L',(24,40)),('L',(8,40))],True)

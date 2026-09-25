"A woman's head faces left with a plain profile, small nose and closed lips. A swept inner hairline curves from the forehead toward the back, while long hair tapers behind the neck.\nPlan: Left-facing asymmetric profile and long swept hair; remove tiny lip/eye marks. Extrema8,4,40,44.\nConstruction reference: human_ref/user.svg facial proportion vocabulary; supplied directional head is not a generic frontal avatar."
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5a0aa177-0676-4a70-8fca-aebbf095a22b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_35/soprano_5a0aa177-0676-4a70-8fca-aebbf095a22b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'left-facing-woman-with-swept-long-hair'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('left', 'facing', 'woman', 'with', 'swept', 'long', 'hair')

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

        path('outline',(24,44),[('L',(24,36)),('L',(16,36)),('A',(12,32),4,4,True),('L',(12,28)),('L',(8,26)),('L',(12,20)),('L',(12,16)),('C',(24,4),(12,9),(17,4)),('C',(38,18),(32,4),(38,10)),('L',(38,30)),('C',(40,44),(38,35),(40,39)),('L',(24,44))],True)
        path('hairline',(12,16),[('C',(27,22),(18,16),(27,16)),('C',(29,34),(27,27),(28,31))]);join('outline','hairline')

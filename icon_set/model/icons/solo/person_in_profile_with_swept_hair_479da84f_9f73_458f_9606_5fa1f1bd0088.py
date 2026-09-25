"A person's head faces right, with a clear nose, chin, and short neck. Smooth hair sweeps across the forehead, curves around a visible ear, and ends in a flared shoulder-length section behind.\nPlan: Right-facing profile, flowing rear hair and small inner ear bend. Extrema8,4,40,44.\nConstruction reference: human_ref/user.svg facial proportion vocabulary; source direction and rear hair preserved."
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '479da84f-9f73-458f-9606-5fa1f1bd0088'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_32/redhead_479da84f-9f73-458f-9606-5fa1f1bd0088.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'person-in-profile-with-swept-hair'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('person', 'in', 'profile', 'with', 'swept', 'hair')

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

        path('outline',(24,44),[('L',(24,36)),('L',(32,36)),('A',(36,32),4,4,False),('L',(36,28)),('L',(40,26)),('L',(36,20)),('L',(36,16)),('C',(24,4),(36,9),(31,4)),('C',(10,18),(16,4),(10,10)),('L',(10,30)),('C',(8,40),(10,35),(8,37)),('L',(24,44))],True)
        path('hairline',(36,16),[('C',(22,22),(30,16),(22,16)),('C',(21,32),(22,26),(21,29))]);join('outline','hairline')

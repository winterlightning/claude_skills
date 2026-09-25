'An upright wrapped tamale with three open husk tips, a rounded packet and a smooth curved fold.\nPlan: VRECT_L exact SOLO48 envelope; coherent contours, shared parameters, 4-unit stroke.\nConstruction: candy: rounded wrapper corners; source supplies the distinctive husk tips.\nOmissions: Small wrapper creases omitted.\nFeedback: smooth centerlines, no kinks or stray nodes; preserve concept.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a83f4829-15c7-44f6-af68-a83e595af553'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_37/tamale_a83f4829-15c7-44f6-af68-a83e595af553.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='wrapped-tamale'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=()
    keywords=('wrapped', 'tamale')
    def build(self):

        def path(name,start,commands,closed=False):
            point=start; members=[]
            for i,(kind,end,*args) in enumerate(commands):
                member=f'{name}-{i}'
                if kind=='L': self.add_line(member,point,end)
                elif kind=='A': self.add_arc(member,point,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(member,point,(args[0],args[1],end))
                point=end; members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*points,closed=False): self.add_polyline(name,*points,closed=closed)
        def join(a,b): self.relate('connect',a,b)

        path('wrap',(16,18),[('L',(8,6)),('L',(18,10)),('A',(30,10),6,6,True),('L',(40,6)),('L',(32,18)),('C',(38,26),(38,18),(38,22)),('L',(38,38)),('A',(32,44),6,6,True),('L',(24,44)),('L',(16,44)),('A',(10,38),6,6,True),('L',(10,26)),('C',(16,18),(10,22),(10,18))],True)
        path('fold',(28,18),[('C',(24,44),(32,27),(28,38))]);join('fold','wrap')

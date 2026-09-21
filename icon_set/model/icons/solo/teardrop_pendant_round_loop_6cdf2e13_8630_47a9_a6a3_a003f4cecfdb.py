'A large teardrop pendant has a pointed upper tip and a broad rounded lower body. A small circular hanging loop sits directly above its tip, touching the otherwise blank pendant outline.\nPlan: Teardrop jewel below its round hanging loop, with a legal gap between distinct loops. Upright symmetry.\nConstruction reference: No useful exact Lucide match; source-specific construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6cdf2e13-8630-47a9-a6a3-a003f4cecfdb'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_30/pendant_6cdf2e13-8630-47a9-a6a3-a003f4cecfdb.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'teardrop-pendant-round-loop'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('teardrop', 'pendant', 'round', 'loop')

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

        circle('loop',24,7,3)
        path('pendant',(24,18),[('C',(38,32),(32,22),(38,27)),('A',(24,44),14,12,True),('A',(10,32),14,12,True),('C',(24,18),(10,27),(16,22))],True)

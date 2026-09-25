'Continuous expanding spiral built from tangent circular and elliptical halves with progressively wider turns.\nPlan: SQUARE exact SOLO48 envelope; coherent contours, shared parameters, 4-unit stroke.\nConstruction: lollipop: tangent semicircles at successive radii form an even spiral.\nOmissions: Innermost partial turn shortened to keep a clean center.\nFeedback: smooth centerlines, no kinks or stray nodes; preserve concept.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2a33b667-bc2b-4e32-942f-6657ff676282'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/video-games/batch-05/logo heartstone_2a33b667-bc2b-4e32-942f-6657ff676282.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='spiral-swirl'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=()
    keywords=('spiral', 'swirl')
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

        # Three half-circles, all with vertical tangents at horizontal endpoints.
        path('spiral',(24,24),[('A',(24,14),5,5,True),('A',(24,34),10,10,True),('A',(24,6),18,14,True),('A',(24,42),18,18,True)])

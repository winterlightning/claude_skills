'Left-facing witch with a gently curved pointed hat, hooked nose, rounded chin and flowing hair.\nPlan: SQUARE exact SOLO48 envelope; coherent contours, shared parameters, 4-unit stroke.\nConstruction: human_ref/user.svg reviewed for head proportions; source retains a continuous profile neck.\nOmissions: Eye, small folded hat notch and hair strand details omitted.\nFeedback: smooth centerlines, no kinks or stray nodes; preserve concept.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '60df543d-dca5-4914-a5c9-114df422b161'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/video-games/batch-13/witch_60df543d-dca5-4914-a5c9-114df422b161.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='witch-in-pointed-hat'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=()
    keywords=('witch', 'in', 'pointed', 'hat')
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

        path('hat',(6,20),[('L',(26,6)),('C',(42,20),(30,12),(38,14)),('L',(28,20)),('L',(18,20)),('L',(6,20))],True)
        path('face',(18,20),[('L',(18,29)),('L',(6,34)),('L',(16,34)),('A',(24,42),8,8,False),('L',(28,42))]);join('face','hat')
        path('hair',(28,20),[('C',(34,32),(28,26),(31,29)),('C',(40,42),(37,35),(40,38))]);join('hair','hat')

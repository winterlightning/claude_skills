'A left-facing serpent dragon with a curled body, pointed ear and large raised membranous wing.\nPlan: SQUARE exact SOLO48 envelope; coherent contours, shared parameters, 4-unit stroke.\nConstruction: bird: coherent head silhouette; source-specific curved serpent and pointed wing construction.\nOmissions: Small face details and wing veins omitted.\nFeedback: smooth centerlines, no kinks or stray nodes; preserve concept.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '73f4cc87-427b-5322-aec8-d42d4ff0929d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/video-games/batch-03/fantasy amphiptere dragon_73f4cc87-427b-5322-aec8-d42d4ff0929d.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='winged-serpent-dragon'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=()
    keywords=('winged', 'serpent', 'dragon')
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

        path('dragon',(6,26),[('L',(6,20)),('L',(16,12)),('L',(14,22)),('C',(32,32),(22,20),(23,30)),('C',(34,17),(37,28),(34,22)),('C',(42,14),(34,15),(38,14)),('C',(24,6),(37,10),(31,6)),('C',(26,20),(26,10),(27,15))])
        path('belly',(6,26),[('C',(24,42),(10,34),(15,42)),('L',(32,42)),('C',(42,34),(37,42),(41,38))]);join('belly','dragon')

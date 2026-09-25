'Sun peeking above an open-bottom cloud with a clear lightning bolt below.\nPlan: SQUARE exact SOLO48 envelope; coherent contours, shared parameters, 4-unit stroke.\nConstruction: cloud-sun: separate sun arc behind a rounded cloud, coherent cloud lobes.\nOmissions: Two lightning bolts reduced to one; small sun rays omitted for clearance.\nFeedback: smooth centerlines, no kinks or stray nodes; preserve concept.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a632e994-61fe-4267-acd7-2d4f14efccec'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-014/references/49-a632e994-61fe-4267-acd7-2d4f14efccec.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='sunny-thunderstorm'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=()
    keywords=('sunny', 'thunderstorm')
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

        path('cloud',(10,32),[('C',(6,26),(7,32),(6,30)),('C',(14,20),(6,22),(10,20)),('C',(22,14),(14,16),(18,14)),('C',(34,24),(29,14),(34,18)),('C',(42,32),(39,24),(42,27))])
        path('sun',(6,14),[('A',(22,14),8,8,True)])
        join('sun','cloud')
        poly('bolt',(26,27),(20,34),(32,34),(24,42))

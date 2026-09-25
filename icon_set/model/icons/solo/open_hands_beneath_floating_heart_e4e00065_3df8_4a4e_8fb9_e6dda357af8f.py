'Symmetric cupped hands and floating heart, matched smooth palm turns and paired lobes.\nPlan: SQUARE exact SOLO48 envelope; coherent contours, shared parameters, 4-unit stroke.\nConstruction: hand: rounded palm silhouette; human_ref/user.svg reviewed; no detached head.\nOmissions: Individual fingers reduced to two cupped hand gestures.\nFeedback: smooth centerlines, no kinks or stray nodes; preserve concept.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e4e00065-3df8-4a4e-8fb9-e6dda357af8f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_15/donation charity hand care heart_e4e00065-3df8-4a4e-8fb9-e6dda357af8f.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='open-hands-beneath-floating-heart'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=()
    keywords=('open', 'hands', 'beneath', 'floating', 'heart')
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

        path('heart',(24,11),[('A',(14,11),5,5,False),('C',(24,23),(14,16),(20,20)),('C',(34,11),(28,20),(34,16)),('A',(24,11),5,5,False)],True)
        for side in (-1,1):
         x=lambda a:24+side*a
         path(f'hand-{side}',(x(18),25),[('L',(x(18),33)),('C',(x(13),39),(x(18),36),(x(16),38)),('L',(x(8),42))])
         path(f'thumb-{side}',(x(18),33),[('C',(x(10),32),(x(15),33),(x(12),32))])
         join(f'hand-{side}',f'thumb-{side}')

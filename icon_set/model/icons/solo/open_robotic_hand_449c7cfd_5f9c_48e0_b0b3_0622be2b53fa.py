'Open robotic palm with cuff, bent thumb and raised articulated finger; smooth wrist-to-palm curves.\nPlan: HRECT_L exact SOLO48 envelope; coherent contours, shared parameters, 4-unit stroke.\nConstruction: hand and pointer: coherent outer hand contour and rounded digit tips.\nOmissions: Small finger joint seams omitted to keep the open palm clear.\nFeedback: smooth centerlines, no kinks or stray nodes; preserve concept.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '449c7cfd-5f9c-48e0-b0b3-0622be2b53fa'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/robot hand_449c7cfd-5f9c-48e0-b0b3-0622be2b53fa.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='open-robotic-hand'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    aliases=()
    keywords=('open', 'robotic', 'hand')
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

        poly('cuff',(4,15),(12,15),(12,33),(4,33))
        path('hand',(12,15),[('C',(24,8),(16,12),(19,8)),('L',(26,8)),('A',(26,16),4,4,True),('L',(23,16)),('L',(28,28)),('L',(38,18)),('C',(44,20),(41,15),(44,16)),('C',(42,27),(44,23),(44,25)),('L',(34,35)),('C',(24,40),(31,40),(28,40)),('C',(12,33),(20,40),(16,33))])
        join('cuff','hand')

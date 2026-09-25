'Right-facing head profile with a smooth rounded skull, deliberate nose corner, rounded jaw and straight neck.\nPlan: SQUARE exact SOLO48 envelope; coherent contours, shared parameters, 4-unit stroke.\nConstruction: human_ref/user.svg: simple head proportions; source preserves a continuous profile neck.\nOmissions: No essential features omitted.\nFeedback: smooth centerlines, no kinks or stray nodes; preserve concept.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = "66eefdff-ac9b-4760-951f-816ff21b1e05"
SOURCE_PATH = "pictographic-primitives/other/head_66eefdff-ac9b-4760-951f-816ff21b1e05.svg"
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='human-head-side-profile-solo'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    categories = ("container", "other", "primitives-generate")
    aliases=()
    keywords=('human', 'head', 'side', 'profile', 'solo')
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

        path('profile',(12,42),[('L',(12,32)),('C',(6,20),(8,28),(6,24)),('C',(24,6),(6,10),(14,6)),('C',(36,14),(30,6),(33,8)),('L',(42,26)),('L',(36,26)),('L',(36,28)),('A',(28,36),8,8,True),('L',(28,42))])

'A seated worker beside a laptop and a rising sun; circular head with exact four-unit detached ink gap.\nPlan: HRECT_L exact SOLO48 envelope; coherent contours, shared parameters, 4-unit stroke.\nConstruction: human_ref/full_body_ref.png and user.svg: circular head, coherent shoulder; cloud-sun: geometric sun arc.\nOmissions: Tiny laptop emblem and sun rays omitted for clearance.\nFeedback: smooth centerlines, no kinks or stray nodes; preserve concept.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '195158ad-68fb-43f8-82c7-2767217ded9c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_15/digital nomad sun_195158ad-68fb-43f8-82c7-2767217ded9c.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='laptop-worker-beneath-sun-and-horizon'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases=()
    keywords=('laptop', 'worker', 'beneath', 'sun', 'and', 'horizon')
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

        circle('head',39,21,5)
        # Head bottom 26; torso starts 34: eight centerline units / four ink units.
        path('body',(39,34),[('C',(44,40),(39,38),(40,40))])
        self.mark_human_figure('worker',head='head',torso='body-0',torso_junction='start')
        path('laptop',(9,40),[('L',(4,25)),('L',(25,25)),('L',(30,40)),('L',(9,40))],True)
        path('sun',(5,16),[('A',(21,16),8,8,True)])

'Side-view steam locomotive with cab, rounded boiler front, chimney and three circular wheels.\nPlan: HRECT_L exact SOLO48 envelope; coherent contours, shared parameters, 4-unit stroke.\nConstruction: train-front: round wheels and coherent mechanical contours.\nOmissions: Small wheel hubs and cowcatcher teeth omitted.\nFeedback: smooth centerlines, no kinks or stray nodes; preserve concept.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f80a174d-7812-44f5-9ee2-c2d09024d923'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_36/steam engine_f80a174d-7812-44f5-9ee2-c2d09024d923.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='three-wheel-steam-locomotive'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases=()
    keywords=('three', 'wheel', 'steam', 'locomotive')
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

        poly('cab',(4,34),(4,8),(16,8),(16,16),(16,24),(16,34))
        path('boiler',(16,16),[('L',(27,16)),('L',(35,16)),('L',(36,16)),('A',(40,20),4,4,True),('L',(40,24)),('L',(16,24))]);join('boiler','cab')
        poly('chimney',(27,16),(27,8),(35,8),(35,16));join('chimney','boiler')
        circle('rear-wheel',10,34,6);join('rear-wheel','cab')
        for x in (27,41):circle(f'wheel-{x}',x,37,3)
        line('front',(40,24),(44,24));join('front','boiler')

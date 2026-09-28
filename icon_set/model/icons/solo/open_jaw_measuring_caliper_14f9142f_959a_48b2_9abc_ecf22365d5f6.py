'Upright measuring caliper with squared jaws and a straight sliding beam; rounded lower outer corner.\nPlan: VRECT_L exact SOLO48 envelope; coherent contours, shared parameters, 4-unit stroke.\nConstruction: pencil-ruler: straight measurement-tool edges with deliberate corners.\nOmissions: Fine ruler graduations and small jaw steps omitted.\nFeedback: smooth centerlines, no kinks or stray nodes; preserve concept.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '14f9142f-959a-48b2-9abc-ecf22365d5f6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_09/caliper_14f9142f-959a-48b2-9abc-ecf22365d5f6.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='open-jaw-measuring-caliper'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases=()
    keywords=('open', 'jaw', 'measuring', 'caliper')
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

        # Rail, fixed jaw and moving jaw own shared attachment points.
        poly('rail',(28,4),(28,12),(40,12),(40,20),(28,20),(28,28),(28,38),(28,44))
        poly('upper-jaw',(28,4),(8,4),(8,16),(16,16),(16,12),(28,12));join('upper-jaw','rail')
        path('lower-jaw',(28,28),[('L',(16,28)),('L',(16,24)),('L',(8,24)),('L',(8,30)),('A',(16,38),8,8,False),('L',(28,38))]);join('lower-jaw','rail')

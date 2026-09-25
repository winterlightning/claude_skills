'Winged monument with a circular head, smooth shoulder, raised leaf-shaped wing and rectangular pedestal.\nPlan: VRECT_L exact SOLO48 envelope; coherent contours, shared parameters, 4-unit stroke.\nConstruction: human_ref/user.svg: rounded head and shoulder; source defines the raised single wing.\nOmissions: Pedestal molding reduced to one rectangle.\nFeedback: smooth centerlines, no kinks or stray nodes; preserve concept.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b8975bc1-4fe4-47c7-82bd-a46a322d6fc6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_03/angel of independence mexico_b8975bc1-4fe4-47c7-82bd-a46a322d6fc6.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='winged-monument-on-a-pedestal'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=()
    keywords=('winged', 'monument', 'on', 'a', 'pedestal')
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

        circle('head',16,9,5)
        path('body',(8,34),[('L',(8,30)),('A',(16,22),8,8,True),('L',(22,22)),('L',(22,34))])
        path('wing',(22,22),[('C',(40,4),(30,22),(28,4)),('C',(22,22),(40,14),(33,22))],True);join('wing','body')
        poly('pedestal',(8,34),(22,34),(30,34),(30,44),(8,44),(8,34));join('pedestal','body')

'Standing woman beside a rounded baby carriage with quarter-circle hood and two wheels.\nPlan: SQUARE exact SOLO48 envelope; coherent contours, shared parameters, 4-unit stroke.\nConstruction: human_ref/full_body_ref.png: circular head and flared dress; truck: circular wheels.\nOmissions: Hair, dress creases and separate feet omitted; two wheels retained.\nFeedback: smooth centerlines, no kinks or stray nodes; preserve concept.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7ef89486-f781-4238-b1ba-7f9d5858262e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_05/baby trolley_7ef89486-f781-4238-b1ba-7f9d5858262e.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='woman-standing-beside-a-baby-carriage-7ef89486'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases=()
    keywords=('woman', 'standing', 'beside', 'a', 'baby', 'carriage', '7ef89486')
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

        circle('head',11,10,4)
        path('dress',(6,36),[('C',(11,22),(6,28),(7,22)),('C',(16,36),(15,22),(16,28)),('L',(11,36)),('L',(6,36))],True)
        line('leg',(11,36),(11,42));join('leg','dress')
        path('carriage',(24,22),[('C',(34,30),(24,28),(28,30)),('C',(42,22),(40,30),(42,28))])
        path('hood',(32,12),[('A',(42,22),10,10,True)]);join('hood','carriage')
        poly('hood-rim',(32,12),(32,22),(42,22));join('hood-rim','hood');join('hood-rim','carriage')
        for x in (27,40):circle(f'wheel-{x}',x,40,2)

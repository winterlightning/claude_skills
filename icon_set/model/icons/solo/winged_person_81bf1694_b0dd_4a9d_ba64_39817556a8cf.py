'A standing person with a circular head, straight torso, two rounded wings and balanced legs.\nPlan: SQUARE exact SOLO48 envelope; coherent contours, shared parameters, 4-unit stroke.\nConstruction: human_ref/full_body_ref.png and user-round: circular head and simple limbs; source supplies rounded wings.\nOmissions: Finger and individual feather details omitted.\nFeedback: smooth centerlines, no kinks or stray nodes; preserve concept.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '81bf1694-b0dd-4a9d-ba64-39817556a8cf'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_40/wingman_81bf1694-b0dd-4a9d-ba64-39817556a8cf.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='winged-person'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases=()
    keywords=('winged', 'person')
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

        circle('head',24,10,4)
        poly('torso',(24,22),(24,24),(24,34))
        self.mark_human_figure('person',head='head',torso='torso-1',torso_junction='start')
        for side in (-1,1):
         x=lambda d:24+side*d
         path(f'wing-{side}',(24,24),[('C',(x(18),24),(x(8),18),(x(18),19)),('C',(x(10),33),(x(18),30),(x(15),33)),('L',(x(8),33))])
         join(f'wing-{side}','torso')
        join('wing--1','wing-1')
        poly('legs',(18,42),(24,34),(30,42));join('legs','torso')

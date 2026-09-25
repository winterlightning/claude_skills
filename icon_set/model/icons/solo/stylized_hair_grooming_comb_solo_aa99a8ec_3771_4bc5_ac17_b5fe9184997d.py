'A diagonal grooming comb with evenly spaced straight teeth and one smooth upturned spine end.\nPlan: HRECT_L exact SOLO48 envelope; coherent contours, shared parameters, 4-unit stroke.\nConstruction: pencil-ruler: exact diagonal runs and shared attachment points; source-specific comb silhouette.\nOmissions: Fine extra teeth omitted.\nFeedback: smooth centerlines, no kinks or stray nodes; preserve concept.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'aa99a8ec-3771-4bc5-ac17-b5fe9184997d'
SOURCE_PATH = 'pictographic-primitives/other/comb_aa99a8ec-3771-4bc5-ac17-b5fe9184997d.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='stylized-hair-grooming-comb-solo'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/interface-essential"
    aliases=()
    keywords=('stylized', 'hair', 'grooming', 'comb', 'solo')
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

        path('spine',(4,40),[('L',(8,37)),('L',(20,28)),('L',(32,19)),('L',(36,16)),('C',(44,8),(40,13),(44,11))])
        for i,(x,y) in enumerate(((8,37),(20,28),(32,19))):
         line(f'tooth-{i}',(x,y),(x-4,y-6));join(f'tooth-{i}','spine')

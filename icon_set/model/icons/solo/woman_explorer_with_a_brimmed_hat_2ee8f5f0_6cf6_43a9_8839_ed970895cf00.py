'Explorer portrait with a broad rounded hat, circular jaw, side hair and smooth shoulders.\nPlan: VRECT_L exact SOLO48 envelope; coherent contours, shared parameters, 4-unit stroke.\nConstruction: human_ref/user.svg and user-round: circular face and matched shoulders; bust ink contact follows the shared human contract.\nOmissions: Backpack straps and tiny hat bands omitted.\nFeedback: smooth centerlines, no kinks or stray nodes; preserve concept.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2ee8f5f0-6cf6-43a9-8839-ed970895cf00'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_05/avatar adventure woman_2ee8f5f0-6cf6-43a9-8839-ed970895cf00.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='woman-explorer-with-a-brimmed-hat'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    aliases=()
    keywords=('woman', 'explorer', 'with', 'a', 'brimmed', 'hat')
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

        self.human_construction='bust'
        path('hat',(12,16),[('L',(12,10)),('C',(24,4),(12,6),(19,4)),('C',(36,10),(29,4),(36,6)),('L',(36,16))])
        poly('brim',(8,16),(12,16),(14,16),(34,16),(36,16),(40,16));join('hat','brim')
        path('jaw',(34,16),[('A',(14,16),10,10,True)]);join('jaw','brim')
        for side in (-1,1):
         x=lambda d:24+side*d
         path(f'hair-{side}',(x(10),16),[('C',(x(12),23),(x(10),19),(x(10),21)),('C',(x(16),25),(x(14),25),(x(15),25))]);join(f'hair-{side}','jaw');join(f'hair-{side}','brim')
        path('shoulders',(8,44),[('A',(24,30),16,14,True),('A',(40,44),16,14,True)])
        # Jaw bottom 26; shoulder apex 30: four centerline units, zero visible ink gap.
        join('jaw','shoulders')

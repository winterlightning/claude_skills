'Rounded tied bag beside a tapered bin with a protruding piece of rubbish; clean symmetrical bag and straight bin edges.\nPlan: SQUARE exact SOLO48 envelope; coherent contours, shared parameters, 4-unit stroke.\nConstruction: droplet: smooth rounded bag base; source-specific bin arrangement.\nOmissions: Small garbage details omitted.\nFeedback: smooth centerlines, no kinks or stray nodes; preserve concept.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2295a288-f526-406a-ae2e-c1f6bc4d44eb'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/ecology/garbage_2295a288-f526-406a-ae2e-c1f6bc4d44eb.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='tied-garbage-bag-beside-filled-trash-bin'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "ecology"
    aliases=()
    keywords=('tied', 'garbage', 'bag', 'beside', 'filled', 'trash', 'bin')
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

        poly('bin',(30,16),(40,16),(42,16),(39,42),(16,42))
        poly('rubbish',(30,16),(30,6),(42,8),(40,16));join('bin','rubbish')
        path('bag',(16,26),[('C',(6,36),(10,26),(6,31)),('C',(16,42),(6,40),(10,42)),('C',(26,36),(22,42),(26,40)),('C',(16,26),(26,31),(22,26))],True)
        poly('tie',(16,26),(10,16),(22,16),(16,26));join('tie','bag');join('bag','bin')

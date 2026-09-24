'Rounded paddle blade, diagonal handle and separate circular ball.\nPlan: SQUARE exact SOLO48 envelope; coherent contours, shared parameters, 4-unit stroke.\nConstruction: lollipop: circular dominant head; pencil-ruler: clean diagonal grip.\nOmissions: Blade seam omitted to preserve room around the separate ball.\nFeedback: smooth centerlines, no kinks or stray nodes; preserve concept.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='86d364a5-4269-4e31-96c0-ecd253882fab'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__table-tennis-paddle-ball/20260924T162030Z-thuan-mac/reference/ping pong paddle_86d364a5-4269-4e31-96c0-ecd253882fab.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='table-tennis-paddle-ball'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=()
    keywords=('table', 'tennis', 'paddle', 'ball')
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

        circle('ball',10,10,4)
        path('paddle',(18,26),[('C',(28,14),(18,19),(21,14)),('C',(42,28),(36,14),(42,20)),('C',(28,40),(42,35),(36,40)),('C',(24,38),(26,40),(25,39)),('L',(14,42)),('L',(6,34)),('L',(16,28)),('C',(18,26),(17,27),(18,27))],True)

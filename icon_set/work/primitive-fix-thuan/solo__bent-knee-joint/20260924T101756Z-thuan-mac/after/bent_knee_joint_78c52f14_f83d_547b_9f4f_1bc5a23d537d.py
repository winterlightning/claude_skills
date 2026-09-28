"""Two rounded bone ends form a bent knee with a clear joint gap. Bounds (8,4)-(40,44). Lower tibia centered beneath the femoral condyles.
Construction reference: Lucide bone: rounded paired bone ends; human full-body reference for limb continuity.
Omissions: Fine bone surface undulations simplified."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='78c52f14-f83d-547b-9f4f-1bc5a23d537d'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__bent-knee-joint/20260924T101756Z-thuan-mac/reference/specialty knee_78c52f14-f83d-547b-9f4f-1bc5a23d537d.svg'
AUTHOR="gpt-6"

class Drawing(Solo48):
    icon_id='bent-knee-joint'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=()
    keywords=('specialty', 'knee')
    def build(self):

        def path(name,start,commands,closed=False):
            here=start; members=[]
            for i,(kind,end,*args) in enumerate(commands):
                ident=f'{name}-{i}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                members.append(ident); here=end
            self.add_contour(name,*members,closed=closed)
        def oval(name,cx,cy,rx,ry):
            path(name,(cx-rx,cy),[('A',(cx+rx,cy),rx,ry,True),('A',(cx-rx,cy),rx,ry,True)],True)
        line=self.add_line; poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)
        path('femur',(8,8),[('L',(20,20)),('L',(20,23)),('C',(25,25),(20,25),(23,27)),('C',(30,22),(27,25),(27,22)),('C',(35,24),(32,22),(32,24)),('C',(40,21),(38,26),(40,25)),('C',(35,17),(40,19),(38,18)),('L',(22,4))])
        path('tibia',(23,44),[('L',(23,38)),('C',(22,35),(22,37),(21,35)),('C',(29,36),(24,35),(27,37)),('C',(37,35),(33,35),(37,35)),('C',(36,39),(38,37),(36,38)),('L',(36,44))])

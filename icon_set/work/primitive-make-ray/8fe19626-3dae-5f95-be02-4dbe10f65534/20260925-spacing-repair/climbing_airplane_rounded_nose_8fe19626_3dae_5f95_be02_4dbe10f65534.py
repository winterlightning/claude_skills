"""Side-view climbing airplane, with a smooth round nose, upper swept wing, broad lower wing and raised tail. Bounds4,8 to44,40.
Construction reference: Lucide plane-takeoff: coherent fuselage and tapered wings.
Omissions: No windows in source; retained both wings.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '8fe19626-3dae-5f95-be02-4dbe10f65534'
SOURCE_PATH = 'pictographic-primitives/travel/plane 1_8fe19626-3dae-5f95-be02-4dbe10f65534.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'climbing-airplane-rounded-nose'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/travel'
    aliases = ()
    keywords = ('plane', '1')
    def build(self):
        self.path('plane',(4,24),[('L',(10,24)),('L',(14,28)),('L',(23,24)),('L',(11,10)),('L',(21,8)),('L',(33,20)),('L',(36,19)),('C',(44,24),(40,18),(44,21)),('C',(38,29),(44,27),(42,28)),('L',(34,30)),('L',(29,40)),('L',(19,40)),('L',(24,30)),('L',(13,35)),('C',(8,32),(11,36),(9,35)),('L',(4,24))],True)

    def path(self, name, start, commands, closed=False):
        members=[]
        for i,c in enumerate(commands):
            ident=f'{name}-{i}'
            if c[0]=='L': end=c[1];self.add_line(ident,start,end)
            elif c[0]=='A':
                _,end,rx,ry,sweep=c
                self.add_arc(ident,start,end,radius_x=rx,radius_y=ry,sweep=sweep)
            elif c[0]=='C':
                _,end,c1,c2=c
                self.add_bezier(ident,start,(c1,c2,end))
            members.append(ident);start=end
        self.add_contour(name,*members,closed=closed)
    def circle(self,name,x,y,r):
        self.path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)

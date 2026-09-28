"""Side-view climbing airplane, with a smooth round nose, upper swept wing, broad lower wing and raised tail. Bounds4,8 to44,40.
Construction reference: Lucide plane-takeoff: coherent fuselage and tapered wings.
Omissions: No windows in source; retained both wings.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '8fe19626-3dae-5f95-be02-4dbe10f65534'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__climbing-airplane-rounded-nose/20260924T092136Z-thuan-mac/reference/plane 1_8fe19626-3dae-5f95-be02-4dbe10f65534.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'climbing-airplane-rounded-nose'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/other'
    aliases = ()
    keywords = ('plane', '1')
    def build(self):
        self.path('plane',(4,22),[('L',(9,21)),('L',(14,25)),('L',(21,23)),('L',(13,10)),('L',(19,8)),('L',(31,20)),('L',(36,18)),('C',(44,23),(40,17),(44,20)),('C',(39,27),(44,25),(42,26)),('L',(29,30)),('L',(23,40)),('L',(16,40)),('L',(20,31)),('L',(13,35)),('C',(7,29),(10,36),(8,32)),('L',(4,22))],True)

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

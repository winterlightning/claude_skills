"""Top-view sea turtle with an elongated head, divided shell and four swept flippers. Shared mirror axis x24 and equal limb curves. SQUARE centerlines (6,6)-(42,42)."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='1adaf0a7-6662-4745-959f-fe860dd47485'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__sea-turtle/20260924T101756Z-thuan-mac/reference/turtle_1adaf0a7-6662-4745-959f-fe860dd47485.svg'
AUTHOR='gpt-6'
CONSTRUCTION_REFERENCE='turtle: shell with attached limbs; source owns the top view'
DESIGN_PLAN='Top-view sea turtle with an elongated head, divided shell and four swept flippers. Shared mirror axis x24 and equal limb curves. SQUARE centerlines (6,6)-(42,42).'
OMISSIONS='None; fine shell pattern reduced to the source central seam.'
class Drawing(Solo48):
    icon_id='sea-turtle-solo'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'animals'
    categories = ('animals', 'primitives')
    aliases=()
    keywords=('sea', 'turtle')
    def path(self, name, start, commands, closed=False):
        members=[]
        for i,(kind,end,*args) in enumerate(commands):
            member=f'{name}-{i}'
            if kind=='L': self.add_line(member,start,end)
            elif kind=='A': self.add_arc(member,start,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            elif kind=='C': self.add_bezier(member,start,(args[0],args[1],end))
            members.append(member); start=end
        self.add_contour(name,*members,closed=closed)

    def circle(self,name,cx,cy,r):
        self.path(name,(cx-r,cy),[('A',(cx,cy-r),r,r,True),('A',(cx+r,cy),r,r,True),('A',(cx,cy+r),r,r,True),('A',(cx-r,cy),r,r,True)],True)



    def build(self):
        self.path('shell',(24,16),[('C',(16,20),(20,16),(16,17)),('L',(16,24)),('L',(16,32)),('C',(20,38),(16,35),(18,37)),('C',(24,40),(21,39),(22,40)),('C',(28,38),(26,40),(27,39)),('C',(32,32),(30,37),(32,35)),('L',(32,24)),('L',(32,20)),('C',(24,16),(32,17),(28,16))],True)
        self.path('head',(24,16),[('C',(20,10),(20,14),(20,12)),('C',(24,6),(20,8),(22,6)),('C',(28,10),(26,6),(28,8)),('C',(24,16),(28,12),(28,14))],True);self.relate('connect','head','shell')
        self.add_line('seam',(24,16),(24,40));self.relate('connect','seam','shell');self.relate('connect','seam','head')
        for side in (-1,1):
            p=lambda x,y:(24+side*(x-24),y)
            self.path(f'front-{side}',p(16,20),[('C',p(6,26),p(12,15),p(6,21)),('C',p(16,24),p(10,27),p(12,26))]);self.relate('connect',f'front-{side}','shell')
            self.path(f'rear-{side}',p(16,32),[('C',p(12,42),p(12,35),p(10,39)),('C',p(20,38),p(16,42),p(18,41))]);self.relate('connect',f'rear-{side}','shell')

"""A toothed saw blade projects above a table, with a semicircular hub opening. HRECT_M centerlines (4,10)-(44,38). Broad hooked teeth and smoothly curved gullets replace the jagged mountain-like outline."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='e168add6-d08c-5ea9-9a91-bf194256b3a5'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__sawmill/20260924T101756Z-thuan-mac/reference/sawmill_e168add6-d08c-5ea9-9a91-bf194256b3a5.svg'
AUTHOR='gpt-6'
CONSTRUCTION_REFERENCE='cog: repeated radial cutting structures; supplied reference owns hooked saw teeth'
DESIGN_PLAN='A toothed saw blade projects above a table, with a semicircular hub opening. HRECT_M centerlines (4,10)-(44,38). Broad hooked teeth and smoothly curved gullets replace the jagged mountain-like outline.'
OMISSIONS='Tooth count reduced to preserve readable gullets.'
class Drawing(Solo48):
    icon_id='sawmill'
    keyshape=Keyshape.HRECT_M
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('sawmill',)
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
        self.path('blade',(8,38),[('C',(8,30),(11,35),(12,31)),('L',(4,28)),('C',(14,26),(9,25),(12,25)),('L',(10,18)),('C',(21,20),(15,16),(20,17)),('L',(20,10)),('C',(30,18),(26,10),(29,14)),('L',(34,12)),('C',(37,25),(39,16),(39,20)),('L',(44,23)),('C',(40,38),(44,30),(42,34))])
        self.add_polyline('table',(4,38),(8,38),(16,38),(32,38),(40,38),(44,38));self.relate('connect','table','blade')
        self.path('hub',(16,38),[('A',(24,30),8,8,True),('A',(32,38),8,8,True)]);self.relate('connect','hub','table')

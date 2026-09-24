"""Long diagonal sporting rifle with broad shouldered stock. SQUARE centerlines (6,6)-(42,42). An outlined shoulder stock, enlarged trigger guard and long barrel preserve the rifle silhouette."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='0f979459-ea45-4f2e-b3ab-3ab2403cc849'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__long-sporting-rifle/20260924T101756Z-thuan-mac/reference/rifle_0f979459-ea45-4f2e-b3ab-3ab2403cc849.svg'
AUTHOR='gpt-6'
CONSTRUCTION_REFERENCE='No useful local Lucide rifle match'
DESIGN_PLAN='Long diagonal sporting rifle with broad shouldered stock. SQUARE centerlines (6,6)-(42,42). An outlined shoulder stock, enlarged trigger guard and long barrel preserve the rifle silhouette.'
OMISSIONS='Doubled barrel edge reduced to one stroke; trigger guard retained and enlarged.'
class Drawing(Solo48):
    icon_id='long-sporting-rifle'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('long', 'sporting', 'rifle')
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
        self.add_polyline('stock',(6,34),(14,42),(20,32),(26,24),(20,20),(16,26),(12,28),closed=True)
        self.add_line('barrel',(26,24),(42,6));self.relate('connect','barrel','stock')
        self.path('trigger-guard',(26,24),[('C',(34,30),(30,24),(34,26)),('C',(28,38),(34,34),(32,38)),('L',(20,32))]);self.relate('connect','trigger-guard','stock');self.relate('connect','trigger-guard','barrel')

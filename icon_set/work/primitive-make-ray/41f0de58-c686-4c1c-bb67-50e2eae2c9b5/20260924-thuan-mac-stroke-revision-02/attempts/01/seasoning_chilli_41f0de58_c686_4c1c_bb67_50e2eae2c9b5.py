"""Curved chilli pepper with broad shoulder, wavy calyx seam and rising stem. SQUARE centerlines (6,6)-(42,42). Smooth return curves retain the pointed left tip and full lower belly."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='41f0de58-c686-4c1c-bb67-50e2eae2c9b5'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__seasoning-chilli/20260924T101756Z-thuan-mac/reference/seasoning chilli_41f0de58-c686-4c1c-bb67-50e2eae2c9b5.svg'
AUTHOR='gpt-6'
CONSTRUCTION_REFERENCE='No useful direct Lucide chilli match'
DESIGN_PLAN='Curved chilli pepper with broad shoulder, wavy calyx seam and rising stem. SQUARE centerlines (6,6)-(42,42). Smooth return curves retain the pointed left tip and full lower belly.'
OMISSIONS='None.'
class Drawing(Solo48):
    icon_id='seasoning-chilli'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('seasoning', 'chilli')
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
        self.path('pepper',(28,20),[('C',(34,12),(28,15),(30,12)),('C',(40,20),(38,12),(40,15)),('L',(40,24)),('C',(24,42),(40,35),(33,42)),('C',(6,32),(15,42),(9,38)),('C',(28,24),(17,38),(28,33)),('L',(28,20))],True)
        self.path('calyx',(28,24),[('C',(40,24),(32,28),(36,28))]);self.relate('connect','pepper','calyx')
        self.path('stem',(34,12),[('C',(42,6),(34,8),(38,6))]);self.relate('connect','stem','pepper')

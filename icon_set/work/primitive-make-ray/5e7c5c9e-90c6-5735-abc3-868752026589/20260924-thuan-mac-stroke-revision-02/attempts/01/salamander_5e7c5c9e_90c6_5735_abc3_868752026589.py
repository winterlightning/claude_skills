"""Salamander with a rounded head, three visible limbs and a returning tail curl. SQUARE centerlines (6,6)-(42,42). Replace angular tail joins with tangent arcs and enlarge the limb gestures."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='5e7c5c9e-90c6-5735-abc3-868752026589'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__salamander/20260924T101756Z-thuan-mac/reference/amphibian chameleon_5e7c5c9e-90c6-5735-abc3-868752026589.svg'
AUTHOR='gpt-6'
CONSTRUCTION_REFERENCE='No exact Lucide match; source establishes head, limbs and curled tail'
DESIGN_PLAN='Salamander with a rounded head, three visible limbs and a returning tail curl. SQUARE centerlines (6,6)-(42,42). Replace angular tail joins with tangent arcs and enlarge the limb gestures.'
OMISSIONS='Tiny limb bends reduced to short strokes.'
class Drawing(Solo48):
    icon_id='salamander'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('salamander',)
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
        self.path('body',(12,15),[('A',(20,6),8,9,True),('A',(28,15),8,9,True),('L',(28,16)),('L',(28,26)),('A',(36,26),4,4,False),('A',(42,26),3,3,True),('A',(28,42),14,16,True),('A',(12,26),16,16,True),('L',(12,18)),('L',(12,15))],True)
        self.add_dot('eye',(20,15))
        self.add_line('fore-left',(12,18),(6,20));self.relate('connect','fore-left','body')
        self.add_line('hind-left',(12,26),(6,30));self.relate('connect','hind-left','body')
        self.add_line('fore-right',(28,16),(36,14));self.relate('connect','fore-right','body')

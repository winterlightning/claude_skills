"""The rejected volleyball has only three sections; restore a second curved seam in each visible panel group. No written reviewer feedback.
Added a curved panel seam and rebuilt the circular rim with exact shared attachment points.
Construction: Lucide volleyball original and atomic-debug: curved panels and shared junctions.
Omissions: Four broad seams replace finer repeated source seams.
Keyshape: CIRCLE. Radial centerline limit 20 around (24,24), preserving the natural circular or slender subject proportions.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='81273324-0457-42f4-b9e3-f24d809cec3b'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__volleyball-panel-ball/20260929T121814Z-thuan-mac/reference/volleyball ball_81273324-0457-42f4-b9e3-f24d809cec3b.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='volleyball-panel-ball'
    keyshape=Keyshape.CIRCLE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='primitives-generate'
    aliases=()
    keywords=('volleyball', 'panel', 'ball')

    def path(self,n,start,ops,closed=False):
        here=start; members=[]
        for i,(kind,end,*args) in enumerate(ops):
            m=f'{n}-{i}'
            if kind=='L': self.add_line(m,here,end)
            elif kind=='A': self.add_arc(m,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            elif kind=='C': self.add_bezier(m,here,(args[0],args[1],end))
            members.append(m); here=end
        self.add_contour(n,*members,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x,y-r),[('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True),('A',(x,y-r),r,r,True)],True)

    def build(self):

        self.path('ball',(24,4),[('A',(40,12),20,20,True),('A',(44,24),20,20,True),('A',(24,44),20,20,True),('A',(12,40),20,20,True),('A',(4,24),20,20,True),('A',(24,4),20,20,True)],True)
        self.path('sweep',(24,4),[('C',(20,16),(21,8),(20,12)),('C',(24,24),(20,20),(21,23)),('C',(44,24),(31,28),(39,28))]);self.relate('connect','sweep','ball')
        self.path('lower',(24,24),[('C',(12,40),(15,26),(13,33))]);self.relate('connect','lower','sweep');self.relate('connect','lower','ball')
        self.path('panel-top',(40,12),[('C',(20,16),(33,9),(25,10))]);self.relate('connect','panel-top','ball');self.relate('connect','panel-top','sweep')


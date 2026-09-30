"""The rejected hill is a shallow flattened strip; restore a tall rounded hill beneath the partly hidden sun. No written feedback.
Symbol plan: Lucide sunrise: separated radial rays and partial sun. Reference hill restored; only three main rays retained.
Keyshape VRECT_L, authored on the SOLO48 integer grid with 4-unit strokes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='9209ad15-ccc6-48e1-b297-b65ddf79ec66'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__sun-appearing-behind-rounded-hill/20260929T115301Z-thuan-mac/reference/day noon_9209ad15-ccc6-48e1-b297-b65ddf79ec66.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='sun-appearing-behind-rounded-hill'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='primitives-generate'
    aliases=()
    keywords=('sun', 'appearing', 'behind', 'rounded', 'hill')

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

        self.path('hill',(8,44),[('C',(12,34),(8,40),(10,36)),('C',(24,28),(15,30),(20,28)),('C',(36,34),(28,28),(33,30)),('C',(40,44),(38,36),(40,40)),('L',(8,44))],True)
        self.path('sun',(12,34),[('A',(36,34),12,18,True)]);self.relate('connect','sun','hill')
        self.add_line('ray-top',(24,4),(24,8))
        self.add_line('ray-left',(8,16),(10,18))
        self.add_line('ray-right',(38,18),(40,16))

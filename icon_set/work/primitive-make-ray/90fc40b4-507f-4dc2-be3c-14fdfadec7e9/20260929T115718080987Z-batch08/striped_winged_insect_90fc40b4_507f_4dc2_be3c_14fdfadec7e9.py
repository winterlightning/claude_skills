"""The rejected insect has an angular head and drooping wings; restore a round head, oval wings and a segmented abdomen. No written feedback.
Rounded the head, added a thorax boundary, restored paired legs, and lifted the mirrored wings.
Lucide bug original and atomic-debug: paired antennae and structured body. Symmetric head/body, mirrored wings and legs.
Omissions: Fine leg bends and additional narrow abdominal bands reduced; two legs and one abdominal stripe retained.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='90fc40b4-507f-4dc2-be3c-14fdfadec7e9'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__striped-winged-insect/20260929T115301Z-thuan-mac/reference/gnat_90fc40b4-507f-4dc2-be3c-14fdfadec7e9.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='striped-winged-insect'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='primitives-generate'
    aliases=()
    keywords=('striped', 'winged', 'insect')

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

        self.circle('head',24,10,4)
        self.add_line('antenna-left',(20,10),(16,6)); self.relate('connect','antenna-left','head')
        self.add_line('antenna-right',(28,10),(32,6)); self.relate('connect','antenna-right','head')
        self.path('body',(24,14),[('C',(30,24),(29,14),(30,18)),('L',(30,32)),('C',(24,42),(30,37),(27,41)),('C',(18,32),(21,41),(18,37)),('L',(18,24)),('C',(24,14),(18,18),(19,14))],True)
        self.relate('connect','head','body')
        self.add_line('stripe',(18,32),(30,32));self.relate('connect','stripe','body')
        self.add_line('thorax-end',(18,24),(30,24));self.relate('connect','thorax-end','body')
        self.path('wing-left',(18,24),[('C',(6,23),(12,17),(6,17)),('C',(18,32),(6,30),(11,34))]);self.relate('connect','wing-left','body')
        self.path('wing-right',(30,24),[('C',(42,23),(36,17),(42,17)),('C',(30,32),(42,30),(37,34))]);self.relate('connect','wing-right','body')
        for side in ('left','right'):
            self.relate('connect',f'wing-{side}','thorax-end')
            self.relate('connect',f'wing-{side}','stripe')
        self.add_polyline('leg-left',(18,32),(10,38),(8,42));self.add_polyline('leg-right',(30,32),(38,38),(40,42))
        for side in ('left','right'):
            self.relate('connect',f'leg-{side}','body');self.relate('connect',f'leg-{side}',f'wing-{side}');self.relate('connect',f'leg-{side}','stripe')

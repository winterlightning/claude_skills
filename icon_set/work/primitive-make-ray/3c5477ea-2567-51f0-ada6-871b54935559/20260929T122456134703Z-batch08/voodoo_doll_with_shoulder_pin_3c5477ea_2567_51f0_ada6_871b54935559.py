"""The rejected doll became a stick person holding a pin; restore a rounded stuffed body and a pin entering its shoulder. No written reviewer feedback.
Symbol plan: Source toy silhouette and shared human reference for round limbs. Continuous toy head/body connection; no detached-human gap applies.
Keyshape SQUARE, authored on the SOLO48 integer grid with 4-unit strokes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='3c5477ea-2567-51f0-ada6-871b54935559'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__voodoo-doll-with-shoulder-pin/20260929T121814Z-thuan-mac/reference/halloween voodoo doll_3c5477ea-2567-51f0-ada6-871b54935559.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='voodoo-doll-with-shoulder-pin'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='primitives-generate'
    aliases=()
    keywords=('voodoo', 'doll', 'with', 'shoulder', 'pin')

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

        self.circle('head',20,14,8)
        self.path('body',(16,22),[('L',(6,28)),('A',(10,34),4,4,False),('L',(14,32)),('L',(12,38)),('A',(20,40),4,4,False),('L',(23,34)),('L',(26,40)),('A',(34,38),4,4,False),('L',(30,28)),('L',(24,22))]);self.relate('connect','head','body')
        self.circle('pin-head',39,10,3)
        self.add_line('pin',(37,12),(30,28));self.relate('connect','pin','pin-head');self.relate('connect','pin','body')

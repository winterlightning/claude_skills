"""adjustable-brightness-light-bulb. Reconstructed clean centerlines from the original reference.
Construction reference: lightbulb. Keyshape SQUARE chosen for the composition.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='afa0c105-3fb7-4c77-b44d-80888cf292ec'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__adjustable-brightness-light-bulb/20260925T034142Z-thuan-mac/reference/adjustable lamp 1_afa0c105-3fb7-4c77-b44d-80888cf292ec.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='adjustable-brightness-light-bulb'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/reference'
    aliases=()
    keywords=('adjustable', 'brightness', 'light', 'bulb')
    def build(self):
        # Root owns a circular dial arc, centered bulb, and detached dial indicator.
        self.path('dial',(6,24),[('A',(24,6),18,18,True),('C',(39,14),(30,6),(36,9))])
        self.path('bulb',(15,23),[('A',(27,23),6,6,True),('C',(26,32),(27,27),(26,28)),('L',(26,34)),('A',(21,39),5,5,True),('A',(16,34),5,5,True),('L',(16,32)),('C',(15,23),(16,28),(15,27))],True)
        self.add_line('contact',(21,39),(21,42));self.join('bulb','contact')
        self.circle('indicator',39,30,3)

    def path(self,n,p,ops,closed=False):
        members=[]
        for i,(kind,q,*v) in enumerate(ops):
            eid=f'{n}-{i}'
            if kind=='L': self.add_line(eid,p,q)
            elif kind=='A': self.add_arc(eid,p,q,radius_x=v[0],radius_y=v[1],sweep=v[2])
            elif kind=='C': self.add_bezier(eid,p,(v[0],v[1],q))
            members.append(eid);p=q
        self.add_contour(n,*members,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
    def join(self,a,b): self.relate('connect',a,b)

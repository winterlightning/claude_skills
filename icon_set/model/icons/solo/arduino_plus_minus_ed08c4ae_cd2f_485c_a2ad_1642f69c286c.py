"""arduino-plus-minus. Reconstructed clean centerlines from the original reference.
Construction reference: infinity. Keyshape HRECT_M chosen for the composition.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='ed08c4ae-cd2f-485c-a2ad-1642f69c286c'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__arduino-plus-minus/20260925T034142Z-thuan-mac/reference/arduino plus minus_ed08c4ae-cd2f-485c-a2ad-1642f69c286c.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='arduino-plus-minus'
    keyshape=Keyshape.HRECT_M
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/reference'
    aliases=()
    keywords=('arduino', 'plus', 'minus')
    def build(self):
        # One continuous infinity stroke: tangent directions cross diagonally.
        self.path('infinity',(14,10),[('A',(4,24),10,14,False),('A',(14,38),10,14,False),('C',(34,10),(23,38),(25,10)),('A',(44,24),10,14,True),('A',(34,38),10,14,True),('C',(14,10),(25,38),(23,10))],True)
        self.add_line('minus',(13,24),(15,24))
        self.add_line('plus-horizontal',(33,24),(35,24))
        self.add_line('plus-vertical',(34,22),(34,26));self.join('plus-horizontal','plus-vertical')

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

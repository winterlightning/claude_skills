"""broad-bladed-medieval-axe. Reconstructed clean centerlines from the original reference.
Construction reference: axe. Keyshape SQUARE chosen for the composition.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='9cc63cfd-be10-4af6-b277-92e252919cc7'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__broad-bladed-medieval-axe/20260925T034142Z-thuan-mac/reference/fantasy medieval excutioner axe_9cc63cfd-be10-4af6-b277-92e252919cc7.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='broad-bladed-medieval-axe'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/reference'
    aliases=()
    keywords=('broad', 'bladed', 'medieval', 'axe')
    def build(self):
        # Straight diagonal shaft. Blade has one smooth cutting ellipse and
        # two flowing concave shoulders; angular collar remains intentional.
        self.add_line('shaft',(6,42),(24,24))
        self.path('blade',(24,24),[('L',(18,18)),('L',(30,6)),('C',(42,18),(30,14),(36,18)),('A',(26,38),16,20,True),('C',(24,24),(28,32),(28,28))],True)
        self.join('shaft','blade')

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

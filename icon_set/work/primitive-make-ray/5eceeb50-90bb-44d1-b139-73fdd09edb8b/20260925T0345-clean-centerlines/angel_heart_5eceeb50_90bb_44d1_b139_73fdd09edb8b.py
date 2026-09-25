"""angel-heart. Reconstructed clean centerlines from the original reference.
Construction reference: heart. Keyshape SQUARE chosen for the composition.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='5eceeb50-90bb-44d1-b139-73fdd09edb8b'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__angel-heart/20260925T034142Z-thuan-mac/reference/love it angel_5eceeb50-90bb-44d1-b139-73fdd09edb8b.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='angel-heart'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/reference'
    aliases=()
    keywords=('angel', 'heart')
    def build(self):
        # A shared axis owns heart lobes, halo, and mirrored wings.
        self.path('halo',(16,10),[('A',(32,10),8,4,True),('A',(16,10),8,4,True)],True)
        self.path('heart',(24,28),[('C',(14,28),(24,20),(14,20)),('C',(24,40),(14,33),(19,37)),('C',(34,28),(29,37),(34,33)),('C',(24,28),(34,20),(24,20))],True)
        for n,s in [('left',1),('right',-1)]:
            def p(x,y):return (24+s*(x-24),y)
            self.path(n,p(14,28),[('C',p(6,28),p(14,20),p(6,20)),('L',p(6,38)),('A',p(14,38),4,4,s<0),('L',p(14,35))])
            self.join('heart',n)

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

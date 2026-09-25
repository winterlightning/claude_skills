"""autism-disorder-symptoms. Reconstructed clean centerlines from the original reference.
Construction reference: puzzle and human profile reference. Keyshape SQUARE chosen for the composition.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='4a264e06-6d44-57cc-8176-d57369c6c0ee'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__autism-disorder-symptoms/20260925T034142Z-thuan-mac/reference/autism disorder symptoms_4a264e06-6d44-57cc-8176-d57369c6c0ee.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='autism-disorder-symptoms'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'health'
    aliases=()
    keywords=('autism', 'disorder', 'symptoms')
    def build(self):
        # Puzzle piece owns the round tab; continuous profile owns brow, nose,
        # jaw and neck. Deliberate asymmetric side view, no detached human head.
        self.path('piece',(6,16),[('A',(16,6),10,10,True),('L',(22,6)),('L',(22,16)),('L',(18,16)),('A',(10,16),4,4,True),('L',(6,16))],True)
        self.path('profile',(14,42),[('L',(14,39)),('C',(6,29),(14,35),(6,34)),('L',(20,29)),('A',(30,29),5,5,False),('L',(32,29)),('L',(32,14)),('C',(38,25),(36,15),(38,20)),('L',(42,30)),('L',(38,30)),('L',(38,34)),('A',(34,38),4,4,True),('L',(30,38)),('L',(30,42))])

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

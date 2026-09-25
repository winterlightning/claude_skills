"""aerial-yoga-bow-pose. Reconstructed clean centerlines from the original reference.
Construction reference: human_ref/full_body_ref.png (no exact Lucide pose). Keyshape SQUARE chosen for the composition.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='4a1112c6-2f20-434b-b756-511460d08610'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__aerial-yoga-bow-pose/20260925T034142Z-thuan-mac/reference/aerial yoga bow pose_4a1112c6-2f20-434b-b756-511460d08610.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='aerial-yoga-bow-pose'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    aliases=()
    keywords=('aerial', 'yoga', 'bow', 'pose')
    def build(self):
        # Two straps, one coherent folded limb and one smooth torso. Head radius3,
        # center39,39; neck28,39 is exactly8 from head outline /4 between ink.
        self.add_polyline('strap-left',(18,6),(16,18),(16,26))
        self.path('strap-right',(27,6),[('L',(25,18)),('C',(16,26),(24,23),(22,26))])
        self.join('strap-left','strap-right')
        self.path('folded-leg',(16,18),[('A',(6,28),10,10,False),('L',(6,36)),('A',(18,36),6,6,False),('C',(16,26),(18,32),(16,30))])
        self.join('folded-leg','strap-left');self.join('folded-leg','strap-right')
        self.path('body',(25,18),[('C',(34,26),(30,18),(37,22)),('C',(24,36),(31,31),(24,32)),('A',(27,39),3,3,False)])
        self.add_line('torso',(27,39),(28,39))
        self.join('body','torso');self.join('body','strap-right')
        self.circle('head',39,39,3)
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='end')

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

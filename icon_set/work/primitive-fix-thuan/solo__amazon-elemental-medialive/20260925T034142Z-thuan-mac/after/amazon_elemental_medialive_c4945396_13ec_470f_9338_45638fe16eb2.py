"""amazon-elemental-medialive. Reconstructed clean centerlines from the original reference.
Construction reference: no useful exact Lucide match; reference three-way layout. Keyshape SQUARE chosen for the composition.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='c4945396-13ec-470f-9338-45638fe16eb2'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__amazon-elemental-medialive/20260925T034142Z-thuan-mac/reference/amazon web service elemental medialive_c4945396-13ec-470f-9338-45638fe16eb2.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='amazon-elemental-medialive'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/reference'
    aliases=()
    keywords=('amazon', 'elemental', 'medialive')
    def build(self):
        # Equal circular media nodes replace hexagonal corners at this scale.
        # Centerline envelope (6,6)-(42,42), symmetric upper scan chevrons.
        self.add_polyline('play',(18,20),(30,26),(18,32),closed=True)
        for n,x,y in [('top',24,9),('left',9,39),('right',39,39)]:self.circle(n,x,y,3)
        self.add_polyline('scan-left',(9,15),(6,18),(9,21))
        self.add_polyline('scan-right',(39,15),(42,18),(39,21))
        self.add_polyline('scan-bottom',(22,40),(24,42),(26,40))

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

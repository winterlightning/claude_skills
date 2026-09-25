"""a-with-sync-arrow. Reconstructed clean centerlines from the original reference.
Construction reference: refresh-cw. Keyshape SQUARE chosen for the composition.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='8d0a0eeb-161b-49dd-b5f6-5bcfc4e716d9'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__a-with-sync-arrow/20260925T034142Z-thuan-mac/reference/a with sync arrow_8d0a0eeb-161b-49dd-b5f6-5bcfc4e716d9.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='a-with-sync-arrow'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/reference'
    aliases=()
    keywords=('a', 'with', 'sync', 'arrow')
    def build(self):
        # Two rotationally paired elliptical sweeps; straight, mirrored A strokes.
        self.path('upper',(6,19),[('A',(42,19),18,13,True)])
        self.add_polyline('upper-head',(39,19),(42,19),(42,13));self.join('upper','upper-head')
        self.path('lower',(42,29),[('A',(6,29),18,13,True)])
        self.add_polyline('lower-head',(9,29),(6,29),(6,35));self.join('lower','lower-head')
        self.add_polyline('a',(17,31),(18,29),(24,17),(30,29),(31,31))
        self.add_line('crossbar',(18,29),(30,29));self.join('a','crossbar')

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

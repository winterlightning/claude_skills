"""autonomous-car-sensor-signal. Reconstructed clean centerlines from the original reference.
Construction reference: car-front. Keyshape SQUARE chosen for the composition.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='8a6f5388-93e2-4e87-bb21-8db3666f5c20'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__autonomous-car-sensor-signal/20260925T034142Z-thuan-mac/reference/auto pilot car radius_8a6f5388-93e2-4e87-bb21-8db3666f5c20.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='autonomous-car-sensor-signal'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    aliases=()
    keywords=('autonomous', 'car', 'sensor', 'signal')
    def build(self):
        # Four equal circular sensor quadrants. Mirrored roof and true circular wheels.
        for ix in (0,1):
            for iy in (0,1):
                def p(x,y):return (48-x if ix else x,48-y if iy else y)
                self.add_arc(f'sensor-{ix}-{iy}',p(6,18),p(18,6),radius_x=12,sweep=ix==iy)
        self.path('roof',(14,29),[('L',(14,26)),('C',(19,21),(14,23),(17,24)),('C',(22,18),(20,19),(20,18)),('L',(26,18)),('C',(29,21),(28,18),(28,19)),('C',(34,26),(31,24),(34,23)),('L',(34,29))])
        self.add_arc('left-wheel',(20,29),(14,29),radius_x=3)
        self.add_arc('right-wheel',(34,29),(28,29),radius_x=3)
        self.add_line('chassis',(28,29),(20,29))
        self.add_contour('car','roof-0','roof-1','roof-2','roof-3','roof-4','roof-5','roof-6','right-wheel','chassis','left-wheel',closed=True)

    def path(self,n,p,ops,closed=False):
        members=[]
        for i,(kind,q,*v) in enumerate(ops):
            eid=f'{n}-{i}'
            if kind=='L': self.add_line(eid,p,q)
            elif kind=='A': self.add_arc(eid,p,q,radius_x=v[0],radius_y=v[1],sweep=v[2])
            elif kind=='C': self.add_bezier(eid,p,(v[0],v[1],q))
            members.append(eid);p=q
        if n!='roof': self.add_contour(n,*members,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
    def join(self,a,b): self.relate('connect',a,b)

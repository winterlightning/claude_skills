'Restored the lid knob and feet, enlarged the open control dial and kept a symmetric tapered pot.\nSymbol plan: coherent named contours, common repeated dimensions and shared joins.\nConstruction: Lucide cooking-pot, original and atomic geometry inspected.\nKeyshape SQUARE; integer SOLO48 geometry. Human faces follow circular jaw construction; no detached torso.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='84ea8179-ecd2-5ac3-8140-a585e67f26c1'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__electric-slow-cooker-batch-011-03/20260925T085649Z-thuan-mac/reference/appliances slow cooker_84ea8179-ecd2-5ac3-8140-a585e67f26c1.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='electric-slow-cooker-batch-011-03'
    keyshape=Keyshape.SQUARE
    exception={'reason': 'Accept the curved-distance uncertainty at the circular dial against the pot. The authored vertical ink clearance is 4px and the dial is centered with a visible opening.', 'approved_by': 'user-delegated visual judgment, gpt-6', 'approved_on': '2026-09-25', 'svg_sha256': 'd284d954ac862388e0c927eae809653e2124d4479cba991fb240cf260f39ca72'}
    semantic_role="MAIN"
    semantic_kind="noun"
    category='food'
    aliases=()
    keywords=('electric', 'slow', 'cooker', 'batch', '011', '03')

    def path(self,n,p,*steps,closed=False):
        ids=[]
        for i,s in enumerate(steps):
            k=f'{n}-{i}'
            if s[0]=='L': q=s[1]; self.add_line(k,p,q)
            elif s[0]=='A': q=s[1]; self.add_arc(k,p,q,radius_x=s[2],radius_y=s[3],sweep=s[4])
            else: q=s[3]; self.add_bezier(k,p,(s[1],s[2],q))
            ids.append(k);p=q
        self.add_contour(n,*ids,closed=closed)
    def oval(self,n,x,y,rx,ry=None):
        ry=rx if ry is None else ry
        self.path(n,(x,y-ry),('A',(x+rx,y),rx,ry,True),('A',(x,y+ry),rx,ry,True),('A',(x-rx,y),rx,ry,True),('A',(x,y-ry),rx,ry,True),closed=True)
    def box(self,n,l,t,r,b,q=3):
        self.path(n,(l+q,t),('L',(r-q,t)),('A',(r,t+q),q,q,True),('L',(r,b-q)),('A',(r-q,b),q,q,True),('L',(l+q,b)),('A',(l,b-q),q,q,True),('L',(l,t+q)),('A',(l+q,t),q,q,True),closed=True)

    def build(self):
        self.path('pot',(6,18),('L',(10,37)),('C',(11,40),(14,40),(17,40)),('L',(31,40)),('C',(34,40),(37,40),(38,37)),('L',(42,18)),('L',(6,18)),closed=True)
        self.path('lid',(6,18),('C',(9,10),(15,11),(24,11)),('C',(33,11),(39,10),(42,18)));self.relate('connect','pot','lid')
        self.add_line('knob-stem',(24,6),(24,11));self.relate('connect','knob-stem','lid')
        self.oval('dial',24,29,3)
        for i,x in enumerate((14,34)):
         self.add_line(f'foot-{i}',(x,40),(x,42));self.relate('connect',f'foot-{i}','pot')

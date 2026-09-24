from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='77937bbd-92c4-4b29-ac40-52719ed0b6cd'
SOURCE_PATH='pictographic-primitives/_uncategorized_32/religion cao dai_77937bbd-92c4-4b29-ac40-52719ed0b6cd.svg'
AUTHOR='gpt-6'
PLAN='A divine eye within the Cao Dai triangle. Upper eyelid genuinely joins split triangle sides at10,34 and38,34. Symmetric about x24. Eye is intentionally stylized with a straight lower boundary.'
CONSTRUCTION_REFERENCE='Lucide eye lens vocabulary; triangle from source'
class Drawing(Solo48):
    icon_id='religion-cao-dai'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('religion', 'cao', 'dai')
    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)
    def box(self,n,l,t,r,b,k=4):
        ps=[(l+k,t),(r-k,t),(r,t+k),(r,b-k),(r-k,b),(l+k,b),(l,b-k),(l,t+k)]
        ns=[]
        for j,a in enumerate(ps):
            z=ps[(j+1)%8]
            if a==z: continue
            m=f'{n}-{j}'; ns.append(m)
            if j%2:self.add_arc(m,a,z,radius_x=k)
            else:self.add_line(m,a,z)
        self.add_contour(n,*ns,closed=True)
    def cross(self,n,x,y,r):
        ns=[]
        for j,p in enumerate([(x-r,y),(x+r,y),(x,y-r),(x,y+r)]):
            m=f'{n}-{j}';ns.append(m);self.add_line(m,(x,y),p)
        self.relate('connect',*ns)
    def build(self):
        self.add_polyline('triangle',(10,34),(24,6),(38,34),(42,42),(6,42),closed=True)
        self.add_arc('eyelid',(10,34),(38,34),radius_x=14,radius_y=10)
        self.relate('connect','eyelid','triangle')
        self.add_dot('pupil',(24,33))

FINAL_OMISSIONS = 'Merge lower eye boundary with triangle base; reduce iris to pupil dot.'
VISUAL_REVIEW = 'Upper eyelid genuinely joins split triangle sides at10,34 and38,34. Symmetric about x24. Eye is intentionally stylized with a straight lower boundary.'

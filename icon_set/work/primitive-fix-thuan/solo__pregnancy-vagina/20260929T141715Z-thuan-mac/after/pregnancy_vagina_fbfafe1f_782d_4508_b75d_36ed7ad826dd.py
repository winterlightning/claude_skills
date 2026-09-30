"""Rebalance mirrored waist and hip curves around a wider, lower heart-shaped pelvis and centered seam.
Symbol plan: Rebalance mirrored waist and hip curves around a wider, lower heart-shaped pelvis and centered seam.
Construction reference: Lucide heart: paired smooth lobes; supplied torso original defines the anatomical fragment.
Omissions: None
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='fbfafe1f-782d-4508-b75d-36ed7ad826dd'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__pregnancy-vagina/20260929T141715Z-thuan-mac/reference/pregnancy vagina_fbfafe1f-782d-4508-b75d-36ed7ad826dd.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='pregnancy-vagina'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=()

    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)
    def box(self,n,l,t,r,b,k=3):
        pts=[(l+k,t),(r-k,t),(r,t+k),(r,b-k),(r-k,b),(l+k,b),(l,b-k),(l,t+k)]
        ids=[]
        for i,a in enumerate(pts):
            z=pts[(i+1)%8]
            if a==z:continue
            q=n+str(i);ids.append(q)
            if i%2:self.add_arc(q,a,z,radius_x=k)
            else:self.add_line(q,a,z)
        self.add_contour(n,*ids,closed=True)

    def build(self):
        for side,sg in [('l',-1),('r',1)]:
            def p(x,y):return (24+sg*x,y)
            self.add_bezier('waist-'+side,p(12,4),(p(9,12),p(13,18),p(15,22)),(p(16,25),p(16,29),p(16,32)),(p(16,37),p(15,41),p(14,44)))
        self.add_bezier('heart-l',(24,29),((20,23),(15,26),(17,31)),((18,34),(21,36),(24,39)))
        self.add_bezier('heart-r',(24,39),((27,36),(30,34),(31,31)),((33,26),(28,23),(24,29)))
        self.add_contour('heart','heart-l','heart-r',closed=True)
        self.add_line('pelvic-seam',(24,39),(24,44));self.relate('connect','heart','pelvic-seam')

"""Use a shared mirrored pair of wider triangles, shorten the central axis, and broaden the overhead right arrow.
Symbol plan: Use a shared mirrored pair of wider triangles, shorten the central axis, and broaden the overhead right arrow.
Construction reference: Lucide flip-horizontal-2: mirrored triangular forms around one axis.
Omissions: None
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='0612d818-cafc-45a8-8575-34af044e11de'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__reflect-right/20260929T141715Z-thuan-mac/reference/reflect right_0612d818-cafc-45a8-8575-34af044e11de.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='reflect-right'
    keyshape=Keyshape.HRECT_L
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
        self.add_line('axis',(24,24),(24,40))
        for side,x,tip in [('left',4,16),('right',44,32)]:
            self.add_polyline(side,(x,22),(tip,31),(x,40),closed=True)
        self.add_arc('sweep',(12,16),(36,16),radius_x=12,radius_y=8)
        x=36
        self.add_polyline('arrow',(x-5,11),(x,16),(x+5,11))
        self.relate('connect','sweep','arrow')

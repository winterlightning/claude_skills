"""Restore a steeper rising arrow above three equal-width ascending columns. Keep shared baseline.
Symbol plan: Restore a steeper rising arrow above three equal-width ascending columns. Keep shared baseline.
Construction reference: Lucide chart-no-axes-column-increasing: repeated equal-pitch rising columns.
Omissions: None
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='4cb4eabd-1bfb-46c2-ab15-0b351ab22677'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__real-estate-market-building-increase/20260929T141715Z-thuan-mac/reference/real estate market building increase_4cb4eabd-1bfb-46c2-ab15-0b351ab22677.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='real-estate-market-building-increase'
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
        for i,(x,y) in enumerate(((4,32),(20,24),(36,16))):
            self.add_polyline('bar'+str(i),(x,40),(x,y),(x+8,y),(x+8,40),closed=True)
        self.add_line('trend',(4,23),(24,8))
        self.add_polyline('arrow',(16,8),(24,8),(24,16))
        self.relate('connect','trend','arrow')

        self.add_polyline('baseline',(4,40),(12,40),(20,40),(28,40),(36,40),(44,40))
        for i in range(3):self.relate('connect','baseline','bar'+str(i))

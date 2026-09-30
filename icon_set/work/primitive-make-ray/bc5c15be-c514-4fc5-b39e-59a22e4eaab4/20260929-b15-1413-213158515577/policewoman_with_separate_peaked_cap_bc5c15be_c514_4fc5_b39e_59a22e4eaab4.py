"""Close the peaked cap, retain a circular jaw, restore hanging side hair, and balance the uniform shoulders and center seam.
Symbol plan: Close the peaked cap, retain a circular jaw, restore hanging side hair, and balance the uniform shoulders and center seam.
Construction reference: human_ref/user.svg: circular face and smooth shoulders; avatar touching-ink contact is 4 centerline units.
Omissions: Small uniform pocket and fine hat band omitted.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='bc5c15be-c514-4fc5-b39e-59a22e4eaab4'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__policewoman-with-separate-peaked-cap/20260929T141715Z-thuan-mac/reference/police woman_bc5c15be-c514-4fc5-b39e-59a22e4eaab4.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='policewoman-with-separate-peaked-cap'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='avatars'
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
        self.add_polyline('cap',(8,8),(24,4),(40,8),(36,16),(12,16),closed=True)
        self.add_arc('jaw',(32,24),(16,24),radius_x=8)
        for x in (8,40):self.add_line('hair'+str(x),(x,24),(x,30))
        self.add_arc('shoulder-l',(8,44),(24,36),radius_x=16,radius_y=8)
        self.add_arc('shoulder-r',(24,36),(40,44),radius_x=16,radius_y=8)
        self.add_contour('shoulders','shoulder-l','shoulder-r')
        self.relate('connect','jaw','shoulders')
        self.add_line('uniform-seam',(24,36),(24,44));self.relate('connect','shoulders','uniform-seam')

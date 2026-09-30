"""Use an open rising sun with short rays above two differently sized round flowers, both with stems and a leaf on the taller flower.
Symbol plan: Use an open rising sun with short rays above two differently sized round flowers, both with stems and a leaf on the taller flower.
Construction reference: Lucide sun and flower: repeated radial details around circular centers; supplied source owns the unequal flowers.
Omissions: Fine detached ray count reduced for the 48px composition.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='1390e012-2151-49eb-9917-83a27c15c4af'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-fix-thuan/solo__sun-and-sunflowers/20260929T142009Z-thuan-mac/reference/outdoors sun plants_1390e012-2151-49eb-9917-83a27c15c4af.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='sun-and-sunflowers'
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
        # Open sun above two flowering stems; bloom sizes deliberately differ.
        self.add_arc('sun',(6,20),(22,20),radius_x=8)
        self.add_line('sun-top-ray',(14,8),(14,12));self.relate('connect','sun','sun-top-ray')
        self.add_line('sun-left-ray',(4,20),(6,20));self.relate('connect','sun','sun-left-ray')
        for n,cx,cy,r in [('small',12,33,4),('large',36,26,6)]:
            self.circle(n,cx,cy,r)
            self.add_line(n+'-stem',(cx,cy+r),(cx,40));self.relate('connect',n,n+'-stem')
            for j,(a,z) in enumerate([((cx-r,cy),(cx-r-2,cy)),((cx+r,cy),(cx+r+2,cy)),((cx,cy-r),(cx,cy-r-2))]):
                self.add_line(n+'-ray'+str(j),a,z);self.relate('connect',n,n+'-ray'+str(j))
        self.add_line('leaf',(36,40),(43,38));self.relate('connect','large-stem','leaf')

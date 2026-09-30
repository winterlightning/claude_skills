"""Rebuild the stack as three overlapping smooth oval slices with a complete foreground oval.
Symbol plan: Rebuild the stack as three overlapping smooth oval slices with a complete foreground oval.
Construction reference: No useful exact local Lucide match; supplied original determines the oval stack and occlusion.
Omissions: None
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='600abb76-55a0-48a0-9c01-0a94b6498aa6'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-fix-thuan/solo__three-overlapping-mozzarella-slices-600abb76/20260929T142009Z-thuan-mac/reference/mozzarella_600abb76-55a0-48a0-9c01-0a94b6498aa6.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='three-overlapping-mozzarella-slices-600abb76'
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
        self.add_arc('front-top',(4,31),(32,31),radius_x=14,radius_y=9)
        self.add_arc('front-bottom',(32,31),(4,31),radius_x=14,radius_y=9)
        self.add_contour('front','front-top','front-bottom',closed=True)
        self.add_bezier('middle',(4,31),((0,13),(27,10),(34,22)),((38,28),(38,32),(32,31)))
        self.relate('connect','front','middle')
        self.add_bezier('back',(15,17),((15,5),(36,3),(42,17)),((46,27),(44,31),(36,31)))

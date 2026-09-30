"""Restore a raised finger and thumb with four outward arrows and short shafts.
Symbol plan: Restore a raised finger and thumb with four outward arrows and short shafts.
Construction reference: Lucide move: four cardinal arrows; supplied source establishes the tap hand.
Omissions: Tap halo omitted to preserve the hand and arrow spacing.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='3404178e-6c6c-4e81-923b-4c9570a627a0'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-fix-thuan/solo__tap-gesture-expand-all-directions/20260929T142009Z-thuan-mac/reference/gesture tap expand all direction_3404178e-6c6c-4e81-923b-4c9570a627a0.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='tap-gesture-expand-all-directions'
    keyshape=Keyshape.SQUARE
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
        # One raised finger with a thumb, surrounded by four outward open arrows.
        self.add_arc('fingertip',(20,24),(28,24),radius_x=4)
        self.add_line('finger-side',(20,24),(20,31))
        self.add_polyline('hand',(20,31),(16,28),(20,34),(28,34),(30,28),(28,26),(28,24))
        self.relate('connect','fingertip','finger-side');self.relate('connect','finger-side','hand');self.relate('connect','fingertip','hand')
        for n,pts,a,z in [
         ('up',[(20,10),(24,6),(28,10)],(24,6),(24,12)),
         ('down',[(20,38),(24,42),(28,38)],(24,42),(24,38)),
         ('left',[(10,20),(6,24),(10,28)],(6,24),(12,24)),
         ('right',[(38,20),(42,24),(38,28)],(42,24),(36,24))]:
            self.add_polyline(n,*pts);self.add_line(n+'-shaft',a,z);self.relate('connect',n,n+'-shaft')

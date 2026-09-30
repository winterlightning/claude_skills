"""Restore a closed pointing finger and thumb, then broaden all four directional arrowheads and preserve short shafts.
Symbol plan: Restore a closed pointing finger and thumb, then broaden all four directional arrowheads and preserve short shafts.
Construction reference: Lucide move: four cardinal arrows; supplied source establishes the tap hand.
Omissions: Tap halo and tiny finger joints omitted for legal spacing.
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
        self.add_arc('fingertip',(20,22),(28,22),radius_x=4)
        self.add_polyline('finger',(28,22),(28,28),(20,28),(20,26),(20,22));self.relate('connect','finger','fingertip')
        self.add_line('thumb',(17,24),(20,26));self.relate('connect','thumb','finger')
        for n,pts,a,z in [
         ('up',[(18,11),(24,6),(30,11)],(24,6),(24,10)),
         ('down',[(18,36),(24,42),(30,36)],(24,42),(24,38)),
         ('left',[(10,18),(6,24),(10,30)],(6,24),(9,24)),
         ('right',[(38,18),(42,24),(38,30)],(42,24),(39,24))]:
            self.add_polyline(n,*pts);self.add_line(n+'-shaft',a,z);self.relate('connect',n,n+'-shaft')

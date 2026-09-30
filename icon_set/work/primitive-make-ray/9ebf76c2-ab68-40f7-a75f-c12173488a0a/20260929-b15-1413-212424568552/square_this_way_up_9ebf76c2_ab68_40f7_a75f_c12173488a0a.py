"""Use paired open 45-degree arrowheads with equal stems and a centered baseline inside a softly rounded sign.
Symbol plan: Use paired open 45-degree arrowheads with equal stems and a centered baseline inside a softly rounded sign.
Construction reference: Lucide move: separate shaft and open arrow wings.
Omissions: Sign widened to HRECT_L to give both arrowheads legal spacing.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='9ebf76c2-ab68-40f7-a75f-c12173488a0a'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-fix-thuan/solo__square-this-way-up/20260929T142009Z-thuan-mac/reference/square this way up_9ebf76c2-ab68-40f7-a75f-c12173488a0a.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='square-this-way-up'
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
        self.box('frame',4,8,44,40,4)
        for i,x in enumerate((16,32)):
            self.add_line('shaft'+str(i),(x,16),(x,24))
            self.add_polyline('head'+str(i),(x-4,20),(x,16),(x+4,20))
            self.relate('connect','shaft'+str(i),'head'+str(i))
        self.add_line('base',(12,32),(36,32))

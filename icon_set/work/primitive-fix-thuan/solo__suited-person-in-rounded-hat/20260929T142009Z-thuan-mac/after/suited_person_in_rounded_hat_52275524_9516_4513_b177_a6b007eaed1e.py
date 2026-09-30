"""Restore the rounded hat and projecting brim, V suit lapels and a central tie below an exact 4-unit detached head-to-torso gap.
Symbol plan: Restore the rounded hat and projecting brim, V suit lapels and a central tie below an exact 4-unit detached head-to-torso gap.
Construction reference: human_ref/user.svg: circular jaw and broad shoulders; Lucide hat-glasses informs the distinct brim.
Omissions: Enclosed tie diamond simplified to a short tie stroke.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='52275524-9516-4513-b177-a6b007eaed1e'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-fix-thuan/solo__suited-person-in-rounded-hat/20260929T142009Z-thuan-mac/reference/governor_52275524-9516-4513-b177-a6b007eaed1e.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='suited-person-in-rounded-hat'
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
        self.add_arc('crown',(12,14),(36,14),radius_x=12,radius_y=10)
        self.add_polyline('brim',(8,14),(12,14),(36,14),(40,14));self.relate('connect','crown','brim')
        self.add_arc('face',(33,14),(15,14),radius_x=9)
        self.relate('connect','face','brim')
        self.add_polyline('collar',(16,32),(24,40),(32,32))
        self.add_arc('shoulder-left',(8,44),(16,32),radius_x=8,radius_y=12)
        self.add_arc('shoulder-right',(32,32),(40,44),radius_x=8,radius_y=12)
        self.relate('connect','collar','shoulder-left');self.relate('connect','collar','shoulder-right')
        self.add_line('tie',(24,40),(24,44));self.relate('connect','collar','tie')

        self.add_line('upper-tie',(24,31),(24,40));self.relate('connect','upper-tie','collar');self.relate('connect','upper-tie','tie')
